class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return f"{sum(self._income.values())}"


employee = Position("Slava", "Kuncevic", "Middle MonkeyCode Dev", 100.1, 0.00001)
print(employee.get_full_name())
print(employee.position)
print(employee.get_total_income())
