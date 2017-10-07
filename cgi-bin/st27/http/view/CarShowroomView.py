from .AbstractView import AbstractView
from ...model.Car import Car
from ...model.UsedCar import UsedCar


class CarShowroomView(AbstractView):
    def render(self):
        cars = self._params['car_showroom'].get_all()
        request_url = self._params['request_url']
        request_params = self._params['request_params']
        print('<a href=' + request_url + '>back</a>')
        print('<table border="1" cellspacing="0" cellpadding="5">'
              '<tr>'
              '<th>№</th>'
              '<th>model</th>'
              '<th>year_of_manufacture</th>'
              '<th>color</th>'
              '<th>price</th>'
              '<th>mileage</th>'
              '<th></th>'
              '</tr>')
        num = 1
        for car in cars:
            data = car.get_data()

            style = 'bgcolor="#82e0a3"'
            if (isinstance(car, UsedCar)):
                style = 'bgcolor="#ffc1c7"'

            if (isinstance(car, Car)):
                print('<tr ' + style + '>')
                print('<td align=center>' + str(num) + '</td>')
                print('<td>' + str(data['model']) + '</td>')
                print('<td align=center>' + str(data['year_of_manufacture']) + '</td>')
                print('<td>' + str(data['color']) + '</td>')
                print('<td align=center>' + str(data['price']) + '</td>')
            if (isinstance(car, UsedCar)):
                print('<td>' + str(data['mileage']) + '</td>')
            else:
                print('<td></td>')

            print('<td>'
                  '<a href=' + request_url + '?student=' + str(request_params.getvalue('student'))
                  + '&route=car/edit&id=' + str(num) + '>edit</a>&nbsp' +
                  '<a href=' + request_url + '?student=' + str(request_params.getvalue('student'))
                  + '&route=car/delete&id=' + str(num) + '>delete</a></td>')

            print('</tr>')
            num += 1
        print('</table>')
        print('<a href=' + request_url + '?student=' + str(request_params.getvalue('student'))
              + '&route=car/create>add</a>')
