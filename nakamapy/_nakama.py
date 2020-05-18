import base64
from uuid import getnode

import aiohttp

from nakamapy.services.account import NakamaAccount
from nakamapy.services.error import NakamaError
from nakamapy.services.logger import Logger
from nakamapy.services.session import NakamaSession
from nakamapy.services.socket import NakamaSocket

logger = Logger()


class Nakama:
    def __init__(self, server_key: str, server_ip: str, server_port: int, server_type: str = "http",
                 server_version: str = "v2"):
        self._server_key = server_key
        self._server_ip = server_ip
        self._server_port = server_port
        self._server_type = server_type
        self._server_version = server_version

    @property
    def server_key(self) -> str:
        return self._server_key

    @property
    def server_key_b64(self) -> str:
        return base64.b64encode(f'{self._server_key}:'.encode()).decode()

    @property
    def server_ip(self) -> str:
        return self._server_ip

    @property
    def server_port(self) -> int:
        return self._server_port

    @property
    def server_type(self) -> str:
        return self._server_type

    @property
    def server_version(self) -> str:
        return self._server_version

    @property
    def base_url(self) -> str:
        return f'{self.server_type}://{self.server_ip}:{self.server_port}/{self.server_version}'

    @property
    def base_header(self) -> dict:
        return {'Authorization': f'Basic {self.server_key_b64}'}

    # Auth Section

    # Auth Device
    async def authenticate_device(self, username: str, create_user: bool = True) -> NakamaSession:
        _data = {'id': str(getnode())}
        _params = {'create': str(create_user).lower(), 'username': username}
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    f'{self.base_url}/account/authenticate/device', params=_params,
                    json=_data, headers=self.base_header) as resp:
                r = await resp.json()
                if resp.status != 200:
                    raise NakamaError(http_code=resp.status, error_name=r['error'], grpc_code=r['code'],
                                      message=r['message'])
                return NakamaSession(token=r['token'])

    # Auth Email
    async def authenticate_email(self, email: str, password: str, username: str,
                                 create_user: bool = True) -> NakamaSession:
        _data = {'email': email, 'password': password}
        _params = {'create': str(create_user).lower(), 'username': username}
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    f'{self.base_url}/account/authenticate/email', params=_params,
                    json=_data, headers=self.base_header) as resp:
                r = await resp.json()
                if resp.status != 200:
                    raise NakamaError(http_code=resp.status, error_name=r['error'], grpc_code=r['code'],
                                      message=r['message'])
                return NakamaSession(token=r['token'])

    # Auth Facebook
    async def authenticate_facebook(self, token: str, username: str, create_user: bool = True,
                                    import_friends: bool = True) -> NakamaSession:
        _data = {'token': token}
        _params = {'create': str(create_user).lower(), 'username': username, 'import': str(import_friends).lower()}
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    f'{self.base_url}/account/authenticate/facebook', params=_params,
                    json=_data, headers=self.base_header) as resp:
                r = await resp.json()
                if resp.status != 200:
                    raise NakamaError(http_code=resp.status, error_name=r['error'], grpc_code=r['code'],
                                      message=r['message'])
                return NakamaSession(token=r['token'])

    # Auth Google
    async def authenticate_google(self, token: str, username: str, create_user: bool = True) -> NakamaSession:
        _data = {'token': token}
        _params = {'create': str(create_user).lower(), 'username': username}
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    f'{self.base_url}/account/authenticate/google', params=_params,
                    json=_data, headers=self.base_header) as resp:
                r = await resp.json()
                if resp.status != 200:
                    raise NakamaError(http_code=resp.status, error_name=r['error'], grpc_code=r['code'],
                                      message=r['message'])
                return NakamaSession(token=r['token'])

    # Auth Game Center
    async def authenticate_game_center(self, player_id: str, bundle_id: str, salt: str, signature: str,
                                       public_key_url: str, username: str, create_user: bool = True,
                                       timestamp_seconds: int = 0) -> NakamaSession:
        _data = {'player_id': player_id, 'bundle_id': bundle_id, 'timestamp_seconds': timestamp_seconds, 'salt': salt,
                 'signature': signature, 'public_key_url': public_key_url}
        _params = {'create': str(create_user).lower(), 'username': username}
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    f'{self.base_url}/account/authenticate/gamecenter', params=_params,
                    json=_data, headers=self.base_header) as resp:
                r = await resp.json()
                if resp.status != 200:
                    raise NakamaError(http_code=resp.status, error_name=r['error'], grpc_code=r['code'],
                                      message=r['message'])
                return NakamaSession(token=r['token'])

    # Auth Steam -> You need to configure the Server to support SteamAuth
    async def authenticate_steam(self, token: str, username: str, create_user: bool = True) -> NakamaSession:
        _data = {'token': token}
        _params = {'create': str(create_user).lower(), 'username': username}
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    f'{self.base_url}/account/authenticate/steam', params=_params,
                    json=_data, headers=self.base_header) as resp:
                r = await resp.json()
                if resp.status != 200:
                    raise NakamaError(http_code=resp.status, error_name=r['error'], grpc_code=r['code'],
                                      message=r['message'])
                return NakamaSession(token=r['token'])

    # Auth Custom
    async def authenticate_custom(self, custom_id: str, username: str, create_user: bool = True) -> NakamaSession:
        _data = {'id': custom_id}
        _params = {'create': str(create_user).lower(), 'username': username}
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    f'{self.base_url}/account/authenticate/custom', params=_params,
                    json=_data, headers=self.base_header) as resp:
                r = await resp.json()
                if resp.status != 200:
                    raise NakamaError(http_code=resp.status, error_name=r['error'], grpc_code=r['code'],
                                      message=r['message'])
                return NakamaSession(token=r['token'])

    # Create Socket
    def create_socket(self) -> NakamaSocket:
        return NakamaSocket(socket_ip=self.server_ip, socket_port=self.server_port)

    # TODO: Implement un-linking of accounts
    async def link_login(self):
        pass

    async def fetch_account(self, session_token: NakamaSession) -> NakamaAccount:
        headers = {'Authorization': f'Bearer {session_token}'}
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f'{self.base_url}/account', headers=headers) as resp:
                r = await resp.json()
                if resp.status != 200:
                    raise NakamaError(http_code=resp.status, error_name=r['error'], grpc_code=r['code'],
                                      message=r['message'])
                return NakamaAccount(r)
