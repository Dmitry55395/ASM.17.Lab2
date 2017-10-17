from .drilling_rig import *

class Developed_rig(Drilling_rig):
    def __init__(self):
        super().__init__()
        self.source_nation = ""
        self.colour = ""


    def intro(self, q ,selfurl):
        self.q = q
        self.selfurl = selfurl
        print('<br><table><tr><td>')
        print('<form action="{0}" method="get">'.format(self.selfurl))
        print('<input type="hidden" name = "index" value = "{0}" >'.format(self.q['index'].value))
        print('<input type="hidden" name = "student" value = "{0}" >'.format(self.q['student'].value))
        print('<br> Название:')
        print('<input type = "text" name = "name" value="{0}">'.format(self.name))
        print('Дата:')
        print('<input type = "text" name = "date" value="{0}">'.format(self.date))
        print('Мощность:')
        print('<input type = "text" name = "capacity" value="{0}">'.format(self.capacity))
        print('Страна:')
        print('<input type = "text" name = "source_nation" value="{0}">'.format(self.source_nation))
        print('Цвет:')
        print('<input type = "text" name = "colour" value="{0}">'.format(self.colour))
        print('<br><br><input type = "submit" value = "Применить">')
        print('<input type="hidden" name = "action" value = "7" >')
        print('</form></tr></td></table>')


    def look(self, q ,selfurl):
        super().look(q ,selfurl)
        if ('source_nation' in self.q):
            self.source_nation = self.q['source_nation'].value
        else: self.source_nation = ""
        if ('colour' in self.q):
            self.colour = self.q['colour'].value
        else: self.colour = ""


    def letter(self):
        print("<br>Название: {0} | Дата: {1} | Мощность: {2} | Страна: {3} | Цвет: {4}".format(self.name, self.date, self.capacity, self.source_nation, self.colour))

