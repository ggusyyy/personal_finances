class InvalidTokenException(Exception):
    def __init__(self, message: str = "Invalid token provided."):
        super().__init__(message)