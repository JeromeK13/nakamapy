import base64
from uuid import getnode

import aiohttp

from nakamapy.services.error import NakamaError
from nakamapy.services.logger import Logger

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
        return {
            'Authorization': f'Basic {self.server_key_b64}'
        }

    async def authenticate_device(self, username: str, create_user: bool = True) -> dict:
        _data = {'id': str(getnode())}
        _params = {'create': str(create_user).lower(), 'username': username}
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    f'{self.base_url}/account/authenticate/device', params=_params,
                    json=_data, headers=self.base_header) as resp:
                if resp.status != 200:
                    r = await resp.json()
                    raise NakamaError(http_code=resp.status, error_name=r['error'], grpc_code=r['code'],
                                      message=r['message'])
                return await resp.json()

    async def authenticate_email(self, email: str, password: str, username: str, create_user: bool = True) -> dict:
        _data = {'email': email, 'password': password}
        _params = {'create': str(create_user).lower(), 'username': username}
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    f'{self.base_url}/account/authenticate/email', params=_params,
                    json=_data, headers=self.base_header) as resp:
                if resp.status != 200:
                    r = await resp.json()
                    raise NakamaError(http_code=resp.status, error_name=r['error'], grpc_code=r['code'],
                                      message=r['message'])
                return await resp.json()
