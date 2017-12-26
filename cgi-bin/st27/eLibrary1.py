import pickle

from Sbornik import Sbornik
from MestSbornik import MestSbornik

class eLibrary:

    def __init__(self):
        self.list_sbornik = []

    def add_sbornik(self):
        new_sb = Sbornik()
        new_sb.create_sbornik()
        self.list_sbornik.append(new_sb)
        print("Сборник добавлен успешно!")

    def add_mest_sbornik(self):
        new_sb = MestSbornik()
        new_sb.create_sbornik()
        self.list_sbornik.append(new_sb)
        print("Местный Сборник добавлен успешно!")

    def delete_sbornik(self):
        id = input("Номер Сборника, который нужно удалить: ")
        self.list_sbornik.pop(int(id)-1)
        print("Заданный Сборник удален успешно!")

    def change_elibrary(self):
        id = input("Номер Сборника, который нужно отредактировать: ")
        self.list_sbornik[int(id)].change_sbornik()

    def print_elibrary(self):
        for i, sbornik in enumerate(self.list_sbornik):
            print("№: ", i)
            sbornik.print_sbornik()
            print()

    def clear_elibrary(self):
        self.list_sbornik.clear()
        print("Библиотека очищена")

    def write_to_file(self):
        file_output = open('eLibrary.dat', 'wb')
        pickle.dump(self.list_sbornik, file_output)
        print('Библиотека записана в файл.')

    def read_from_file(self):
        file_input = open('eLibrary.dat', 'rb')
        self.list_sbornik = pickle.load(file_input)
        print('Библиотека считана из файла.')
        
