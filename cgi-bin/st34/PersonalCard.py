from .UIFunc import *


class PersonalCard:
    _first_name: str = ''
    _last_name: str = ''
    _birth_date: str = ''

    def __init__(self):
        pass

    def show_form(self, self_id, q):
        print(LoadTemplate('personal_form').format(
            q['student'].value,
            self_id,
            self._first_name,
            self._last_name,
            self._birth_date
        ))

    def show_edit(self, q, url):
        print(LoadTemplate('preserve_pc').format(
            url,
            q['student'].value,
            q['card_id'].value,
            True,
            self._first_name,
            self._last_name,
            self._birth_date
        ))

    def set_parameters(self, q):
        self._first_name = q['first_name'].value
        self._last_name = q['last_name'].value
        self._birth_date = q['birth_date'].value