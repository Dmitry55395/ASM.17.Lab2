from abc import ABCMeta, abstractmethod


class AbstractCar(metaclass=ABCMeta):
    @abstractmethod
    def get_data(self) -> dict:
        pass
