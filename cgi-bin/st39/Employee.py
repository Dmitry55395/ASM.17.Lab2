from .templateLoader import load_template


class Employee:
    def __init__(self, q, selfurl):
        self._q = q
        self._selfurl = selfurl
        self._id = None
        self._name = None
        self._position = None
        self._salary = None

    def edit(self):
        print(load_template('employee_form').format(
            self._selfurl,
            self._q['student'].value,
            self._id,
            self._name,
            self._position,
            self._salary
        ))

    def display(self):
        print(load_template('display_employee').format(
            self._q['student'].value,
            self._id,
            self._name,
            self._position,
            self._salary))

    def add(self):
        print(load_template('employee_form').format(
            self._selfurl,
            self._q['student'].value,
            -1,
            '', '', ''
        ))


    def save(self, id):
        self._id = id
        self._name = self._q.getvalue('name', '')
        self._position = self._q.getvalue('position', '')
        self._salary = self._q.getvalue('salary', '')





