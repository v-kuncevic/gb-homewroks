class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def how_much_asphalt(self, weight=25, thickness=5):
        return f'Чтобы покрыть дорожное полотно необходимо ' \
               f'{(self._length * self._width * weight * thickness) / 1000} тонн асфальта '


road_repair = Road(int(input("Ширина дороги: ")), int(input("Длина отрезка: ")))
print(road_repair.how_much_asphalt())
