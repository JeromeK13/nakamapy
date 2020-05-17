import base64

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
    def server_key(self):
        return self._server_key

    @property
    def server_key_b64(self):
        return base64.b64encode(f'{self._server_key}:'.encode()).decode()

    @property
    def server_ip(self):
        return self._server_ip

    @property
    def server_port(self):
        return self._server_port

    @property
    def server_type(self):
        return self._server_type

    @property
    def server_version(self):
        return self._server_version

    @property
    def base_url(self):
        return f'{self.server_type}://{self.server_ip}:{self.server_port}/{self.server_version}'

    async def authenticate_device(self):
        pass

    async def authenticate_email(self, email: str, password: str):
        return self.server_key_b64
