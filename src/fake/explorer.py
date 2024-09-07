from model.explorer import Explorer
from error import MissingError, DuplicateError


_explorers = [
    Explorer(name="Claude Hande", country="FR", description="Scarce during full moons"),
    Explorer(name="Noah Weiser", country="DE", description="Myopic machete man"),
]


def check_missing(name: str, explorers: list[Explorer]):
    if name not in [explorer.name for explorer in explorers]:
        raise MissingError(msg=f"Explorer {name} not found.")


def check_duplicate(name: str, explorers: list[Explorer]):
    if name in [explorer.name for explorer in explorers]:
        raise DuplicateError(msg=f"Explorer {name} already exists.")


def get_all() -> list[Explorer]:
    """return all explorers"""
    return _explorers


def get_one(name: str) -> Explorer:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    raise MissingError(msg=f"Explorer {name} not found.")


def create(explorer: Explorer) -> Explorer:
    """Add an explorer"""
    check_duplicate(explorer.name, _explorers)
    return explorer


def modify(explorer: Explorer) -> Explorer:
    """Partially modify an explorer"""
    check_missing(explorer.name, _explorers)
    return explorer


def replace(explorer: Explorer) -> Explorer:
    """Completely replace an explorer"""
    check_missing(explorer.name, _explorers)
    return explorer


def delete(name: str) -> bool:
    """Delete an explorer; return None if existed"""
    check_missing(name, _explorers)
    return True
