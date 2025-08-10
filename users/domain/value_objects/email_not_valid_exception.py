class EmailNotValidException(Exception):
    """Exception raised when an email is not valid."""
    def __init__(self, message: str = "Email is not valid"):
        super().__init__(message)