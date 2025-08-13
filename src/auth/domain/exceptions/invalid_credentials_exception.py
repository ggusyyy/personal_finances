class InvalidCredentialsException(Exception):
    def __init__(self, message: str ="Invalid credentials provided."):
        super().__init__(self.message)
        
        self.message = message