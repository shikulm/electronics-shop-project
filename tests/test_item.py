"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import *


@pytest.mark.parametrize("name, price, quantity, result",
                         [
                             ("Смартфон", 10000, 20, ["Смартфон", 10000, 20]),
                             ("Ноутбук", 20000, 5, ["Ноутбук", 20000, 5])
                         ])
def test_init(name, price, quantity, result):
    item1 = Item(name, price, quantity)
    assert [item1.name, item1.price, item1.quantity] == result


def test_init_all():
    ln = len(Item.all)
    item1 = Item("Смартфон", 10000, 20)
    assert len(Item.all) == ln + 1

def test_init_TypeErrorname():
    ln = len(Item.all)
    with pytest.raises(TypeError):
        Item(25, 10000, 20)
    assert len(Item.all) == ln

def test_init_TypeErrorprice():
    ln = len(Item.all)
    with pytest.raises(TypeError):
        Item("Смартфон", "das", 20)
    assert len(Item.all) == ln


def test_init_TypeErrorquantity():
    ln = len(Item.all)
    with pytest.raises(TypeError):
        Item("Смартфон", 10000, 20.4)
    assert len(Item.all) == ln

@pytest.mark.parametrize("name, price, quantity, total_price",
                         [
                             ("Смартфон", 10000, 20, 200000),
                             ("Ноутбук", 20000, 5, 100000)
                         ])
def test_calculate_total_price(name, price, quantity, total_price):
    item1 = Item(name, price, quantity)
    assert item1.calculate_total_price() == total_price