from .Goalkeeper import Goalkeeper, Player
from .LoadTpl import *
import pickle


class Container:
    __player_container = []
    CONTAINER_FILE = "cgi-bin/st25/container.pkl"

    def __init__(self, q, instance_url):
        self.__q = q
        self.__instance_url = instance_url

    def show_edit(self):
        self.__read_container_from_file()
        id = int(self.__q['player_id'].value)

        if id == -1:
            if self.__q['is_parent'].value == "True":
                player = Player(self.__q, self.__instance_url)
            else:
                player = Goalkeeper(self.__q, self.__instance_url)
            player.show_edit()
        else:
            self.__player_container[id].show_edit()

    def save_player(self):
        self.__read_container_from_file()
        id = int(self.__q['player_id'].value)

        if id == -1:
            if self.__q['is_parent'].value == "True":
                player = Player(self.__q, self.__instance_url)
            else:
                player = Goalkeeper(self.__q, self.__instance_url)
            player.set_parameters()
            self.__player_container.append(player)
        else:
            player = self.__player_container[id]
            player.set_parameters()

        self.__write_container_to_file()
        print(loadTpl('redirect').format(self.__instance_url, self.__q['student'].value))

    def remove_player(self):
        self.__read_container_from_file()
        id = int(self.__q['player_id'].value)
        del self.__player_container[id]
        self.__write_container_to_file()
        print(loadTpl('redirect').format(self.__instance_url, self.__q['student'].value))
        pass

    def show_container(self):
        self.__read_container_from_file()
        print(loadTpl('show_header'))
        for i, player in enumerate(self.__player_container):
            player.show(i)
        print(loadTpl('show_footer'))

    def clear(self):
        self.__read_container_from_file()
        self.__player_container.clear()
        self.__write_container_to_file()

        print(loadTpl('container_menu').format(
            self.__q['student'].value,
            self.__instance_url
        ))

    def __write_container_to_file(self):
        output = open(self.CONTAINER_FILE, 'wb')
        pickle.dump(self.__player_container, output, -1)
        output.close()

    def __read_container_from_file(self):
        pkl_file = open(self.CONTAINER_FILE, 'rb')
        self.__player_container = pickle.load(pkl_file)
        for i, player in enumerate(self.__player_container):
            if isinstance(player, Player):
                player.set_q_and_url(self.__q, self.__instance_url)
        pkl_file.close()
