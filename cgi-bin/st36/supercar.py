from .car import *

class Supercar(Car):
    def __init__(self):
        super().__init__()
        self.nitro = ""
        self.modification = ""


    def tbl(self, q ,selfurl):
        self.q = q
        self.selfurl = selfurl
        print('<br><table><tr><td>')
        print('<form action="{0}" method="get">'.format(self.selfurl))
        print('<input type="hidden" name = "index" value = "{0}" >'.format(self.q['index'].value))
        print('<input type="hidden" name = "student" value = "{0}" >'.format(self.q['student'].value))
        print('<br> Model:')
        print('<input type = "text" name = "name" value="{0}">'.format(self.model))
        print('Type:')
        print('<input type = "text" name = "health" value="{0}">'.format(self.type))
        print('Color:')
        print('<input type = "text" name = "attack" value="{0}">'.format(self.color))
        print('Nitro:')
        print('<input type = "text" name = "mana" value="{0}">'.format(self.nitro))
        print('Modification:')
        print('<input type = "text" name = "spell" value="{0}">'.format(self.modification))
        print('<br><br><input type = "submit" value = "Apply">')
        print('<input type="hidden" name = "action" value = "7" >')
        print('</form></tr></td></table>')


    def read(self, q ,selfurl):
        super().read(q ,selfurl)
        if ('nitro' in self.q):
            self.nitro = self.q['nitro'].value
        else: self.nitro = ""
        if ('modification' in self.q):
            self.modification = self.q['modification'].value
        else: self.modification = ""


    def write(self):
        print("<br>Model: {0} | Type: {1} | Color: {2} | Nitro: {3} | Modification: {4}".format(self.model, self.type, self.color, self.nitro, self.modification))

