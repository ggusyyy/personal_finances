class AmountIsLessThanZeroException(Exception):
    def __init__(self, message: str = "Amount must be greater than or equal to zero."):
        super().__init__(message)
        self.message = message