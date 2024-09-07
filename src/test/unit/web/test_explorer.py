import pytest
from fastapi import HTTPException, status
from model.explorer import Explorer
from test.utils import assert_missing, assert_duplicate

# use double/fake for testing
import os
os.environ["CRYPTID_UNIT_TEST"] = "yes"
from web import explorer


@pytest.fixture
def sample() -> Explorer:
    return Explorer(name="Indiana Jones",
                    country="US",
                    description="Starred Harrison Ford")


@pytest.fixture
def fakes() -> list[Explorer]:
    return explorer.get_all()


# ===========
# tests
# ===========
def test_create(sample):
    assert explorer.create(sample) == sample


def test_create_duplicate(fakes):
    with pytest.raises(HTTPException) as e:
        explorer.create(fakes[0])
        assert_duplicate(e.value)


def test_get_one(fakes):
    assert explorer.get_one(fakes[0].name) == fakes[0]


def test_get_one_missing(sample):
    with pytest.raises(HTTPException) as e:
        explorer.get_one(sample.name)
        assert_missing(e.value)


def test_modify(fakes):
    assert explorer.modify(fakes[0]) == fakes[0]


def test_modify_missing(sample):
    with pytest.raises(HTTPException) as e:
        explorer.modify(sample)
        assert_missing(e.value)


def test_replace(fakes):
    assert explorer.replace(fakes[0]) == fakes[0]


def test_replace_missing(sample):
    with pytest.raises(HTTPException) as e:
        explorer.replace(sample)
        assert_missing(e.value)


def test_delete(fakes):
    assert explorer.delete(fakes[0].name) == True


def test_delete_missing(sample):
    with pytest.raises(HTTPException) as e:
        explorer.delete(sample.name)
        assert_missing(e.value)
