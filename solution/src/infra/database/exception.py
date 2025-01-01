class BaseDBException(Exception):
    def __init__(self, details: str) -> None:
        self.details = details


class DBDoesNotExistException(BaseDBException):
    def __init__(self, details: str):
        self.reason = "Данных не существует."
        self.details = details


class DBUniqueException(BaseDBException):
    def __init__(self, details: str):
        self.reason = "Данные не уникальны."
        self.details = details
