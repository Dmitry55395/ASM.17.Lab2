from .AbstractCarShowroom import AbstractCarShowroom
from .model.AbstractCar import AbstractCar
import pickle


class CarShowroom(AbstractCarShowroom):
    __cars: []
    __STORAGE_FILE = 'cgi-bin/st27/storage/dump'

    def __init__(self, cars: [] = None):
        if cars is None:
            self.__cars = []
        else:
            self.__cars = cars
        self.__init_from_file()

    def set_cars(self, cars: [AbstractCar]):
        self.__cars = cars

    def set_car(self, index: int, car: AbstractCar):
        self.__cars[index] = car

    def add_car(self, car: AbstractCar):
        self.__cars.append(car)
        return self

    def delete_car(self, index: int):
        self.__cars.pop(index)
        return self

    def get(self, index: int) -> AbstractCar:
        return self.__cars[index]

    def get_all(self) -> [AbstractCar]:
        return self.__cars

    def clear(self):
        self.__cars.clear()
        return self

    def is_empty(self) -> bool:
        return len(self.__cars) == 0

    def __init_from_file(self):
        f = open(self.__STORAGE_FILE, 'rb')
        self.set_cars(pickle.load(f))
        f.close()

    def save(self):
        f = open(self.__STORAGE_FILE, 'wb')
        pickle.dump(self.get_all(), f)
        f.close()
