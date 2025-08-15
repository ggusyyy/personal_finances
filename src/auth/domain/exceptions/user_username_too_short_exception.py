class UserUsernameTooShortException(Exception):
    def __init__(self, message: str = "Username is too short") -> None:
        super().__init__(message)