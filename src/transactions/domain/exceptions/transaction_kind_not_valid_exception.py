class TransactionKindIsNotValidException(Exception):
    def __init__(self, message: str = "The kind of the transaction is not valid"):
        super().__init__(message)
        self.message = message