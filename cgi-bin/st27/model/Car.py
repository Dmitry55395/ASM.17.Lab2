from .AbstractCar import AbstractCar


class Car(AbstractCar):
    _model: str
    _year_of_manufacture: int
    _color: str
    _price: float

    def __init__(self, model: str = None, year_of_manufacture: int = None, color: str = None, price: float = None):
        self._model = model
        self._year_of_manufacture = year_of_manufacture
        self._color = color
        self._price = price

    def get_data(self) -> dict:
        return {
            'model': self.get_model(),
            'year_of_manufacture': self.get_year_of_manufacture(),
            'color': self.get_color(),
            'price': self.get_price()
        }

    def set_model(self, model: str):
        self._model = model

    def get_model(self):
        return self._model

    def set_year_of_manufacture(self, year_of_manufacture: int):
        self._year_of_manufacture = year_of_manufacture

    def get_year_of_manufacture(self):
        return self._year_of_manufacture

    def set_color(self, color: str):
        self._color = color

    def get_color(self):
        return self._color

    def set_price(self, price: float):
        self._price = price

    def get_price(self):
        return self._price
