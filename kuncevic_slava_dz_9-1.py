import time
import colorama
from colorama import Fore

colorama.init()


class TrafficLight:
    __traffic_color = ['Красный', 'Жёлтый', 'Зелёный']

    def traffic_signal(self):
        while True:
            a = self.__traffic_color
            b = '    '
            for i in a:
                if i == 'Красный':
                    print(Fore.RED + f'{i}', end='')
                    time.sleep(7)
                    print(f'{b}\r', end='', )
                elif i == 'Жёлтый':
                    print(Fore.YELLOW + f'{i}', end='')
                    time.sleep(2)
                    print(f'{b}\r', end='', )
                else:
                    print(Fore.GREEN + f'{i}', end='')
                    time.sleep(7)
                    print(f'{b}\r', end='', )


exemple = TrafficLight()
exemple.traffic_signal()
