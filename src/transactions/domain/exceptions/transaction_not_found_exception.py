class TransactionNotFoundException(Exception):
    def __init__(self, message: str = "The transactions was not found."):
        super().__init__(message)
        self.message = message