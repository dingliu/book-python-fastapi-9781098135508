import os
import pytest
from model.creature import Creature
from error import MissingError, DuplicateError

os.environ["CRYPTID_SQLITE_DB"] = ":memory:"
from service import creature as code


@pytest.fixture
def sample() -> Creature:
    return Creature(
        name="Yeti",
        aka="Abominable Snowman",
        country="CN",
        area="Himalayas",
        description="Hirsute Himalayan",
    )


def test_create(sample):
    resp = code.create(sample)
    assert resp == sample


def test_get_exists(sample):
    resp = code.get_one(sample.name)
    assert resp == sample


def test_get_missing():
    with pytest.raises(MissingError):
        resp = code.get_one("BoxTurtle")
