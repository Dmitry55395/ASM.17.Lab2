from .student import *

class Mayor(Student):
    def __init__(self):
        super().__init__()
        self.telephone = ""
        self.doljnost = ""
        

    def me(self, q, selfurl):
        self.q = q
        self.selfurl = selfurl
        print('<br><table><tr><td>')
        print('<form action="{0}" method="get">'.format(self.selfurl))
        print('<input type="hidden" name = "index" value = "{0}" >'.format(self.q['index'].value))
        print('<input type="hidden" name = "student" value = "{0}" >'.format(self.q['student'].value))
        print('<br> Имя: ')
        print('<input type = "text" name = "name" value="{0}">'.format(self.name))
        print('Пол:')
        print('<input type = "text" name = "sex" value="{0}">'.format(self.sex))
        print('Возраст: ')
        print('<input type = "text" name = "age" value="{0}">'.format(self.age))
        print('Зарплата: ')
        print('<input type = "text" name = "grants" value="{0}">'.format(self.grants))
        print('Телефон: ')
        print('<input type = "text" name = "telephone" value="{0}">'.format(self.telephone))
        print('Должность: ')
        print('<input type = "text" name = "doljnost" value="{0}">'.format(self.doljnost))
        print('<br><br><input type = "submit" value = "Применить">')
        print('<input type="hidden" name = "i" value = "okok" >')
        print('</form></tr></td></table>')

        
    def vvod (self, q, selfurl):
        self.q = q
        self.selfurl = selfurl
        super().vvod(q, selfurl)
        if ('telephone' in self.q):
            self.telephone = self.q['telephone'].value
        else: self.telephone = ""
        if ('doljnost' in self.q):
            self.doljnost = self.q['doljnost'].value
        else: self.doljnost = ""
       
        
        
    def vyvod(self):
        print("<br> Имя: {0} <br> Пол: {1} <br> Возраст: {2} <br> Зарплата: {3}<br> Телефон: {4}<br> Должность: {5} ".format(self.name, self.sex, self.age, self.grants, self.telephone, self.doljnost))


