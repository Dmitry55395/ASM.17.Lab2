from .warrior import *

class Mage(Warrior):
    def __init__(self):
        super().__init__()
        self.mana = ""
        self.spell = ""


    def tbl(self, q ,selfurl):
        self.q = q
        self.selfurl = selfurl
        print('<br><table><tr><td>')
        print('<form action="{0}" method="get">'.format(self.selfurl))
        print('<input type="hidden" name = "index" value = "{0}" >'.format(self.q['index'].value))
        print('<input type="hidden" name = "student" value = "{0}" >'.format(self.q['student'].value))
        print('<br> Имя:')
        print('<input type = "text" name = "name" value="{0}">'.format(self.name))
        print('Здоровье:')
        print('<input type = "text" name = "health" value="{0}">'.format(self.health))
        print('Атака:')
        print('<input type = "text" name = "attack" value="{0}">'.format(self.attack))
        print('Мана:')
        print('<input type = "text" name = "mana" value="{0}">'.format(self.mana))
        print('Заклинание:')
        print('<input type = "text" name = "spell" value="{0}">'.format(self.spell))
        print('<br><br><input type = "submit" value = "Применить">')
        print('<input type="hidden" name = "action" value = "7" >')
        print('</form></tr></td></table>')


    def read(self, q ,selfurl):
        super().read(q ,selfurl)
        if ('mana' in self.q):
            self.mana = self.q['mana'].value
        else: self.mana = ""
        if ('spell' in self.q):
            self.spell = self.q['spell'].value
        else: self.spell = ""


    def write(self):
        print("<br>Имя: {0} | Здоровье: {1} | Атака: {2} | Мана: {3} | Заклинание: {4}".format(self.name, self.health, self.attack, self.mana, self.spell))

