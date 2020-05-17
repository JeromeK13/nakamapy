from nakamapy.services.logger import Logger

logger = Logger()


class Nakama:
    def __init__(self, server_key: str, server_ip: str, server_port: int, server_type: str = "http"):
        self.server_key = server_key
        self.server_ip = server_ip
        self.server_port = server_port
        self.server_type = server_type
