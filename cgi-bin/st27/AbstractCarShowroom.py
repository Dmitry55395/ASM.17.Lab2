from abc import ABCMeta, abstractmethod
from .model.AbstractCar import AbstractCar


class AbstractCarShowroom(metaclass=ABCMeta):
    @abstractmethod
    def set_cars(self, cars: [AbstractCar]):
        pass

    @abstractmethod
    def set_car(self, index: int, car: AbstractCar):
        pass

    @abstractmethod
    def add_car(self, car: AbstractCar):
        pass

    @abstractmethod
    def delete_car(self, index: int):
        pass

    @abstractmethod
    def get(self, index: int) -> AbstractCar:
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass
