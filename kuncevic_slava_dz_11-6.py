from abc import ABC, abstractmethod


class OfficeStorage:
    def __init__(self, name):
        self.__name = name
        self.__office_storage = {}
        self.__office_workplace = {}

    def add_device(self, device):
        if device.__class__.__name__ not in self.__office_storage:
            self.__office_storage[device.__class__.__name__] = [device]
        else:
            self.__office_storage[device.__class__.__name__].append(device)

    def show_office_storage(self):
        print(f'{self.__name} девайсы:')
        for k, v in self.__office_storage.items():
            print(f"\t{k} ({len(v)})")
            for e in v:
                print("\t\t", end='')
                e.show_info()

    def move_office_storage(self, office, device):
        if device.__class__.__name__ not in self.__office_storage:
            raise ValueError(f"{device.__class__.__name__} нет {self.__name}")
        found = list(filter(lambda i: i.serial == device.serial,
                            self.__office_storage[device.__class__.__name__]))
        if len(found) == 0:
            raise ValueError(f"{device.serial} нет {self.__name}")
        self.__office_storage[device.__class__.__name__].remove(found[0])
        if office not in self.__office_workplace:
            self.__office_workplace[office] = [found[0]]
        else:
            self.__office_workplace[office].append(found[0])

    def show_office_workplace(self):
        for k, v in self.__office_workplace.items():
            print(f"{k} {len(v)}")
            for e in v:
                print("\t", end='')
                e.show_info()


class Equipment(ABC):
    def __init__(self, brand_name, serial):
        self._brand_name = brand_name
        self._serial = serial

    @abstractmethod
    def show_info(self):
        pass

    @property
    def serial(self):
        return self._serial


class Printer(Equipment):
    def __init__(self, brand_name, serial, device_type, paper_size, color):
        super().__init__(brand_name, serial)
        self.__type = device_type
        self.__size = paper_size
        self.__color = color

    def show_info(self):
        print(
            f'{self.__class__.__name__} {self._brand_name} {self.__type}'
            f'{self.__size} {self.serial} {self.__color}')


class Scanner(Equipment):
    def __init__(self, brand_name, serial, paper_size):
        super().__init__(brand_name, serial)
        self.__size = paper_size

    def show_info(self):
        print(
            f"{self.__class__.__name__} {self._brand_name} {self.serial} {self.__size}")


class Copycat(Equipment):
    def __init__(self, brand_name, serial, paper_size, is_auto_feed):
        super().__init__(brand_name, serial)
        self.__size = paper_size
        self.__is_auto_feed = is_auto_feed

    def show_info(self):
        print(
            f"{self.__class__.__name__} {self._brand_name} {self.serial} {self.__size}"
            f"{self.__is_auto_feed}")


store = OfficeStorage("Имеются")
store.add_device(Printer("Name", "fcwew7eyw", "Jet", "A4", True))
store.add_device(Scanner("Name", "7fye8w7cwe", "A4"))
store.add_device(Copycat("Name", "67ecewgh43", "A4", False))
store.show_office_storage()

store.move_office_storage("Ушёл", Scanner("Name", "7fye8w7cwe", "A4"))
store.show_office_storage()
store.show_office_workplace()
