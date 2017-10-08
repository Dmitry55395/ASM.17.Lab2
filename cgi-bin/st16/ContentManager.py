from .Zoo import *
from .LoadTpl import *


class ContentManager:
    __zoo: Zoo = None

    def __init__(self, zoo, url, q):
        self.__zoo = zoo
        self.__url = url
        self.__q = q

    def show_content(self):
        content = {
            'show_menu': self.show_menu,
            'show_edit': self.__zoo.show_edit,
            'save_animal': self.__zoo.save_animal,
            'remove_animal': self.__zoo.remove_animal,
            'clear_zoo': self.__zoo.clear
        }

        if 'action' in self.__q:
            content[self.__q['action'].value]()
        else:
            content['show_menu']()

    def show_menu(self):
        self.__zoo.show_zoo()
        print(loadTpl('zoo_menu').format(
            self.__q['student'].value,
            self.__url
        ))
