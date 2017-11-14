from .part1 import *

class fullinfcar(infcar):
    def __init__(self):
        super().__init__()
        self.power = ""
        self.speed = ""


    def tbl(self, q ,selfurl):
        self.q = q
        self.selfurl = selfurl
        print('<br><table><tr><td>')
        print('<form action="{0}" method="get">'.format(self.selfurl))
        print('<input type="hidden" name = "index" value = "{0}" >'.format(self.q['index'].value))
        print('<input type="hidden" name = "student" value = "{0}" >'.format(self.q['student'].value))
        print('<br> Марка автомобиля:')
        print('<input type = "text" name = "mark" value="{0}">'.format(self.mark))
        print('Цвет автомобиля:')
        print('<input type = "text" name = "color" value="{0}">'.format(self.color))
        print('Год выпуска автомобиля:')
        print('<input type = "text" name = "year" value="{0}">'.format(self.year))
        print('Мощность автомобиля:')
        print('<input type = "text" name = "power" value="{0}">'.format(self.power))
        print('Максимальная скорость автомобиля:')
        print('<input type = "text" name = "speed" value="{0}">'.format(self.speed))
        print('<br><br><input type = "submit" value = "Применить">')
        print('<input type="hidden" name = "action" value = "7" >')
        print('</form></tr></td></table>')


    def read(self, q ,selfurl):
        super().read(q ,selfurl)
        if ('power' in self.q):
            self.power = self.q['power'].value
        else: self.power = ""
        if ('speed' in self.q):
            self.speed = self.q['speed'].value
        else: self.speed = ""


    def write(self):
        print("<br>Марка автомобиля: {0} | Цвет автомобиля: {1} | Год выпуска автомобиля: {2} | Мощность автомобиля: {3} | Максимальная скорость автомобиля: {4}".format(self.mark, self.color, self.year, self.power, self.speed))

