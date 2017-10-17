from .prisoner import *


class Overseer(Prisoner):

    def __init__(self):
        super().__init__()
        self._salary = '8888'
        self._phone_numb = '9999999999'

    def print_data(self):
        print('<td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td>'
              .format(self._first_name, self._last_name, self._age, self._salary, self._phone_numb))

    def edit_data(self):
        super().edit_data()
        print('<tr><td>Salary:</td><td><input type="text" name="salary" value="{}"></td><tr>'
              .format(self._salary),
              '<tr><td>Phone number:</td><td><input type="text" name="phone_numb" value="{}"></td></tr>'
              .format(self._phone_numb))

    def get_data(self, f_param):
        super().get_data(f_param)
        self._salary = f_param.getvalue('salary')
        self._phone_numb = f_param.getvalue('phone_numb')

