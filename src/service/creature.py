from model.creature import Creature

# double/fake for testing
import os
if os.environ.get("CRYPTID_UNIT_TEST", ""):
    import fake.creature as data
else:
    import data.creature as data


def get_all() -> list[Creature]:
    return data.get_all()


def get_one(name: str) -> Creature:
    return data.get_one(name)


def create(creature: Creature) -> Creature:
    return data.create(creature)


def replace(creature: Creature) -> Creature:
    return data.replace(creature)


def modify(creature: Creature) -> Creature:
    return data.modify(creature)


def delete(name: str) -> bool:
    return data.delete(name)
