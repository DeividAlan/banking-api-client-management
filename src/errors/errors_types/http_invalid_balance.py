class HttpInvalidBalanceError(Exception):
    def __init__(self, message: str = "Insufficient balance to complete the transaction.") -> None:
        super().__init__(message)
        self.status_code = 400
        self.name = "InvalidBalance"
        self.message = message
