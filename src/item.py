import csv
import os

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
        super().__init__()


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        else:
            raise ValueError("Складывать можно только с экземпляром класса Item или его наследником!")

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
            raise ValueError("Длина наименования товара превышает 10 символов")


    @classmethod
    def instantiate_from_csv(cls, csv_name: str = "items.csv"):
        """класс-метод, инициализирующий экземпляры класса Item данными из файла csv_name"""

        path_file = os.path.dirname(os.path.abspath(__file__))
        full_file_name = os.path.join(path_file, csv_name)

        Item.all = []
        try:
            with open(full_file_name, "r", encoding="ansi") as fl:
                input_items = csv.DictReader(fl)
                itm = []
                for item in input_items:
                    # print(item)
                    itm.append(cls(name=item['name'], price=float(item['price']), quantity=int(item['quantity'])))

            return itm
        except FileNotFoundError:
            raise FileNotFoundError(f"Отсутствует файл {csv_name}")

    @staticmethod
    def string_to_number(str_digit: str) -> None:
        """Преобразовывает строку в число"""
        try:
            return int(float(str_digit))
        except:
            raise TypeError

