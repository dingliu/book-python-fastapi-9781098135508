import os
import pytest
from model.explorer import Explorer
from error import MissingError, DuplicateError


# set this before data imports below for data init
os.environ["CRYPTID_SQLITE_DB"] = ":memory:"
from data import explorer


@pytest.fixture
def sample() -> Explorer:
    return Explorer(
        name="Claude Hande", country="FR", description="Scarce during full moons"
    )


@pytest.fixture
def another() -> Explorer:
    return Explorer(name="Noah Weiser", country="DE", description="Myopic machete man")


def test_create(sample):
    resp = explorer.create(sample)
    assert resp == sample


def test_create_duplicate(sample):
    with pytest.raises(DuplicateError):
        explorer.create(sample)


def test_get_one(sample):
    resp = explorer.get_one(sample.name)
    assert resp == sample


def test_get_one_missing(another):
    with pytest.raises(MissingError):
        explorer.get_one(another.name)


def test_modify(sample):
    sample.description = "modified description"
    resp = explorer.modify(sample)
    assert resp == sample


def test_modify_missing(another):
    with pytest.raises(MissingError):
        explorer.modify(another)


def test_delete(sample):
    resp = explorer.delete(sample.name)
    assert resp == True


def test_delete_missing(another):
    with pytest.raises(MissingError):
        explorer.delete(another.name)
