class ExpiredTokenException(Exception):
    def __init__(self, message: str = "The provided token has expired."):
        super().__init__(message)