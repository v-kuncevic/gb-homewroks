class Cell:
    def __init__(self, cubicles):
        self.cubicles = cubicles

    def make_order(self, line_length):
        result = ['*' * line_length] * (self.cubicles // line_length)
        if self.cubicles % line_length:
            result.append('*' * (self.cubicles % line_length))
        return '\n'.join(result)

    def __str__(self):
        return f"{self.cubicles}"

    def __add__(self, other):
        print("Результат объединения клеток: ")
        return Cell(self.cubicles + other.cubicles)

    def __sub__(self, other):
        print("Результат вычитания клеток: ")
        if self.cubicles < other.cubicles:
            print("Разность количества ячеек двух клеток меньше нуля - невозможно выполнить операцию!")
        else:
            return Cell(self.cubicles - other.cubicles)

    def __mul__(self, other):
        print("Результат объединения клеток: ")
        return Cell(self.cubicles * other.cubicles)

    def __floordiv__(self, other):
        print("Результат целочисленного деления клеток: ")
        return Cell(self.cubicles // other.cubicles)


box = Cell(12)
cubicle = Cell(15)
print(box + cubicle)
print(box - cubicle)
print(box * cubicle)
print(box // cubicle)
print(cubicle.make_order(7))
