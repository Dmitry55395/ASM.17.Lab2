from .Container import *
from .LoadTpl import *


class Group:
    __container: Container = None

    def __init__(self, container, url, q):
        self.__container = container
        self.__url = url
        self.__q = q

    def show_content(self):
        content = {
            'show_menu': self.show_menu,
            'show_edit': self.__container.show_edit,
            'save_player': self.__container.save_player,
            'remove_player': self.__container.remove_player,
            'clear_container': self.__container.clear,

        }

        if 'action' in self.__q:
            content[self.__q['action'].value]()
        else:
            content['show_menu']()

    def show_menu(self):
        self.__container.show_container()
        print(loadTpl('container_menu').format(
            self.__q['student'].value,
            self.__url
        ))