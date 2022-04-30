from abc import ABC, abstractmethod


class Clothes(ABC):
    layout = 0

    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        if isinstance(self.__size, str) or self.__size <= 0:
            raise ValueError("Нет у вас ткани!")
        return self.__size

    @abstractmethod
    def fitting(self):
        pass


class Coat(Clothes):
    def fitting(self):
        __v = self.size
        amount = float(f'{__v / 6.5 + 0.5 :0.2f}')
        Clothes.layout += amount
        return f'{amount} - расход ткани на пальто;'


class Suit(Clothes):

    def fitting(self):
        __h = self.size
        amount = float(f'{__h * 2 + 0.3 :0.2f}')
        Clothes.layout += amount
        return f'{amount} - расход ткани на костюмы;'


sew_coat = Coat(555)
print(sew_coat.fitting())

sew_suit = Suit(444)
print(sew_suit.fitting())

print(Clothes.layout, "- общий расход ткани.")
