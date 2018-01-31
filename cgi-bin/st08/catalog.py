import pickle
from .dcsh import *

class Catalog:
    d = [] # Инициализация стека

    def __init__(self, q, selfurl):
        self.q = q
        self.selfurl = selfurl

    def mn(self):
        self.read_file()
        print("----------")
        print("<p><a href = {0}?student={1}&i=plus_dc>1. Добавить дизайнера одежды</a></p>".format(self.selfurl, self.q['student'].value))
        print("<p><a href = {0}?student={1}&i=plus_dcsh>2. Добавить дизайнера одежды и обуви</a></p>".format(self.selfurl, self.q['student'].value))
        print("<p><a href = {0}?student={1}&i=print>3. Вывести список дизайнеров на экран</a></p>".format(self.selfurl, self.q['student'].value))
        print("<p><a href = {0}?student={1}&i=clear_catalog>4. Очистить список дизайнеров</a></p>".format(self.selfurl, self.q['student'].value))
        print("<p><a href = {0}>Вернуться в главное меню</a></p>".format(self.selfurl))
        print("----------")

    # 1 - Добавить дизайнера одежды
    def plus_dc(self):
        self.read_file()
        des_clo = DesignerClothers()  # экземпляр класса
        if ("res" in self.q) :
            if (self.q['res'].value == 'ok'):
                des_clo.add(self.q, self.selfurl)
                self.d.append(des_clo)  # добавление информации в стек
                self.write_file()
        else : des_clo.writed(self.q, self.selfurl)  # заполнение класса данными
        self.print()

    # 2 - Добавить дизайнера одежды и обуви
    def plus_dcsh(self):
        self.read_file()
        des_clo_sh = DesignerCloSH()  # экземпляр класса
        if ("res" in self.q) :
            if (self.q['res'].value == 'ok'):
                des_clo_sh.add(self.q, self.selfurl)
                self.d.append(des_clo_sh)  # добавление информации в стек
                self.write_file()
        else : des_clo_sh.writed(self.q, self.selfurl)  # заполнение класса данными
        self.print()

    # 3 - Вывести список дизайнеров на экран
    def print(self):
        print('<br><br><h1>Дизайнеры</h1><br><br>')
        for desig in self.d:
            print("№: {0}".format(self.d.index(desig) + 1))
            desig.info_rew()
            print("<br><a href = {0}?i=rewrite&index={1}&student={2}> Редактировать</a> / ".format(self.selfurl,
                                                                                                self.d.index(desig),
                                                                                                self.q[
                                                                                                    'student'].value))
            print("<a href = {0}?i=delete&index={1}&student={2}>Удалить<br><br></a>".format(self.selfurl,
                                                                                            self.d.index(desig),
                                                                                            self.q['student'].value))
        if len(self.d) == 0:
            print("<br>Список пуст<br>")

    # 4 - Редактировать данные о дизайнере
    def rewrite(self):
        self.read_file()
        des_clo = self.d[int(self.q['index'].value) ]
        if ("res" in self.q) :
            if (self.q['res'].value == 'ok'):
                des_clo.add(self.q, self.selfurl)
                self.write_file()
        else : des_clo.writed(self.q, self.selfurl, self.d.index(des_clo))  # заполнение класса данными

        self.write_file()
        self.print()

    # 5 - Удалить данные
    def delete(self):
        self.read_file()
        self.d.pop(int(self.q["index"].value))
        self.write_file()
        self.print()

    # 6 - Сохранить список дизайнеров в файл
    def write_file(self):
        with open('cgi-bin/st08/data.dat', 'wb') as f:  #wb - перезапись файла в бинарном режиме
            pickle.dump(self.d, f)
        f.close()

    # 7 - Загрузить список дизайнеров из файла
    def read_file(self):
        with open('cgi-bin/st08/data.dat', 'rb') as f:
            self.d = pickle.load(f)
        f.close()

    # 8 - Очистить список дизайнеров
    def clear_catalog(self):
        self.read_file()
        self.d.clear()
        self.write_file()
        print("<p>Список очищен</p>")