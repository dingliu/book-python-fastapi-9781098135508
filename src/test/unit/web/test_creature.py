import pytest
from fastapi import HTTPException, status
from model.creature import Creature
from test.utils import assert_duplicate, assert_missing

# use double/fake for testing
import os
os.environ["CRYPTID_UNIT_TEST"] = "yes"
from web import creature


@pytest.fixture
def sample() -> Creature:
    return Creature(name="Dragon",
                    country="*",
                    area="*",
                    description="Wings! Fire! Aieeee!",
                    aka="Long")


@pytest.fixture
def fakes() -> list[Creature]:
    return creature.get_all()


# ==============
# tests
# ==============
def test_create(sample):
    assert creature.create(sample) == sample


def test_create_duplicate(fakes):
    with pytest.raises(HTTPException) as e:
        creature.create(fakes[0])
        assert_duplicate(e.value)


def test_get_one(fakes):
    assert creature.get_one(fakes[0].name) == fakes[0]


def test_get_one_missing(sample):
    with pytest.raises(HTTPException) as e:
        creature.get_one(sample)
        assert_missing(e.value)


def test_modify(fakes):
    assert creature.modify(fakes[0]) == fakes[0]


def test_modify_missing(sample):
    with pytest.raises(HTTPException) as e:
        creature.modify(sample)
        assert_missing(e.value)


def test_replace(fakes):
    assert creature.replace(fakes[0]) == fakes[0]


def test_replace_missing(sample):
    with pytest.raises(HTTPException) as e:
        creature.replace(sample)
        assert_missing(e.value)


def test_delete(fakes):
    assert creature.delete(fakes[0].name) == True


def test_delete_missing(sample):
    with pytest.raises(HTTPException) as e:
        creature.delete(sample.name)
        assert_missing(e.value)
