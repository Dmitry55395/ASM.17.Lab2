from .AbsctractController import AbstractController
from ...CarShowroom import CarShowroom
from ...model.Car import Car
from ...model.UsedCar import UsedCar
from ..view.CarShowroomView import CarShowroomView
from ..view.EditCarView import EditCarView
from ..view.CreateCarView import CreateCarView


class CarController(AbstractController):
    def index(self):
        car_showroom = CarShowroom()
        self._render(CarShowroomView, {
            'car_showroom': car_showroom,
            'request_url': self._request_url,
            'request_params': self._request_params
        })

    def create(self):
        self._render(CreateCarView, {
            'request_url': self._request_url,
            'request_params': self._request_params
        })

    def store(self):
        car_showroom = CarShowroom()
        request_params = self._request_params
        mileage = request_params.getvalue('mileage')

        if (mileage is None):
            car = Car(
                request_params.getvalue('model'),
                int(request_params.getvalue('year_of_manufacture')),
                request_params.getvalue('color'),
                float(request_params.getvalue('price'))
            )
        else:
            car = UsedCar(
                request_params.getvalue('model'),
                int(request_params.getvalue('year_of_manufacture')),
                request_params.getvalue('color'),
                float(request_params.getvalue('price')),
                float(mileage),
            )
        car_showroom.add_car(car)
        car_showroom.save()

        redirect_url = self._request_url + '?student=' + request_params.getvalue('student')
        self._redirect(redirect_url)

    def edit(self):
        car_showroom = CarShowroom()
        item_num = int(self._request_params.getvalue('id'))
        car = car_showroom.get(item_num - 1)
        self._render(EditCarView, {
            'request_url': self._request_url,
            'request_params': self._request_params,
            'car': car,
            'car_id': item_num
        })

    def update(self):
        car_showroom = CarShowroom()
        request_params = self._request_params
        id = int(request_params.getvalue('id'))
        mileage = request_params.getvalue('mileage')

        if (mileage is None):
            car = Car(
                request_params.getvalue('model'),
                int(request_params.getvalue('year_of_manufacture')),
                request_params.getvalue('color'),
                float(request_params.getvalue('price'))
            )
        else:
            car = UsedCar(
                request_params.getvalue('model'),
                int(request_params.getvalue('year_of_manufacture')),
                request_params.getvalue('color'),
                float(request_params.getvalue('price')),
                float(mileage),
            )
        car_showroom.set_car(id - 1, car)
        car_showroom.save()

        redirect_url = self._request_url + '?student=' + request_params.getvalue('student')
        self._redirect(redirect_url)

    def destroy(self):
        car_showroom = CarShowroom()
        request_params = self._request_params
        id = int(request_params.getvalue('id'))
        car_showroom.delete_car(id - 1)
        car_showroom.save()

        redirect_url = self._request_url + '?student=' + request_params.getvalue('student')
        self._redirect(redirect_url)
