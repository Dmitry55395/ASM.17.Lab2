import cgi

class Student:
    def __init__(self):
        self.name = ''
        self.age = ''
        self.year = ''
        self.payment = ''
        
    def Write(self):
        print('<td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td><td>{5}</td>'.format(self.name, self.age, self.year, self.payment, '-', '-'))

    def ShowEdit(self):
        print('<tr><td>Имя:</td><td><input type="text" name="name" value="{0}"></td><tr>'.format(self.name))
        print('<tr><td>Возраст:</td><td><input type="text" name="age" value="{0}"></td></tr>'.format(self.age))
        print('<tr><td>Курс:</td><td><input type="text" name="year" value="{0}"></td></tr>'.format(self.year))
        print('<tr><td>Тип оплаты:</td><td><input type="text" name="payment" value="{0}"></td></tr>'.format(self.payment))
        
    def SaveEdit(self, q):
        self.name = q.getvalue('name')
        self.age = q.getvalue('age')
        self.year = q.getvalue('year')
        self.payment = q.getvalue('payment')
