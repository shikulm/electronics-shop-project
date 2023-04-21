class item():
    """Класс с описанием данных по товарам в магазине"""

    def __init__(self, name: str, price: float, count: int):
        self.name = name
        self.price = price
        self.count = count
