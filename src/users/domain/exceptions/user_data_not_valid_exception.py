class UserNotValidException(Exception):
    """Exception raised when a user is not valid."""
    def __init__(self, message: str = "User is not valid."):
        super().__init__(message)