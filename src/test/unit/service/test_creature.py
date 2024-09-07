import pytest
from model.creature import Creature
from error import MissingError, DuplicateError

# use double/fake for testing
import os
os.environ["CRYPTID_UNIT_TEST"] = "yes"

from service import creature


@pytest.fixture
def fakes() -> list[Creature]:
    return creature.get_all()


@pytest.fixture
def sample() -> Creature:
    return Creature(name="Dragon",
                    country="*",
                    area="*",
                    description="Wings! Fire! Aieeee!",
                    aka="Long")


def test_create(sample):
    resp = creature.create(sample)
    assert resp == sample


def test_create_duplicate(fakes):
    with pytest.raises(DuplicateError):
        creature.create(fakes[0])


def test_get_all(fakes):
    assert creature.get_all() == fakes


def test_get_one(fakes):
    assert creature.get_one(fakes[0].name) == fakes[0]


def test_get_one_missing(sample):
    with pytest.raises(MissingError):
        creature.get_one(sample.name)
