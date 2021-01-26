import logging as log

from definitions import ProductDbInfo, ConfigGameInfo
from product_db_pb2 import ProductDb


class ConfigParser(object):
    def __init__(self, config_data):
        self._blizz_code_lang = ''
        self._region = ''
        self.games = []

        if config_data is None:
            return
        try:
            raw_games = self.parse(config_data)
            self.games = self.decode(raw_games)
        except Exception:
            log.warning('Failed to read Battle.net config, using default values.')

    @property
    def locale_language(self):
        return self._blizz_code_lang

    @property
    def region(self):
        return self._region

    def parse(self, content):
        for key in content.keys():
            if 'Client' in content[key]:
                self._blizz_code_lang = content[key]['Client']['Language']

            if 'Services' in content[key]:
                self._region = content[key]['Services']['LastLoginRegion']
        if 'Games' in content:
            return content['Games']
        else:
            return {}

    def decode(self, games_dict):
        games = []
        for uid, properties in games_dict.items():
            if uid == 'battle_net':
                continue
            uninstall_tag = properties.get('ServerUid', None)
            last_played = properties.get('LastPlayed', None)
            games.append(ConfigGameInfo(uid, uninstall_tag, last_played))
        return games


class DatabaseParser(object):
    NOT_GAMES = ('bna', 'agent')

    def __init__(self, data):
        self.data = data
        self.products = {}
        self._region = ''

        self.parse()

    @property
    def region(self):
        return self._region

    @property
    def battlenet_present(self):
        return 'bna' in self.products

    @property
    def games(self):
        if self.products:
            return [v for k, v in self.products.items() if k not in self.NOT_GAMES]
        return []

    def parse(self):
        self.products = {}
        database = ProductDb()
        database.ParseFromString(self.data)

        for product_install in database.product_installs:
            # process region
            if product_install.product_code in ['agent',
                                                'bna'] and not self.region:
                self._region = product_install.settings.play_region

            ngdp_code = product_install.product_code
            uninstall_tag = product_install.uid
            install_path = product_install.settings.install_path
            playable = product_install.cached_product_state.base_product_state.playable
            version = product_install.cached_product_state.base_product_state.current_version_str
            installed = product_install.cached_product_state.base_product_state.installed
            total_to_download = product_install.cached_product_state.update_progress.total_to_download

            self.products[ngdp_code] = ProductDbInfo(uninstall_tag, ngdp_code, install_path, version, playable, installed, total_to_download)

