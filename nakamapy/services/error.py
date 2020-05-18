from nakamapy.services.logger import Logger

logger = Logger()


class NakamaError(Exception):
    def __init__(self, http_code: int, error_name: str, grpc_code: int, message: str):
        # Build default message
        error_message = \
            f'NakamaServer raised an error | HTTP_CODE: {http_code} | ' \
            f'ERROR_NAME: {error_name} | GRPC_CODE: {grpc_code} | MESSAGE: {message}'
        logger.error(error_message)
        super().__init__(error_message)
        self._http_code: int = http_code
        self._error_name: str = error_name
        self._grpc_code: int = grpc_code
        self._message: str = message

    @property
    def http_code(self) -> int:
        return self._http_code

    @property
    def error_name(self) -> str:
        return self._error_name

    @property
    def grpc_code(self) -> int:
        return self._grpc_code

    @property
    def message(self) -> str:
        return self._message
