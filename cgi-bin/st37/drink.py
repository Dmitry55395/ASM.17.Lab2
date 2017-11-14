from .food import *

class drink(food):
    def __init__(self):
        super().__init__()
        self.alcogol = ""
        

    def me(self, q, selfurl):
        self.q = q
        self.selfurl = selfurl
        print('<br><table><tr><td>')
        print('<form action="{0}" method="get">'.format(self.selfurl))
        print('<input type="hidden" name = "index" value = "{0}" >'.format(self.q['index'].value))
        print('<input type="hidden" name = "student" value = "{0}" >'.format(self.q['student'].value))
        print('<br> Название: ')
        print('<input type = "text" name = "name" value="{0}">'.format(self.name))
        print('Количество блюд:')
        print('<input type = "text" name = "quantity" value="{0}">'.format(self.quantity))
        print('Каллорий в одной порции: ')
        print('<input type = "text" name = "calories" value="{0}">'.format(self.calories))
        print('Есть алкоголь?: ')
        print('<input type = "text" name = "alcogol" value="{0}">'.format(self.alcogol))
        print('<br><br><input type = "submit" value = "Применить">')
        print('<input type="hidden" name = "j" value = "okok" >')
        print('</form></tr></td></table>')

    def vvod(self, q, selfurl):
        self.q = q
        self.selfurl = selfurl
        super().vvod(q, selfurl)
        if ('alcogol' in self.q):
            self.alcogol = self.q['alcogol'].value
        else: self.alcogol = ""
        
    def vyvod(self):
        print("<br><br>Название: {0} <br> Количество блюд: {1} <br> Каллорий в одной порции: {2} <br>Есть алкоголь?: {3} ".format(self.name, self.quantity, self.calories, self.alcogol))
        
