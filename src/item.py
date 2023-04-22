import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        # Проверка типов данных параметров
        if not (isinstance(name, str) and (isinstance(price, float) or isinstance(price, int)) and isinstance(quantity, int)):
            raise TypeError
        else:
            self.__name = name
            self.price = price
            self.quantity = quantity
            Item.all.append(self)


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception("Длина наименования товара превышает 10 символов")


    @classmethod
    def instantiate_from_csv(cls, csv_name: str = "items.csv"):
        """класс-метод, инициализирующий экземпляры класса Item данными из файла csv_name"""

        with open(csv_name, "r", encoding="ansi") as fl:
            input_items = csv.DictReader(fl)
            itm = []
            for item in input_items:
                # print(item)
                itm.append(cls(name=item['name'], price=float(item['price']), quantity=int(item['quantity'])))

        return itm


# item1 = Item("Смартфон", 10000, 20)
# print(Item.instantiate_from_csv())
# print(item1.calculate_total_price())