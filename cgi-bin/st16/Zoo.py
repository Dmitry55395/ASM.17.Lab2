from .Bird import Bird, Animal
from .LoadTpl import *
import pickle


class Zoo:
    __animal_container = []
    ZOO_FILENAME = "cgi-bin/st16/Storage/zoo.pkl"

    def __init__(self, q, instance_url):
        self.__q = q
        self.__instance_url = instance_url

    def show_edit(self):
        self.__read_zoo_from_file()
        id = int(self.__q['animal_id'].value)

        if id == -1:
            if self.__q['is_parent'].value == "True":
                animal = Animal(self.__q, self.__instance_url)
            else:
                animal = Bird(self.__q, self.__instance_url)
            animal.show_edit()
        else:
            self.__animal_container[id].show_edit()

    def save_animal(self):
        self.__read_zoo_from_file()
        id = int(self.__q['animal_id'].value)

        if id == -1:
            if self.__q['is_parent'].value == "True":
                animal = Animal(self.__q, self.__instance_url)
            else:
                animal = Bird(self.__q, self.__instance_url)
            animal.set_parameters()
            self.__animal_container.append(animal)
        else:
            animal = self.__animal_container[id]
            animal.set_parameters()

        self.__write_zoo_to_file()
        print(loadTpl('redirect').format(self.__instance_url, self.__q['student'].value))

    def remove_animal(self):
        self.__read_zoo_from_file()
        id = int(self.__q['animal_id'].value)
        del self.__animal_container[id]
        self.__write_zoo_to_file()
        print(loadTpl('redirect').format(self.__instance_url, self.__q['student'].value))
        pass

    def show_zoo(self):
        self.__read_zoo_from_file()
        print(loadTpl('show_header'))
        for i, animal in enumerate(self.__animal_container):
            animal.show(i)
        print(loadTpl('show_footer'))

    def clear(self):
        self.__read_zoo_from_file()
        self.__animal_container.clear()
        self.__write_zoo_to_file()

        print(loadTpl('zoo_menu').format(
            self.__q['student'].value,
            self.__instance_url
        ))

    def __write_zoo_to_file(self):
        output = open(self.ZOO_FILENAME, 'wb')
        pickle.dump(self.__animal_container, output, -1)
        output.close()

    def __read_zoo_from_file(self):
        pkl_file = open(self.ZOO_FILENAME, 'rb')
        self.__animal_container = pickle.load(pkl_file)
        for i, animal in enumerate(self.__animal_container):
            if isinstance(animal, Animal):
                animal.set_q_and_url(self.__q, self.__instance_url)
        pkl_file.close()
