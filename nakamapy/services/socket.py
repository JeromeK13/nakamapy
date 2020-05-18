import socket


class NakamaSocket:
    def __init__(self, socket_ip: str, socket_port: int):
        self._socket_ip = socket_ip
        self._socket_port = socket_port

    @property
    def socket_ip(self) -> str:
        return self._socket_ip

    @property
    def socket_port(self) -> int:
        return self._socket_port

    async def connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.socket_ip, self.socket_port))