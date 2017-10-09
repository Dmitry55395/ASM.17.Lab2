from .Employee import Employee
from .templateLoader import load_template



class Supervisor(Employee):
    def __init__(self, q, selfurl):
        super().__init__(q, selfurl)
        self._responsibility = None
        self._liberties = None


    def edit(self):
        print(load_template('employee_form').format(
            self._selfurl,
            self._q['student'].value,
            self._id,
            self._name,
            self._position,
            self._salary,
            self._responsibility,
            self._liberties
        ))


    def display(self):
        print(load_template('display_supervisor').format(
            self._q['student'].value,
            self._id,
            self._name,
            self._position,
            self._salary,
            self._responsibility,
            self._liberties))

    def add(self):
        print(load_template('supervisor_form').format(
            self._selfurl,
            self._q['student'].value,
            -1,
            '', '', '', '', ''
        ))


    def save(self, id):
        super().save(id)
        self._liberties = self._q.getvalue('liberties', '')
        self._responsibility = self._q.getvalue('responsibility', '')