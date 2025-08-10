class UserNotFoundException(Exception):
    def __init__(self, message: str = "User not found") -> None:
        super().__init__(message)