#класс описывающий элемент картотеки "Магазин"
from .LoadTpl import *

class Market:
    _nickname: str = ''
    _owner_name: str = ''
    _address: str = ''

    
    def __init__(self, q, instance_url):
        self._q = q
        self._instance_url = instance_url

    def show(self, self_id):
        print(loadTpl('show_Market').format(
            self._q['student'].value,
            self_id,
            self._nickname,
            self._owner_name,
            self._address
        ))

    def show_edit(self):
        print(loadTpl('save_Market').format(
            self._instance_url,
            self._q['student'].value,
            self._q['market_id'].value,
            True,
            self._nickname,
            self._owner_name,
            self._address
        ))

    def set_parameters(self):
        self._nickname = self._q['nickname'].value
        self._owner_name = self._q['owner_name'].value
        self._address = self._q['address'].value

    def set_q_and_url(self, q, _instance_url):
        self._q = q
        self._instance_url = _instance_url
