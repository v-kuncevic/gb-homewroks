class Car:
    is_police = False

    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.speed = 0

    def go(self, speed=35):
        self.speed = speed
        print(f"{self.color} {self.name} поехал со скоростью {self.speed}.")

    def stop(self):
        self.speed = 0
        print(f"{self.color} {self.name} затормозил.")

    def turn(self, direction):
        if direction == "налево" or direction == "направо":
            print(f"{self.color} {self.name} повернул {direction}.")
        else:
            self.speed = 0
            print(f"и влупился в столб")

    def show_speed(self):
        print(f"Скорость {self.speed} ")


class TownCar(Car):

    def show_speed(self):
        if self.speed >= 61:
            print(f"{self.speed} - превышение скорости")
        else:
            print(f"Скорость {self.speed}.")


class WorkCar(Car):

    def show_speed(self):
        if self.speed >= 41:
            print(f"{self.speed} - превышение скорости")
        else:
            print(f"Скорость {self.speed}.")


class SportCar(Car):
    pass


class PoliceCar(Car):
    is_police = True


auto_1 = PoliceCar("жёлтый", "автозак")
auto_1.go(100)
auto_1.show_speed()
auto_2 = SportCar("грязный", "спорткар")
auto_2.go(150)
auto_2.show_speed()
auto_2.turn("налево")
auto_3 = WorkCar("белый", "мусоровоз")
auto_3.go(10)
auto_3.show_speed()
auto_3.stop()
auto_3.show_speed()
auto_4 = TownCar("зеленоглазое", "такси")
auto_4.go(100)
auto_4.show_speed()
auto_4.stop()
auto_4.show_speed()
auto_5 = SportCar("разноцветный", "мотоциклет")
auto_5.go(500)
auto_5.show_speed()
auto_5.turn("прямо")
auto_5.show_speed()
