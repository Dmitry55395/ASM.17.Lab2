class Car:

    def __init__(self):
        
        self.model = ""
        self.type = ""
        self.color = ""

    def tbl(self, q ,selfurl):
        self.q = q
        self.selfurl = selfurl
        print('<br><table><tr><td>')
        print('<form action="{0}" method="get">'.format(self.selfurl))
        print('<input type="hidden" name = "index" value = "{0}" >'.format(self.q['index'].value))
        print('<input type="hidden" name = "student" value = "{0}" >'.format(self.q['student'].value))
        print('<br> Model: ')
        print('<input type = "text" name = "model" value="{0}">'.format(self.model))
        print('Type:')
        print('<input type = "text" name = "type" value="{0}">'.format(self.type))
        print('Color: ')
        print('<input type = "text" name = "color" value="{0}">'.format(self.color))
        print('<br><br><input type = "submit" value = "Применить">')
        print('<input type="hidden" name = "action" value = "6" >')
        print('</form></tr></td></table>')
    

    def read(self, q ,selfurl):
        self.q = q
        self.selfurl = selfurl
        if ('model' in self.q):
            self.model = self.q['model'].value
        else: self.model = ""
        if ('type' in self.q):
            self.type = self.q['type'].value
        else: self.type = ""
        if ('color' in self.q):
            self.color = self.q['color'].value
        else: self.color = ""

    def write(self):
        print("<br>Model: {0} | Type: {1} | Color: {2} ".format(self.model,self.type,self.color))

    

