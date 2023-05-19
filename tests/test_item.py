"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import *
import os


@pytest.mark.parametrize("name, price, quantity, result",
                         [
                             ("Смартфон", 10000, 20, ["Смартфон", 10000, 20]),
                             ("Ноутбук", 20000, 5, ["Ноутбук", 20000, 5])
                         ])
def test__init__(name, price, quantity, result):
    item1 = Item(name, price, quantity)
    assert [item1.name, item1.price, item1.quantity] == result

@pytest.mark.parametrize("item, result",
                         [
                             (Item("Смартфон", 10000, 20), "Item('Смартфон', 10000, 20)"),
                             (Item("Ноутбук", 20000, 5), "Item('Ноутбук', 20000, 5)")
                         ])
def test__repr__(item, result):
    assert item.__repr__() == result

@pytest.mark.parametrize("item, result",
                         [
                             (Item("Смартфон", 10000, 20), "Смартфон"),
                             (Item("Ноутбук", 20000, 5), "Ноутбук")
                         ])
def test__str__(item, result):
    assert str(item) == result

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


def test__add__valuerror():
    with pytest.raises(ValueError):
        res = Item("Смартфон", 10000, 20) + 25


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


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0
    assert item2.price == 20000

def test_getter_name():
    item = Item('Телефон', 10000, 5)
    assert item.name == 'Телефон'

def test_setter_name():
    item = Item('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    with pytest.raises(ValueError):
        item.name = 'СуперСмартфон'


def test_instantiate_from_csv():
    # Item.instantiate_from_csv(os.path.join("src", "items.csv"))  # создание объектов из данных файла
    itms = Item.instantiate_from_csv()  # создание объектов из данных файла
    assert len(itms) == 5  # в файле 5 записей с данными по товарам
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам

    item1 = itms[0]
    assert item1.name == 'Смартфон'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_instantiate_from_csv_FileNotFoundError():
    with pytest.raises(FileNotFoundError) as err:
        Item.instantiate_from_csv("_item.csv")
        assert err.message == "Файл item_with_error.csv поврежден"


def test_instantiate_from_csv_InstantiateCSVError():
    with pytest.raises(FileNotFoundError) as err:
        Item.instantiate_from_csv("item_with_error.csv")
        assert err.message == "InstantiateCSVError: Файл item_with_error.csv поврежден"


def test_string_to_number_TypeError():
    with pytest.raises(TypeError):
        Item.string_to_number('dd') == 5
        Item.string_to_number(23) == 5









