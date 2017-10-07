from .AbstractView import AbstractView
from ...model.Car import Car
from ...model.UsedCar import UsedCar


class EditCarView(AbstractView):
    def render(self):
        car = self._params.get('car')

        request_url = self._params.get('request_url')
        request_params = self._params.get('request_params')

        print('<a href=' + request_url + '?student=' + request_params.getvalue('student') + '>back</a>')

        print('<form action="' + request_url + '" method="get">')
        print('<input type="hidden" name="student" value="' + request_params.getvalue('student') + '">')
        print('<input type="hidden" name="route" value="car/update">')

        style = 'bgcolor="#82e0a3"'
        if (isinstance(car, UsedCar)):
            style = 'bgcolor="#ffc1c7"'

        print('<table ' + style + ' frame="box">')

        if (isinstance(car, Car)):
            car_id = self._params.get('car_id')
            model = car.get_model()
            year_of_manufacture = car.get_year_of_manufacture()
            color = car.get_color()
            price = car.get_price()
            print('<tr><td>№:</td><td><input type="text" name="id" value="' + str(car_id) + '" readonly></td></tr>')

            print('<tr><td>model:</td><td><input type="text" name="model" value="' + str(model) + '"></td></tr>')
            print('<tr><td>year_of_manufacture:</td><td><input type="text" name="year_of_manufacture" value="' +
                  str(year_of_manufacture) + '"></td></tr>')
            print('<tr><td>color:</td><td><input type="text" name="color" value="' + str(color) + '"></td></tr>')
            print('<tr><td>price:</td><td><input type="text" name="price" value="' + str(price) + '"></td></tr>')

        if (isinstance(car, UsedCar) or car is None):
            mileage = car.get_mileage()
            print('<tr><td>mileage:</td><td><input type="text" name="mileage" value="'
                  + str(mileage) + '"></td></tr>')

        print('<tr><td></td><td><input type="submit" value="Edit"></td></tr>')

        print('</table>')
        print('</form>')
