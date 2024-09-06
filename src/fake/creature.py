from model.creature import Creature
from error import MissingError, DuplicateError


# fake data, until we have a real database and sql
_creatures = [
    Creature(
        name="Yeti",
        aka="Abominable Snowman",
        country="CN",
        area="Himalayas",
        description="Hirsute Himalayan",
    ),
    Creature(
        name="Bigfoot",
        description="Yeti's Cousin Eddie",
        country="US",
        area="*",
        aka="Sasquatch",
    ),
]


def check_missing(name: str, creatures: list[Creature]):
    if name not in [creature.name for creature in creatures]:
        raise MissingError(msg=f"Creature {name} not found.")


def check_duplicate(name: str, creatures: list[Creature]):
    if name in [creature.name for creature in creatures]:
        raise DuplicateError(msg=f"Creature {name} already exists.")


def get_all() -> list[Creature]:
    """return all creatures"""
    return _creatures


def get_one(name: str) -> Creature:
    """return one creature"""
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    raise MissingError(msg=f"Creature {name} not found.")


def create(creature: Creature) -> Creature:
    """Add an creature"""
    check_duplicate(creature.name, _creatures)
    return creature


def modify(creature: Creature) -> Creature:
    """partially modify a creature"""
    check_missing(creature.name, _creatures)
    return creature


def replace(creature: Creature) -> Creature:
    """completely replace a creature"""
    check_missing(creature.name, _creatures)
    return creature


def delete(name: str) -> bool:
    """delete a creature; return None if it existed"""
    check_missing(name, _creatures)
    return True
