from .dc import *


class DesignerCloSH(DesignerClothers):  # класс потомок

    def __init__(self):  # конструктор
        super().__init__() #обращение к родительску классу
        self.quantity_shoes = ""
        self.university = ""


    def writed(self, q, selfurl, index = 0):  # запись данных
        self.q = q
        self.selfurl = selfurl
        print('<br><table><tr><td>')
        print('<form action="{0}" method="get">'.format(self.selfurl))
        print('<input type="hidden" name = "student" value = "{0}" >'.format(self.q['student'].value))
        print('<br> Имя: ')
        print('<input type = "text" name = "named" value="{0}">'.format(self.named))
        print('Стаж работы:')
        print('<input type = "text" name = "experience" value="{0}">'.format(self.experience))
        print('Количество коллекций одежы: ')
        print('<input type = "text" name = "quantity_clothers" value="{0}">'.format(self.quantity_clothers))
        print('Количество коллекций обуви: ')
        print('<input type = "text" name = "quantity_shoes" value="{0}">'.format(self.quantity_shoes))
        print('Образование: ')
        print('<input type = "text" name = "university" value="{0}">'.format(self.university))

        print('<br><br><input type = "submit" value = "Применить">')
        print('<input type="hidden" name = "i" value = "{}" >'.format(q['i'].value))
        print('<input type="hidden" name = "index" value = "{}" >'.format(index))
        print('<input type="hidden" name = "res" value = "ok" >')
        print('</form></tr></td></table>')

    def add(self, q, selfurl):  # запись данных
        if ('named' in q):
            self.named = q['named'].value
        else:
            self.named = ""
        if ('experience' in q):
            self.experience = q['experience'].value
        else:
            self.experience = ""
        if ('quantity_clothers' in q):
            self.quantity_clothers = q['quantity_clothers'].value
        else:
            self.quantity_clothers = ""
        if ('quantity_shoes' in q):
            self.quantity_shoes = q['quantity_shoes'].value
        else:
            self.quantity_shoes = ""
        if ('university' in q):
            self.university = q['university'].value
        else:
            self.university = ""


    def info_rew(self):  # отображение записанных данных
        print("<br> Имя: {0} <br> Стаж работы: {1} <br> Количество коллекций одежды: {2} <br> Количество коллекций обуви: {3} <br> Образование: {4}".format(self.named, self.experience, self.quantity_clothers, self.quantity_shoes, self.university))

