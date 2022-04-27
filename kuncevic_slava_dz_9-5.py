class Stationery:
    def __init__(self, title='Рисуем "Тайную вечерю" своими руками:'):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки. {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Делаем экскиз с помощью {self.title} карандаша.")


class Pen(Stationery):
    def draw(self):
        print(f"Растушуем {self.title} ручкой.")


class Marker(Stationery):
    def draw(self):
        print(f"Раскрасим {self.title} фламастерами. Готово!")


stat = Stationery()
stat.draw()
pencil = Pencil("ТМ")
pencil.draw()
pen = Pen("перьевой")
pen.draw()
marker = Marker("цветными")
marker.draw()

