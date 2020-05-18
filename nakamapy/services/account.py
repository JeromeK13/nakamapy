class NakamaAccount:
    def __init__(self, account_dict: dict):
        for k, v in account_dict.items():
            setattr(self, k, v)
