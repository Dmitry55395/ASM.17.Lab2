class Prisoner:

    def __init__(self):
        self._first_name = 'Richard'
        self._last_name = 'Ramirez'
        self._age = '24'

    def print_data(self):
        print('<td align="centre">{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td>'
              .format(self._first_name, self._last_name, self._age, 'xxx', 'xxx'))

    def edit_data(self):
        print('<tr><td>First name:</td><td><input type="text" name="f_name" value="{}"></td><tr>'
              .format(self._first_name),
              '<tr><td>Last name:</td><td><input type="text" name="l_name" value="{}"></td></tr>'
              .format(self._last_name),
              '<tr><td>Age:</td><td><input type="text" name="age" value="{}"></td></tr>'
              .format(self._age))

    def get_data(self, f_param):
        self._first_name = f_param.getvalue('f_name')
        self._last_name = f_param.getvalue('l_name')
        self._age = f_param.getvalue('age')
