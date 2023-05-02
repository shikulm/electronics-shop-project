import pytest
from src.phone import Phone
from src.item import Item

@pytest.fixture()
def phone1():
    return Phone("iPhone 14", 120000, 5, 2)


@pytest.fixture()
def item1():
    return Item("Смартфон", 10000, 20)


def test__init__(phone1):
    assert phone1.name == "iPhone 14"
    assert phone1.price == 120000
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2


def test_number_of_sim_setter(phone1):
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0
        phone2 = Phone("iPhone 14", 120000, 5, 2)


def test__str__(phone1):
    assert str(phone1) == 'iPhone 14'



