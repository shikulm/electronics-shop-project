import pytest
from src.keyboard import *

@pytest.fixture
def kb():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test__init__(kb):
    assert str(kb) == "Dark Project KD87A"


def test_change_lang(kb):
    kb.change_lang()
    assert str(kb.language) == "RU"

    # Сделали RU -> EN -> RU
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"


def test_language(kb):
    with pytest.raises(AttributeError):
        kb.language = 'CH'

