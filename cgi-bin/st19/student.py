class Student:
    def __init__(self):
        self.name = ""
        self.sex = ""
        self.age = ""
        self.grants = ""     

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
        print('<br><br><input type = "submit" value = "Применить">')
        print('<input type="hidden" name = "i" value = "ok" >')
        print('</form></tr></td></table>')

        
    def vvod (self, q, selfurl):
        self.q = q
        self.selfurl = selfurl
        if ('name' in self.q):
            self.name = self.q['name'].value
        else: self.name = ""
        if ('sex' in self.q):
            self.sex = self.q['sex'].value
        else: self.sex = ""
        if ('age' in self.q):
            self.age = self.q['age'].value
        else: self.age = ""
        if ('grants' in self.q):
            self.grants = self.q['grants'].value
        else: self.grants = ""
        
        
    def vyvod(self):
        print("<br> Имя: {0} <br> Пол: {1} <br> Возраст: {2} <br> Зарплата: {3} ".format(self.name, self.sex, self.age, self.grants))


