class TransactionDataIsNotValidException(Exception):
    def __init__(self, message: str = "The data of the transaction is not valid"):
        super().__init__(message)
        self.message = message