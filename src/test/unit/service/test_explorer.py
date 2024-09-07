import pytest
from model.explorer import Explorer
from error import MissingError, DuplicateError

# use double/fake for testing
import os
os.environ["CRYPTID_UNIT_TEST"] = "yes"

from service import explorer


@pytest.fixture
def fakes() -> list[Explorer]:
    return explorer.get_all()


@pytest.fixture
def sample() -> Explorer:
    return Explorer(name="Indiana Jones",
                    country="US",
                    description="Starred Harrison Ford")


def test_create(sample):
    assert explorer.create(sample) == sample


def test_create_duplicate(fakes):
    with pytest.raises(DuplicateError):
        explorer.create(fakes[0])


def test_get_all(fakes):
    assert explorer.get_all() == fakes


def test_get_one(fakes):
    assert explorer.get_one(fakes[0].name) == fakes[0]


def test_get_one_missing(sample):
    with pytest.raises(MissingError):
        explorer.get_one(sample)


def test_modify(fakes):
    assert explorer.modify(fakes[0]) == fakes[0]


def test_modify_missing(sample):
    with pytest.raises(MissingError):
        explorer.modify(sample)


def test_delete(fakes):
    assert explorer.delete(fakes[0].name) == True


def test_delete_missing(sample):
    with pytest.raises(MissingError):
        explorer.delete(sample.name)
