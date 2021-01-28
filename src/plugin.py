import asyncio
import json
import os
import sys
import multiprocessing
import webbrowser
import requests
import requests.cookies
import logging as log
import subprocess
import time
import re
from typing import Union, List, Dict

from galaxy.api.consts import LocalGameState, Platform
from galaxy.api.plugin import Plugin, create_and_run_plugin
from galaxy.api.types import Achievement, Game, LicenseInfo, LocalGame, GameTime, LicenseType
from galaxy.api.errors import (
    AuthenticationRequired, BackendTimeout, BackendNotAvailable, BackendError,
    NetworkError, UnknownError, InvalidCredentials, UnknownBackendResponse
)

from version import __version__ as version
from process import ProcessProvider
from local_client_base import ClientNotInstalledError
from local_client import LocalClient
from backend import BackendClient, AccessTokenExpired
from definitions import Blizzard, DataclassJSONEncoder, BlizzardGame, ClassicGame
from consts import SYSTEM
from consts import Platform as pf
from http_client import AuthenticatedHttpClient


class BNetPlugin(Plugin):
    def __init__(self, reader, writer, token):
        super().__init__(Platform.Battlenet, version, reader, writer, token)
        self.local_client = LocalClient(self._update_statuses)
        self.authentication_client = AuthenticatedHttpClient(self)
        self.backend_client = BackendClient(self, self.authentication_client)

        self.watched_running_games = set()

    async def _notify_about_game_stop(self, game, starting_timeout):
        id_to_watch = game.info.uid

        if id_to_watch in self.watched_running_games:
            log.debug(f'Game {id_to_watch} is already watched. Skipping')
            return

        try:
            self.watched_running_games.add(id_to_watch)
            await asyncio.sleep(starting_timeout)
            ProcessProvider().update_games_processes([game])
            log.info(f'Setuping process watcher for {game._processes}')
            loop = asyncio.get_event_loop()
            await loop.run_in_executor(None, game.wait_until_game_stops)
        finally:
            self.update_local_game_status(LocalGame(id_to_watch, LocalGameState.Installed))
            self.watched_running_games.remove(id_to_watch)

    def _update_statuses(self, refreshed_games, previous_games):
        for blizz_id, refr in refreshed_games.items():
            prev = previous_games.get(blizz_id, None)

            if prev is None:
                if refr.has_galaxy_installed_state:
                    log.debug('Detected playable game')
                    state = LocalGameState.Installed
                else:
                    log.debug('Detected not-fully installed game')
                    state = LocalGameState.None_
            elif refr.has_galaxy_installed_state and not prev.has_galaxy_installed_state:
                log.debug('Detected playable game')
                state = LocalGameState.Installed
            elif refr.last_played != prev.last_played:
                log.debug('Detected launched game')
                state = LocalGameState.Installed | LocalGameState.Running
                asyncio.create_task(self._notify_about_game_stop(refr, 5))
            else:
                continue

            log.info(f'Changing game {blizz_id} state to {state}')
            self.update_local_game_status(LocalGame(blizz_id, state))

        for blizz_id, prev in previous_games.items():
            refr = refreshed_games.get(blizz_id, None)
            if refr is None:
                log.debug('Detected uninstalled game')
                state = LocalGameState.None_
                self.update_local_game_status(LocalGame(blizz_id, state))

    def log_out(self):
        if self.backend_client:
            asyncio.create_task(self.authentication_client.shutdown())
        self.authentication_client.user_details = None

    async def open_battlenet_browser(self):
        url = self.authentication_client.blizzard_battlenet_download_url
        log.info(f'Opening battle.net website: {url}')
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, lambda x: webbrowser.open(x, autoraise=True), url)

    async def install_game(self, game_id):
        if not self.authentication_client.is_authenticated():
            raise AuthenticationRequired()

        installed_game = self.local_client.get_installed_games().get(game_id, None)
        if installed_game and os.access(installed_game.install_path, os.F_OK):
            log.warning("Received install command on an already installed game")
            return await self.launch_game(game_id)

        if game_id in [classic.uid for classic in Blizzard.CLASSIC_GAMES]:
            if SYSTEM == pf.WINDOWS:
                platform = 'windows'
            elif SYSTEM == pf.MACOS:
                platform = 'macos'
            webbrowser.open(f"https://www.blizzard.com/download/confirmation?platform={platform}&locale=enUS&version=LIVE&id={game_id}")
            return
        try:
            self.local_client.refresh()
            log.info(f'Installing game of id {game_id}')
            self.local_client.install_game(game_id)
        except ClientNotInstalledError as e:
            log.warning(e)
            await self.open_battlenet_browser()
        except Exception as e:
            log.exception(f"Installing game {game_id} failed: {e}")

    def _open_battlenet_at_id(self, game_id):
        try:
            self.local_client.refresh()
            self.local_client.open_battlenet(game_id)
        except Exception as e:
            log.exception(f"Opening battlenet client on specific game_id {game_id} failed {e}")
            try:
                self.local_client.open_battlenet()
            except Exception as e:
                log.exception(f"Opening battlenet client failed {e}")

    async def uninstall_game(self, game_id):
        if not self.authentication_client.is_authenticated():
            raise AuthenticationRequired()

        if game_id == 'wow_classic':
            # attempting to uninstall classic wow through protocol gives you a message that the game cannot
            # be uninstalled through protocol and you should use battle.net
            return self._open_battlenet_at_id(game_id)

        if SYSTEM == pf.MACOS:
            self._open_battlenet_at_id(game_id)
        else:
            try:
                installed_game = self.local_client.get_installed_games().get(game_id, None)

                if installed_game is None or not os.access(installed_game.install_path, os.F_OK):
                    log.error(f'Cannot uninstall {game_id}')
                    self.update_local_game_status(LocalGame(game_id, LocalGameState.None_))
                    return

                if not isinstance(installed_game.info, ClassicGame):
                    if self.local_client.uninstaller is None:
                        raise FileNotFoundError('Uninstaller not found')

                uninstall_tag = installed_game.uninstall_tag
                client_lang = self.local_client.config_parser.locale_language
                self.local_client.uninstaller.uninstall_game(installed_game, uninstall_tag, client_lang)

            except Exception as e:
                log.exception(f'Uninstalling game {game_id} failed: {e}')

    async def launch_game(self, game_id):
        try:
            game = self.local_client.get_installed_games().get(game_id, None)
            if game is None:
                log.error(f'Launching game that is not installed: {game_id}')
                return await self.install_game(game_id)

            if isinstance(game.info, ClassicGame):
                log.info(f'Launching game of id: {game_id}, {game} at path {os.path.join(game.install_path, game.info.exe)}')
                if SYSTEM == pf.WINDOWS:
                    subprocess.Popen(os.path.join(game.install_path, game.info.exe))
                elif SYSTEM == pf.MACOS:
                    if not game.info.bundle_id:
                        log.warning(f"{game.name} has no bundle id, help by providing us bundle id of this game")
                    subprocess.Popen(['open', '-b', game.info.bundle_id])

                self.update_local_game_status(LocalGame(game_id, LocalGameState.Installed | LocalGameState.Running))
                asyncio.create_task(self._notify_about_game_stop(game, 6))
                return

            self.local_client.refresh()
            log.info(f'Launching game of id: {game_id}, {game}')
            await self.local_client.launch_game(game, wait_sec=60)

            self.update_local_game_status(LocalGame(game_id, LocalGameState.Installed | LocalGameState.Running))
            self.local_client.close_window()
            asyncio.create_task(self._notify_about_game_stop(game, 3))

        except ClientNotInstalledError as e:
            log.warning(e)
            await self.open_battlenet_browser()
        except TimeoutError as e:
            log.warning(str(e))
        except Exception as e:
            log.exception(f"Launching game {game_id} failed: {e}")

    async def authenticate(self, stored_credentials=None):
        try:
            if stored_credentials:
                auth_data = self.authentication_client.process_stored_credentials(stored_credentials)
                try:
                    await self.authentication_client.create_session()
                    await self.backend_client.refresh_cookies()
                    auth_status = await self.backend_client.validate_access_token(auth_data.access_token)
                except (BackendNotAvailable, BackendError, NetworkError, UnknownError, BackendTimeout) as e:
                    raise e
                except Exception:
                    raise InvalidCredentials()
                if self.authentication_client.validate_auth_status(auth_status):
                    self.authentication_client.user_details = await self.backend_client.get_user_info()
                return self.authentication_client.parse_user_details()
            else:
                return self.authentication_client.authenticate_using_login()
        except Exception as e:
            raise e

    async def pass_login_credentials(self, step, credentials, cookies):
        if "logout&app=oauth" in credentials['end_uri']:
            # 2fa expired, repeat authentication
            return self.authentication_client.authenticate_using_login()

        if self.authentication_client.attempted_to_set_battle_tag:
            self.authentication_client.user_details = await self.backend_client.get_user_info()
            return self.authentication_client.parse_auth_after_setting_battletag()

        cookie_jar = self.authentication_client.parse_cookies(cookies)
        auth_data = await self.authentication_client.get_auth_data_login(cookie_jar, credentials)

        try:
            await self.authentication_client.create_session()
            await self.backend_client.refresh_cookies()
        except (BackendNotAvailable, BackendError, NetworkError, UnknownError, BackendTimeout) as e:
            raise e
        except Exception:
            raise InvalidCredentials()

        auth_status = await self.backend_client.validate_access_token(auth_data.access_token)
        if not ("authorities" in auth_status and "IS_AUTHENTICATED_FULLY" in auth_status["authorities"]):
            raise InvalidCredentials()

        self.authentication_client.user_details = await self.backend_client.get_user_info()

        self.authentication_client.set_credentials()

        return self.authentication_client.parse_battletag()

    async def get_owned_games(self):
        if not self.authentication_client.is_authenticated():
            raise AuthenticationRequired()

        def _parse_battlenet_games(standard_games: dict, cn: bool) -> Dict[BlizzardGame, LicenseType]:
            licenses = {
                None: LicenseType.Unknown,
                "Trial": LicenseType.OtherUserLicense,
                "Good": LicenseType.SinglePurchase,
                "Inactive": LicenseType.SinglePurchase,
                "Banned": LicenseType.SinglePurchase,
                "Free": LicenseType.FreeToPlay
            }
            games = {}

            for standard_game in standard_games["gameAccounts"]:
                title_id = standard_game['titleId']
                try:
                    game = Blizzard.game_by_title_id(title_id, cn)
                except KeyError:
                    log.warning(f"Skipping unknown game with titleId: {title_id}")
                else:
                    games[game] = licenses[standard_game.get("gameAccountStatus")]

            # Add wow classic if retail wow is present in owned games
            wow_license = games.get(Blizzard['wow'])
            if wow_license is not None:
                games[Blizzard['wow_classic']] = wow_license
            return games

        def _parse_classic_games(classic_games: dict) -> Dict[ClassicGame, LicenseType]:
            games = {}
            for classic_game in classic_games["classicGames"]:
                sanitized_name = classic_game["localizedGameName"].replace(u'\xa0', ' ')
                for cg in Blizzard.CLASSIC_GAMES:
                    if cg.name == sanitized_name:
                        games[cg] = LicenseType.SinglePurchase
                        break
                else:
                    log.warning(f"Skipping unknown classic game with name: {sanitized_name}")
            return games

        cn = self.authentication_client.region == 'cn'

        battlenet_games = _parse_battlenet_games(await self.backend_client.get_owned_games(), cn)
        classic_games = _parse_classic_games(await self.backend_client.get_owned_classic_games())
        owned_games: Dict[BlizzardGame, LicenseType] = {**battlenet_games, **classic_games}

        for game in Blizzard.try_for_free_games(cn):
            if game not in owned_games:
                owned_games[game] = LicenseType.FreeToPlay

        return [
            Game(game.uid, game.name, None, LicenseInfo(license_type))
            for game, license_type in owned_games.items()
        ]

    async def get_local_games(self):
        timeout = time.time() + 2

        try:
            translated_installed_games = []

            while not self.local_client.games_finished_parsing():
                await asyncio.sleep(0.1)
                if time.time() >= timeout:
                    break

            running_games = self.local_client.get_running_games()
            installed_games = self.local_client.get_installed_games()
            log.info(f"Installed games {installed_games.items()}")
            log.info(f"Running games {running_games}")
            for uid, game in installed_games.items():
                if game.has_galaxy_installed_state:
                    state = LocalGameState.Installed
                    if uid in running_games:
                        state |= LocalGameState.Running
                else:
                    state = LocalGameState.None_
                translated_installed_games.append(LocalGame(uid, state))
            self.local_client.installed_games_cache = installed_games
            return translated_installed_games

        except Exception as e:
            log.exception(f"failed to get local games: {str(e)}")
            raise

    async def get_game_time(self, game_id, context):
        total_time = None
        last_played_time = None

        blizzard_game = Blizzard[game_id]

        if blizzard_game.name == "Overwatch":
            total_time = await self._get_overwatch_time()
            log.debug(f"Gametime for Overwatch is {total_time} minutes.")

        for config_info in self.local_client.config_parser.games:
            if config_info.uid == blizzard_game.uid:
                if config_info.last_played is not None:
                    last_played_time = int(config_info.last_played)
                break

        return GameTime(game_id, total_time, last_played_time)

    async def _get_overwatch_time(self) -> Union[None, int]:
        log.debug("Fetching playtime for Overwatch...")
        player_data = await self.backend_client.get_ow_player_data()
        if 'message' in player_data:  # user not found
            log.error('No Overwatch profile found.')
            return None
        if player_data['private'] == True:
            log.info('Unable to get data as Overwatch profile is private.')
            return None
        qp_time = player_data['playtime'].get('quickplay')
        if qp_time is None:  # user has not played quick play
            return 0
        if qp_time.count(':') == 1:  # minutes and seconds
            match = re.search('(?:(?P<m>\\d+):)(?P<s>\\d+)', qp_time)
            if match:
                return int(match.group('m'))
        elif qp_time.count(':') == 2:  # hours, minutes and seconds
            match = re.search('(?:(?P<h>\\d+):)(?P<m>\\d+)', qp_time)
            if match:
                return int(match.group('h')) * 60 + int(match.group('m'))
        raise UnknownBackendResponse(f'Unknown Overwatch API playtime format: {qp_time}')

    async def _get_wow_achievements(self):
        achievements = []
        try:
            characters_data = await self.backend_client.get_wow_character_data()
            characters_data = characters_data["characters"]

            wow_character_data = await asyncio.gather(
                *[
                    self.backend_client.get_wow_character_achievements(character["realm"], character["name"])
                    for character in characters_data
                ],
                return_exceptions=True,
            )

            for data in wow_character_data:
                if isinstance(data, requests.Timeout) or isinstance(data, requests.ConnectionError):
                    raise data

            wow_achievement_data = [
                list(
                    zip(
                        data["achievements"]["achievementsCompleted"],
                        data["achievements"]["achievementsCompletedTimestamp"],
                    )
                )
                for data in wow_character_data
                if type(data) is dict
            ]

            already_in = set()

            for char_ach in wow_achievement_data:
                for ach in char_ach:
                    if ach[0] not in already_in:
                        achievements.append(Achievement(achievement_id=ach[0], unlock_time=int(ach[1] / 1000)))
                        already_in.add(ach[0])
        except (AccessTokenExpired, BackendError) as e:
            log.exception(str(e))
        with open('wow.json', 'w') as f:
            f.write(json.dumps(achievements, cls=DataclassJSONEncoder))
        return achievements

    async def _get_sc2_achievements(self):
        account_data = await self.backend_client.get_sc2_player_data(self.authentication_client.user_details["id"])

        # TODO what if more sc2 accounts?
        assert len(account_data) == 1
        account_data = account_data[0]

        profile_data = await self.backend_client.get_sc2_profile_data(
                                                         account_data["regionId"], account_data["realmId"],
                                                         account_data["profileId"]
                                                         )

        sc2_achievement_data = [
            Achievement(achievement_id=achievement["achievementId"], unlock_time=achievement["completionDate"])
            for achievement in profile_data["earnedAchievements"]
            if achievement["isComplete"]
        ]

        with open('sc2.json', 'w') as f:
            f.write(json.dumps(sc2_achievement_data, cls=DataclassJSONEncoder))
        return sc2_achievement_data

    # async def get_unlocked_achievements(self, game_id):
    #     if not self.website_client.is_authenticated():
    #         raise AuthenticationRequired()
    #     try:
    #         if game_id == "21298":
    #             return await self._get_sc2_achievements()
    #         elif game_id == "5730135":
    #             return await self._get_wow_achievements()
    #         else:
    #             return []
    #     except requests.Timeout:
    #         raise BackendTimeout()
    #     except requests.ConnectionError:
    #         raise NetworkError()
    #     except Exception as e:
    #         log.exception(str(e))
    #         return []

    async def launch_platform_client(self):
        if self.local_client.is_running():
            log.info("Launch platform client called but client is already running")
            return
        self.local_client.open_battlenet()
        await self.local_client.prevent_battlenet_from_showing()

    async def shutdown_platform_client(self):
        await self.local_client.shutdown_platform_client()

    async def shutdown(self):
        log.info("Plugin shutdown.")
        await self.authentication_client.shutdown()


def main():
    multiprocessing.freeze_support()
    create_and_run_plugin(BNetPlugin, sys.argv)


if __name__ == "__main__":
    main()
