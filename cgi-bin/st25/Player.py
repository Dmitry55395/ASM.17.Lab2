from .LoadTpl import *


class Player:
    _playername: str = ''
    _raiting: int = 0

    def __init__(self, q, instance_url):
        self._q = q
        self._instance_url = instance_url

    def show(self, self_id):
        print(loadTpl('show_player').format(
            self._q['student'].value,
            self_id,
            self._playername,
            self._raiting
        ))

    def show_edit(self):
        print(loadTpl('save_player').format(
            self._instance_url,
            self._q['student'].value,
            self._q['player_id'].value,
            True,
            self._playername,
            self._raiting
        ))

    def set_parameters(self):
        self._playername = self._q['playername'].value
        self._raiting = self._q['raiting'].value

    def set_q_and_url(self, q, _instance_url):
        self._q = q
        self._instance_url = _instance_url