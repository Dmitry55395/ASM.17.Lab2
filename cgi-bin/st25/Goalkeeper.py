from .Player import *
from .LoadTpl import *


class Goalkeeper(Player):
    __reaction: int = 0

    def __init__(self, q, instance_url):
        super().__init__(q, instance_url)

    def show(self, self_id):
        print(loadTpl('show_goalkeeper').format(
            self._q['student'].value,
            self_id,
            self._playername,
            self._raiting,
            self.__reaction
        ))

    def show_edit(self):
        print(loadTpl('save_goalkeeper').format(
            self._instance_url,
            self._q['student'].value,
            self._q['player_id'].value,
            False,
            self._playername,
            self._raiting,
            self.__reaction
        ))

    def set_parameters(self):
        super().set_parameters()
        self.__reaction = self._q['reaction'].value
