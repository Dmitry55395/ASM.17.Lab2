from abc import ABCMeta, abstractmethod


class AbstractView(metaclass=ABCMeta):
    def __init__(self, params):
        self._params = params

    @abstractmethod
    def render(self):
        pass
