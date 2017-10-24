from .PersonalCard import *
from .UIFunc import *


class EmployeeCard(PersonalCard):
    _job_title: int = 0

    def __init__(self):
        pass

    def show_form(self, self_id, q):
        print(LoadTemplate('employee_form').format(
            q['student'].value,
            self_id,
            self._first_name,
            self._last_name,
            self._birth_date,
            self._job_title
        ))

    def show_edit(self, q, url):
        print(LoadTemplate('preserve_ec').format(
            url,
            q['student'].value,
            q['card_id'].value,
            False,
            self._first_name,
            self._last_name,
            self._birth_date,
            self._job_title
        ))

    def set_parameters(self, q):
        super().set_parameters(q)
        self._job_title = q['job_title'].value