class Warrior:

    def __init__(self):
        
        self.name = ""
        self.health = ""
        self.attack = ""

    def tbl(self, q ,selfurl):
        self.q = q
        self.selfurl = selfurl
        print('<br><table><tr><td>')
        print('<form action="{0}" method="get">'.format(self.selfurl))
        print('<input type="hidden" name = "index" value = "{0}" >'.format(self.q['index'].value))
        print('<input type="hidden" name = "student" value = "{0}" >'.format(self.q['student'].value))
        print('<br> Имя: ')
        print('<input type = "text" name = "name" value="{0}">'.format(self.name))
        print('Здоровье:')
        print('<input type = "text" name = "health" value="{0}">'.format(self.health))
        print('Атака: ')
        print('<input type = "text" name = "attack" value="{0}">'.format(self.attack))
        print('<br><br><input type = "submit" value = "Применить">')
        print('<input type="hidden" name = "action" value = "6" >')
        print('</form></tr></td></table>')
    

    def read(self, q ,selfurl):
        self.q = q
        self.selfurl = selfurl
        if ('name' in self.q):
            self.name = self.q['name'].value
        else: self.name = ""
        if ('health' in self.q):
            self.health = self.q['health'].value
        else: self.health = ""
        if ('attack' in self.q):
            self.attack = self.q['attack'].value
        else: self.attack = ""

    def write(self):
        print("<br>Имя: {0} | Здоровье: {1} | Атака: {2} ".format(self.name,self.health,self.attack))

    

