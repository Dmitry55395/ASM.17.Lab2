class infcar:

    def __init__(self):
        
        self.mark = ""
        self.color = ""
        self.year = ""

    def table(self, q ,selfurl):
        self.q = q
        self.selfurl = selfurl
        print('<br><table><tr><td>')
        print('<form action="{0}" method="get">'.format(self.selfurl))
        print('<input type="hidden" name = "index" value = "{0}" >'.format(self.q['index'].value))
        print('<input type="hidden" name = "student" value = "{0}" >'.format(self.q['student'].value))
        print('<br> Марка автомобиля: ')
        print('<input type = "text" name = "mark" value="{0}">'.format(self.mark))
        print('Цвет автомобиля:')
        print('<input type = "text" name = "color" value="{0}">'.format(self.color))
        print('Год выпуска автомобиля: ')
        print('<input type = "text" name = "year" value="{0}">'.format(self.year))
        print('<br><br><input type = "submit" value = "Применить">')
        print('<input type="hidden" name = "action" value = "6" >')
        print('</form></tr></td></table>')
    

    def read (self, q ,selfurl):
        self.q = q
        self.selfurl = selfurl
        if ('mark' in self.q):
            self.mark = self.q['mark'].value
        else: self.mark = ""
        if ('color' in self.q):
            self.color = self.q['color'].value
        else: self.year = ""
        if ('year' in self.q):
            self.year = self.q['year'].value
        else: self.year = ""

    def write(self):
        print("<br>Марка автомобиля: {0} | Цвет автомобиля: {1} | Год выпуска автомобиля: {2} ".format(self.mark,self.color,self.year))
