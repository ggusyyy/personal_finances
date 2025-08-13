class UserPasswordTooShortException(Exception):
    def __init__(self, message: str = "User password is too short") -> None:
        super().__init__(message)