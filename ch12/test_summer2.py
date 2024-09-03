from unittest.mock import patch
from ch12 import mod1, mod2


def test_summer_a():
    with patch("ch12.mod1.preamble", return_value=""):
        assert mod2.summer(5, 6) == "11"


def test_summer_b():
    with patch("ch12.mod1.preamble") as mock_preamble:
        mock_preamble.return_value = ""
        assert mod2.summer(5, 6) == "11"


@patch("ch12.mod1.preamble", return_value="")
def test_summer_c(mock_preamble):
    assert mod2.summer(5, 6) == "11"


@patch("ch12.mod1.preamble")
def test_summer_d(mock_preamble):
    mock_preamble.return_value = ""
    assert mod2.summer(5, 6) == "11"
