class UserLinkFormat:
    @staticmethod
    def reformat(user_link: str, *args: list) -> str:
        return user_link.format(*args)