class Drilling_rig:

    def __init__(self):
        
        self.name = ""
        self.date = ""
        self.capacity = ""

    def intro(self, q ,selfurl):
        self.q = q
        self.selfurl = selfurl
        print('<br><table><tr><td>')
        print('<form action="{0}" method="get">'.format(self.selfurl))
        print('<input type="hidden" name = "index" value = "{0}" >'.format(self.q['index'].value))
        print('<input type="hidden" name = "student" value = "{0}" >'.format(self.q['student'].value))
        print('<br> Название: ')
        print('<input type = "text" name = "name" value="{0}">'.format(self.name))
        print('Дата:')
        print('<input type = "text" name = "date" value="{0}">'.format(self.date))
        print('Мощность: ')
        print('<input type = "text" name = "capacity" value="{0}">'.format(self.capacity))
        print('<br><br><input type = "submit" value = "Применить">')
        print('<input type="hidden" name = "action" value = "6" >')
        print('</form></tr></td></table>')
    

    def look (self, q ,selfurl):
        self.q = q
        self.selfurl = selfurl
        if ('name' in self.q):
            self.name = self.q['name'].value
        else: self.name = ""
        if ('date' in self.q):
            self.date = self.q['date'].value
        else: self.date = ""
        if ('capacity' in self.q):
            self.capacity = self.q['capacity'].value
        else: self.capacity = ""

    def letter(self):
        print("<br>Название: {0} | Дата: {1} | Мощнсоть: {2} ".format(self.name,self.date,self.capacity))
