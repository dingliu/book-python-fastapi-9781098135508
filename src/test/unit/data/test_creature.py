import os
import pytest
from model.creature import Creature
from error import MissingError, DuplicateError


# set this before data imports below for data.init
os.environ["CRYPTID_SQLITE_DB"] = ":memory:"
from data import creature


@pytest.fixture
def sample() -> Creature:
    return Creature(
        name="Yeti",
        country="CN",
        area="Himalayas",
        description="harmless Himalayan",
        aka="Abominable Snowman",
    )


@pytest.fixture
def thing() -> Creature:
    return Creature(
        name="BoxTurtle",
        country="RU",
        area="Northern Asia",
        description="For testing",
        aka="test creature",
    )


def test_create(sample):
    resp = creature.create(sample)
    assert resp == sample


def test_create_duplicate(sample):
    with pytest.raises(DuplicateError):
        creature.create(sample)


def test_get_one(sample):
    resp = creature.get_one(sample.name)
    assert resp == sample


def test_get_one_missing():
    with pytest.raises(MissingError):
        creature.get_one("BoxTurtle")


def test_modify(sample):
    sample.area = "Atlantis"
    resp = creature.modify(sample)
    assert resp == sample


def test_modify_missing(thing):
    with pytest.raises(MissingError):
        creature.modify(thing)


def test_delete(sample):
    resp = creature.delete(sample.name)
    assert resp == True


def test_delete_missing(thing):
    with pytest.raises(MissingError):
        creature.delete(thing.name)
