from .emploee import Employee

class Developer(Employee):
     
    def __init__(self):
        Employee.__init__(self)
        self.language = ""
        self.exp = ""

    def form(self, q, selfurl):
        self.q = q
        self.selfurl = selfurl
        print('<br><table cellpadding="7" border="1"><tr><td>')
        print('<form action="{0}" method="get">'.format(self.selfurl))
        print('<input type="hidden" name = "index" value = "{0}" >'.format(self.q['index'].value))
        print('<input type="hidden" name = "student" value = "{0}" >'.format(self.q['student'].value))
        print('<br> Имя: ')
        print('<input type = "text" name = "name" value="{0}">'.format(self.name))
        print('Возраст:')
        print('<input type = "number" name = "age" value="{0}">'.format(self.age))
        print('Дата начала работы(dd/mm/yyyy): ')
        print('<input type = "date" name = "start" value="{0}">'.format(self.start))
        print('Зарплата: ')
        print('<input type = "number" name = "salary" value="{0}">'.format(self.salary))
        print('Язык программирования: ')
        print('<input type = "text" name = "language" value="{0}">'.format(self.language))
        print('Стаж программирования (лет): ')
        print('<input type = "number" name = "exp" value="{0}">'.format(self.exp))
        print('<input type = "submit" value = "Применить">')
        print('<input type="hidden" name = "action" value = "7" >')
        print('</form></tr></td></table>')

    def read(self, q, selfurl):
        self.q = q
        self.selfurl = selfurl
        self.name=self.q['name'].value
        self.age = self.q['age'].value
        self.start = self.q['start'].value
        self.salary = self.q['salary'].value
        self.language = self.q['language'].value
        self.exp = self.q['exp'].value

    def show(self):
        print("<br>Имя: {0} | Возраст: {1} | Дата начала работы(dd/mm/yyyy): {2} | Зарплата: {3} | Язык программирования: {4} | Стаж программирования (лет): {5}".format(self.name,self.age,self.start,self.salary,self.language,self.exp))
