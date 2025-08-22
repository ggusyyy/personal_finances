class TransactionUserIdIsNotValidException(Exception):
    def __init__(self, message: str = "The user id of the transaction is not valid"):
        super().__init__(message)
        self.message = message