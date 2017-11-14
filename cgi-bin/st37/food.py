

class food:
    def __init__(self):
        self.name =""
        self.quantity =""
        self.calories=""
        
      
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
        print('<br><br><input type = "submit" value = "Применить">')
        print('<input type="hidden" name = "j" value = "ok" >')
        print('</form></tr></td></table>')
        
    def vvod (self, q, selfurl):
        self.q = q
        self.selfurl = selfurl
        if ('name' in self.q):
            self.name = self.q['name'].value
        else: self.name = ""
        if ('quantity' in self.q):
            self.quantity = self.q['quantity'].value
        else: self.quantity = ""
        if ('calories' in self.q):
            self.calories = self.q['calories'].value
        else: self.calories = ""
        

        
       
        
    def vyvod(self):
        print("<br>Название: {0} <br> Количество блюд: {1} <br> Каллорий в одной порции: {2} ".format(self.name, self.quantity, self.calories))

