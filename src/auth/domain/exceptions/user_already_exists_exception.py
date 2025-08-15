class UserAlreadyExistsException(Exception):
    def __init__(self, message: str = "User Already Exists") -> None:
        super().__init__(message)