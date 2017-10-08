from .Animal import *
from .LoadTpl import *


class Bird(Animal):
    __beak_length: int = 0

    def __init__(self, q, instance_url):
        super().__init__(q, instance_url)

    def show(self, self_id):
        print(loadTpl('show_bird').format(
            self._q['student'].value,
            self_id,
            self._nickname,
            self._limbs_count,
            self.__beak_length
        ))

    def show_edit(self):
        print(loadTpl('save_bird').format(
            self._instance_url,
            self._q['student'].value,
            self._q['animal_id'].value,
            False,
            self._nickname,
            self._limbs_count,
            self.__beak_length
        ))

    def set_parameters(self):
        super().set_parameters()
        self.__beak_length = self._q['beak_length'].value
