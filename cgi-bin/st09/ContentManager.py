from .Stores import *
from .LoadTpl import *


class ContentManager:
    __stores: Stores = None

    def __init__(self, stores, url, q):
        self.__stores = stores
        self.__url = url
        self.__q = q

    def show_content(self):
        content = {
            'show_menu': self.show_menu,
            'show_edit': self.__stores.show_edit,
            'save_Market': self.__stores.save_Market,
            'remove_market': self.__stores.remove_market,
            'clear_stores': self.__stores.clear
        }

        if 'action' in self.__q:
            content[self.__q['action'].value]()
        else:
            content['show_menu']()

    def show_menu(self):
        self.__stores.show_stores()
        print(loadTpl('stores_menu').format(
            self.__q['student'].value,
            self.__url
        ))
