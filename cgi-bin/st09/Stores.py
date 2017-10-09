from .Department import Department, Market
from .LoadTpl import *
import pickle
import os

class Stores:
    __stores_container = []
    STORES_FILENAME = "cgi-bin/st09/Storage/stores.pkl"

    def __init__(self, q, instance_url):
        self.__q = q
        self.__instance_url = instance_url

    def show_edit(self):
        self.__read_stores_from_file()
        id = int(self.__q['market_id'].value)

        if id == -1:
            if self.__q['is_parent'].value == "True":
                market = Market(self.__q, self.__instance_url)
            else:
                market = Department(self.__q, self.__instance_url)
            market.show_edit()
        else:
            self.__stores_container[id].show_edit()

    def save_Market(self):
        self.__read_stores_from_file()
        id = int(self.__q['market_id'].value)

        if id == -1:
            if self.__q['is_parent'].value == "True":
                market = Market(self.__q, self.__instance_url)
            else:
                market = Department(self.__q, self.__instance_url)
            market.set_parameters()
            self.__stores_container.append(market)
        else:
            market = self.__stores_container[id]
            market.set_parameters()

        self.__write_stores_to_file()
        print(loadTpl('redirect').format(self.__instance_url, self.__q['student'].value))

    def remove_market(self):
        self.__read_stores_from_file()
        id = int(self.__q['market_id'].value)
        del self.__stores_container[id]
        self.__write_stores_to_file()
        print(loadTpl('redirect').format(self.__instance_url, self.__q['student'].value))
        pass

    def show_stores(self):
        self.__read_stores_from_file()
        print(loadTpl('show_header'))
        for i, market in enumerate(self.__stores_container):
            market.show(i)
        print('</table>')

    def clear(self):
        self.__read_stores_from_file()
        self.__stores_container.clear()
        self.__write_stores_to_file()

        print(loadTpl('stores_menu').format(
            self.__q['student'].value,
            self.__instance_url
        ))

    def __write_stores_to_file(self):
        output = open(self.STORES_FILENAME, 'wb')
        pickle.dump(self.__stores_container, output, -1)
        output.close()

    def __read_stores_from_file(self):
        if os.path.exists(self.STORES_FILENAME):
            pkl_file = open(self.STORES_FILENAME, 'rb')
            self.__stores_container = pickle.load(pkl_file)
            for i, market in enumerate(self.__stores_container):
                if isinstance(market, Market):
                    market.set_q_and_url(self.__q, self.__instance_url)
            pkl_file.close()

