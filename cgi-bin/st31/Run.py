import datetime

class Run:    
    attrs = ('length', 'time')
    names = ('Дистанция (в км)', 'Время (в мин)')
    
    def __init__(self, length=0, time=0):
        self.length = length
        self.time = time
        
        now = datetime.datetime.now()
        self.date = '{0}.{1}.{2}'.format(str(now.day), str(now.month), str(now.year))
        
    def hours(self):
        raw = int(self.time) // 60
        return raw
        
    def minutes(self):
        raw = int(self.time) - self.hours() * 60
        if raw < 10:
            return '0' + str(raw)
        return str(raw)
        
    def update(self, q):
        for attr in self.attrs:
            if attr in q:
                setattr(self, attr, q[attr].value)
                
    def show(self):   
        return 'Пробежка {0} - {1} км за {2}:{3}'.format(self.date, self.length, self.hours(), self.minutes())
        
