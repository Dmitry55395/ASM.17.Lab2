import datetime

from .Run import Run

class Marathon(Run):
    attrs = ('length', 'time', 'place')
    names = ('Дистанция (в км)', 'Время (в мин)', 'Место')
    
    def __init__(self, length=0, time=0, place=1):
        Run.__init__(self, length, time)
        self.place = place
        
    def show(self):        
        return 'Марафон {0} - {1} км за {2}:{3}, {4} место'.format(self.date, self.length, self.hours(), self.minutes(), self.place)