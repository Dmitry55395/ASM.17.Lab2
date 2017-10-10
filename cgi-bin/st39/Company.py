from .Employee import Employee
from .Supervisor import Supervisor
from .templateLoader import load_template
import pickle
import os


class Company:
    FILENAME = 'cgi-bin/st39/dump.pkl'

    def __init__(self, q, selfurl):
        self._q = q
        self._selfurl = selfurl
        self._staff = []
        self._counter = 0

    def add_employee(self):
        e = Employee(self._q, self._selfurl)
        e.add()

    def add_supervisor(self):
        s = Supervisor(self._q, self._selfurl)
        s.add()

    def edit_person(self):
        id = self._q['id'].value
        e = self._staff_found()
        e.edit()

    def _save_person(self, person):
        id = self._q['id'].value
        if id == '-1':  # add
            person.save(self._counter)
            self._staff.append(person)
            self._counter += 1
        else:
            person._q = self._q
            person.save(self._q['id'].value)

        self.display_staff()

    def save_employee(self):
        id = self._q['id'].value
        if id == '-1':
            e = Employee(self._q, self._selfurl)
        else:
            e = self._staff_found()
        self._save_person(e)

    def save_supervisor(self):
        id = self._q['id'].value
        if id == '-1':
            s = Supervisor(self._q, self._selfurl)
        else:
            s = self._staff_found()
        self._save_person(s)

    def display_staff(self):
        print(load_template('table_header'))
        for person in self._staff:
            person._q = self._q
            person.display()
        print(load_template('menu').format(
            self._selfurl,
            self._q['student'].value))

    def clear_staff(self):
        self._staff.clear()
        self.display_staff()


    def remove_person(self):
        item = self._staff_found()
        self._staff.remove(item)
        self.display_staff()

    def write_to_file(self):
        pickle.dump(self._staff, open(Company.FILENAME, 'wb'))

    def read_from_file(self):
        if (os.path.exists(Company.FILENAME)):
            self._staff.clear()
            self._staff = pickle.load(open(Company.FILENAME, 'rb'))
            if self._staff:
                self._counter = int(self._staff[-1]._id) + 1


    def _staff_found(self):  #
        id = self._q['id'].value
        for item in self._staff:
            if str(item._id) == id:
                return item