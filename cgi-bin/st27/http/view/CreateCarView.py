from .AbstractView import AbstractView


class CreateCarView(AbstractView):
    def render(self):
        request_url = self._params.get('request_url')
        request_params = self._params.get('request_params')

        print('<a href=' + request_url + '?student=' + request_params.getvalue('student') + '>back</a>')

        print('<form action="' + request_url + '" method="get">')
        print('<input type="hidden" name="student" value="' + request_params.getvalue('student') + '">')
        print('<input type="hidden" name="route" value="car/store">')

        print('<table frame="box">')

        print('<tr bgcolor="#82e0a3"><td>model:</td><td><input type="text" name="model"></td></tr>')
        print('<tr bgcolor="#82e0a3"><td>year_of_manufacture:</td><td><input type="text" name="year_of_manufacture"></td></tr>')
        print('<tr bgcolor="#82e0a3"><td>color:</td><td><input type="text" name="color"></td></tr>')
        print('<tr bgcolor="#82e0a3"><td>price:</td><td><input type="text" name="price"></td></tr>')

        print('<tr bgcolor="#ffc1c7"><td>mileage:</td><td><input type="text" name="mileage"></td></tr>')

        print('<tr><td></td><td><input type="submit" value="Create"></td></tr>')

        print('</table>')
        print('</form>')
