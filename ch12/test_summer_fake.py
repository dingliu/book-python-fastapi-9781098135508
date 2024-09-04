import os

# double fake for testing
os.environ["UNIT_TEST"] = "yes"
from ch12.mod2 import summer


def test_summer():
    assert summer(5, 6) == "11"
