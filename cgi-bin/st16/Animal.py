from .LoadTpl import *


class Animal:
    _nickname: str = ''
    _limbs_count: int = 0

    def __init__(self, q, instance_url):
        self._q = q
        self._instance_url = instance_url

    def show(self, self_id):
        print(loadTpl('show_animal').format(
            self._q['student'].value,
            self_id,
            self._nickname,
            self._limbs_count
        ))

    def show_edit(self):
        print(loadTpl('save_animal').format(
            self._instance_url,
            self._q['student'].value,
            self._q['animal_id'].value,
            True,
            self._nickname,
            self._limbs_count
        ))

    def set_parameters(self):
        self._nickname = self._q['nickname'].value
        self._limbs_count = self._q['limbs_count'].value

    def set_q_and_url(self, q, _instance_url):
        self._q = q
        self._instance_url = _instance_url
