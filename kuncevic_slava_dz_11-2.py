class Zeroing(Exception):
    text = "На ноль делить нельзя!"

    def __str__(self):
        return self.text


class Number(int):

    def __init__(self, number):
        self.number = number

    def __truediv__(self, other):
        if other == 0:
            raise Zeroing

        return self.number / other


num_1 = Number(1)
num_2 = Number(0)
x = num_1 / num_2
print(x)
