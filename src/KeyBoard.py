from item import Item

class MixinKeyBoard:
    """ Дополнительный функционал по хранению и изменению раскладки клавиатуры """

    # language = "EN"

    def __init__(self, language="EN"):
        self.__language = language

    def change_lang(self):
        self.__language = "RU" if self.__language == "EN" else "EN"

    @property
    def language(self):
        return self.language
