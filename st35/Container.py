from .PersonalCard import *
from .EmployeeCard import *
from .UIFunc import *
import pickle


class Container:
    container = []
    FILENAME = "cgi-bin/st35/Storage/container.pkl"

    def __init__(self, q, instance_url):
        self.__q = q
        self.__instance_url = instance_url

    def show_menu(self):
        self.__read_from_file()
        print(LoadTemplate('header'))
        for i, card in enumerate(self.container):
            card.show_form(i, self.__q)
        print(LoadTemplate('footer'))

        print(LoadTemplate('menu').format(
            self.__q['student'].value,
            self.__instance_url
        ))

    def show_edit_card(self):
        self.__read_from_file()
        id = int(self.__q['card_id'].value)

        if id == -1:
            if self.__q['is_parent'].value == "True":
                card = PersonalCard()
            else:
                card = EmployeeCard()
            card.show_edit(self.__q, self.__instance_url)
        else:
            self.container[id].show_edit(self.__q, self.__instance_url)

    def save_personal_card(self):
        self.__read_from_file()
        id = int(self.__q['card_id'].value)

        if id == -1:
            if self.__q['is_parent'].value == "True":
                card = PersonalCard()
            else:
                card = EmployeeCard()
            card.set_parameters(self.__q)
            self.container.append(card)
        else:
            card = self.container[id]
            card.set_parameters(self.__q)

        self.__write_to_file()
        print(LoadTemplate('refresh').format(self.__instance_url, self.__q['student'].value))

    def delete_personal_card(self):
        self.__read_from_file()
        id = int(self.__q['card_id'].value)
        del self.container[id]

        self.__write_to_file()
        print(LoadTemplate('refresh').format(self.__instance_url, self.__q['student'].value))
        pass

    def show_container(self):
        self.__read_from_file()
        print(LoadTemplate('header'))
        for i, personal_card in enumerate(self.container):
            personal_card.show(i)
        print(LoadTemplate('footer'))

    def clear_container(self):
        self.__read_from_file()
        self.container.clear()
        self.__write_to_file()

        print(LoadTemplate('menu').format(
            self.__q['student'].value,
            self.__instance_url
        ))

    def __write_to_file(self):
        output = open(self.FILENAME, 'wb')
        pickle.dump(self.container, output, -1)
        output.close()

    def __read_from_file(self):
        pkl_file = open(self.FILENAME, 'rb')
        self.container = pickle.load(pkl_file)
        pkl_file.close()