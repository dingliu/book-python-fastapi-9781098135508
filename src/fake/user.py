from model.user import User
from error import MissingError, DuplicateError


## No hashed password checking in this module
fakes = [
    User(name="fkiwsjobo", hash="abals"),
    User(name="alswsl", hash="slawo"),
]


def find(name: str) -> User | None:
    for f in fakes:
        if f.name == name:
            return f
    else:
        return None


def check_missing(name: str):
    if not find(name):
        raise MissingError(msg=f"Missing user {name}.")


def check_duplicate(name: str):
    if find(name):
        raise DuplicateError(msg=f"Duplicated user {name}.")


def get_all() -> list[User]:
    return fakes


def get_one(name: str) -> User:
    check_missing(name)
    return find(name)


def create(user: User) -> User:
    check_duplicate(user.name)
    return user


def modify(name: str, user: User) -> User:
    check_missing(name)
    return user


def delete(name: str) -> bool:
    check_missing(name)
    return True
