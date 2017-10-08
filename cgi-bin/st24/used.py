from .auto import *

class Used(Auto):

    def __init__(self):
        super().__init__()
        self.owners = ''
        self.mileage = ''

    def get(self, q):
        super().get(q)
        self.owners = q.getvalue('owners')
        self.mileage = q.getvalue('mileage')

    def edit(self):
        super().edit()
        print('<tr><td>Кол-во владельцев:</td><td><input type="text" name="owners" value="{}"></td><tr>'.format(self.owners))
        print('<tr><td>Пробег:</td><td><input type="text" name="mileage" value="{}"></td></tr>'.format(self.mileage))
        
    def show(self):
        print('<td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td>'.format(self.name, self.year, self.color, self.owners, self.mileage))


