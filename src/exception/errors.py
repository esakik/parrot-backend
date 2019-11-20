class BaseError(Exception):
    def __init__(self, message: str):
        self.__message: str = message
        super().__init__(message)

    @property
    def message(self):
        return self.__message


class ValidationError(BaseError):
    def __init__(self, cause: str):
        super().__init__(message=f"The request is invalid. {cause}")


class UnexpectedError(BaseError):
    def __init__(self, state: str):
        super().__init__(
            message=f"Unexpected error occurred. {state} Please contact your administrator for assistance."
        )
