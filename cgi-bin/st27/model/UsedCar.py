from .Car import Car


class UsedCar(Car):
    _mileage: float

    def __init__(self, model=None, year_of_manufacture=None, color=None, price=None, mileage=None):
        super().__init__(model, year_of_manufacture, color, price)
        self._mileage = mileage

    def get_data(self) -> dict:
        data = super().get_data()
        data['mileage'] = self._mileage
        return data

    def set_mileage(self, mileage: float):
        self._mileage = mileage

    def get_mileage(self):
        return self._mileage
