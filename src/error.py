class CryptidError(Exception):
    def __init__(self, msg: str) -> None:
        self.msg = msg


class MissingError(CryptidError): ...


class DuplicateError(CryptidError): ...
