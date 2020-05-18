import jwt


class NakamaSession:
    def __init__(self, token: str):
        self._token = token

    @property
    def token(self) -> str:
        return self._token

    @property
    def user_id(self) -> str:
        return jwt.decode(self.token, verify=False)['uid']

    @property
    def username(self) -> str:
        return jwt.decode(self.token, verify=False)['usn']

    @property
    def expire_date(self) -> int:
        return jwt.decode(self.token, verify=False)['exp']

    @property
    def is_expired(self) -> bool:
        try:
            jwt.decode(self.token, verify=False)
            return False
        except jwt.ExpiredSignatureError:
            return True
