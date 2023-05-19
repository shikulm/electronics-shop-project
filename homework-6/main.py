from src.item import Item

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv("item_with_error.csv")
    # FileNotFoundError: Отсутствует файл item_with_error.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv()
    # InstantiateCSVError: Файл item_with_error.csv поврежден
