from definitions import WebsiteAuthData
import pickle
import asyncio

import requests
import requests.cookies
from urllib.parse import urlparse, parse_qs
from functools import partial

from galaxy.api.errors import InvalidCredentials
from galaxy.api.types import Authentication, NextStep

from consts import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, FIREFOX_AGENT
from region_helper import _found_region, guess_region


class AuthenticatedHttpClient(object):
    def __init__(self, plugin):
        self._plugin = plugin
        self.user_details = None
        self._region = None
        self.session = None
        self.creds = None
        self.timeout = 20.0
        self.attempted_to_set_battle_tag = None
        self.auth_data = None

    def is_authenticated(self):
        return self.session is not None

    async def shutdown(self):
        if self.session:
            self.session.close()
            self.session = None

    def process_stored_credentials(self, stored_credentials):
        auth_data = WebsiteAuthData(
            cookie_jar=pickle.loads(bytes.fromhex(stored_credentials['cookie_jar'])),
            access_token=stored_credentials['access_token'],
            region=stored_credentials['region'] if 'region' in stored_credentials else 'eu'
        )

        # set default user_details data from cache
        if 'user_details_cache' in stored_credentials:
            self.user_details = stored_credentials['user_details_cache']
            self.auth_data = auth_data
        return auth_data

    async def get_auth_data_login(self, cookie_jar, credentials):
        code = parse_qs(urlparse(credentials['end_uri']).query)["code"][0]
        loop = asyncio.get_running_loop()

        s = requests.Session()
        url = f"{self.blizzard_oauth_url}/token"
        data = {
            "grant_type": "authorization_code",
            "redirect_uri": REDIRECT_URI,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "code": code
        }
        response = await loop.run_in_executor(None, partial(s.post, url, data=data))
        response.raise_for_status()
        result = response.json()
        access_token = result["access_token"]
        self.auth_data = WebsiteAuthData(cookie_jar=cookie_jar, access_token=access_token, region=self.region)
        return self.auth_data

    # NOTE: use user data to present usertag/name to Galaxy, if this token expires and plugin cannot refresh it
    # use stored usertag/name if token validation fails, this is temporary solution, as we do not need that
    # endpoint for nothing else at this moment
    def validate_auth_status(self, auth_status):
        if 'error' in auth_status:
            if not self.user_details:
                raise InvalidCredentials()
            else:
                return False
        elif not self.user_details:
            raise InvalidCredentials()
        else:
            if not ("authorities" in auth_status and "IS_AUTHENTICATED_FULLY" in auth_status["authorities"]):
                raise InvalidCredentials()
            return True

    def parse_user_details(self):
        if 'id' and 'battletag' in self.user_details:
            return Authentication(self.user_details["id"], self.user_details["battletag"])
        else:
            raise InvalidCredentials()

    def authenticate_using_login(self):
        _URI = f'{self.blizzard_oauth_url}/authorize?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope=wow.profile+sc2.profile'
        auth_params = {
            "window_title": "Login to Battle.net",
            "window_width": 540,
            "window_height": 700,
            "start_uri": _URI,
            "end_uri_regex": r"(.*logout&app=oauth.*)|(^http://friendsofgalaxy\.com.*)"
        }
        return NextStep("web_session", auth_params)

    def parse_auth_after_setting_battletag(self):
        self.creds["user_details_cache"] = self.user_details
        try:
            battletag = self.user_details["battletag"]
        except KeyError:
            raise InvalidCredentials()
        self._plugin.store_credentials(self.creds)
        return Authentication(self.user_details["id"], battletag)

    def parse_cookies(self, cookies):
        if not self.region:
            self.region = _found_region(cookies)
        new_cookies = {cookie["name"]: cookie["value"] for cookie in cookies}
        return requests.cookies.cookiejar_from_dict(new_cookies)

    def set_credentials(self):
        self.creds = {"cookie_jar": pickle.dumps(self.auth_data.cookie_jar).hex(), "access_token": self.auth_data.access_token,
                      "user_details_cache": self.user_details, "region": self.auth_data.region}

    def parse_battletag(self):
        try:
            battletag = self.user_details["battletag"]
        except KeyError:
            st_parameter = requests.utils.dict_from_cookiejar(
                self.auth_data.cookie_jar)["BA-tassadar"]
            start_uri = f'{self.blizzard_battlenet_login_url}/flow/' \
                            f'app.app?step=login&ST={st_parameter}&app=app&cr=true'
            auth_params = {
                "window_title": "Login to Battle.net",
                "window_width": 540,
                "window_height": 700,
                "start_uri": start_uri,
                "end_uri_regex": r".*accountName.*"
            }
            self.attempted_to_set_battle_tag = True
            return NextStep("web_session", auth_params)

        self._plugin.store_credentials(self.creds)
        return Authentication(self.user_details["id"], battletag)

    async def create_session(self):
        self.session = requests.Session()
        self.session.cookies = self.auth_data.cookie_jar
        self.region = self.auth_data.region
        self.session.max_redirects = 300
        self.session.headers = {
            "Authorization": f"Bearer {self.auth_data.access_token}",
            "User-Agent": FIREFOX_AGENT
        }

    def refresh_credentials(self):
        creds = {
            "cookie_jar": pickle.dumps(self.session.cookies).hex(),
            "access_token": self.auth_data.access_token,
            "region": self.auth_data.region,
            "user_details_cache": self.user_details
        }
        self._plugin.store_credentials(creds)

    @property
    def region(self):
        if self._region is None:
            self._region = guess_region(self._plugin.local_client)
        return self._region

    @region.setter
    def region(self, value):
        self._region = value

    @property
    def blizzard_accounts_url(self):
        if self.region == 'cn':
            return "https://account.blizzardgames.cn"
        else:
            return f"https://{self.region}.account.blizzard.com"

    @property
    def blizzard_oauth_url(self):
        if self.region == 'cn':
            return "https://www.battlenet.com.cn/oauth"
        else:
            return f"https://{self.region}.battle.net/oauth"

    @property
    def blizzard_api_url(self):
        if self.region == 'cn':
            return "https://gateway.battlenet.com.cn"
        else:
            return f"https://{self.region}.api.blizzard.com"

    @property
    def blizzard_battlenet_download_url(self):
        if self.region == 'cn':
            return "https://cn.blizzard.com/zh-cn/apps/battle.net/desktop"
        else:
            return "https://www.blizzard.com/apps/battle.net/desktop"

    @property
    def blizzard_battlenet_login_url(self):
        if self.region == 'cn':
            return 'https://www.battlenet.com.cn/login/zh'
        else:
            return f'https://{self.region}.battle.net/login/en'
