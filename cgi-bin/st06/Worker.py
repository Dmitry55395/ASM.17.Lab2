import cgi,datetime

class Worker:
    def __init__(self):
        self.type = 'Сотрудник'
        self.name = ''
        self.year = ''
        self.position = ''
        self.salary = ''

    def __str__(self):
        return '<b>{}</b><br><b>Имя:</b> {}<br><b>Год рождения:</b> {}<br><b>Должность:</b> {}<br><b>Оклад:</b> {}<br>'.format(self.type, self.name, self.year, self.position, self.salary)

    def Edit_Show(self):
        print('<tr><td>Имя</td><td><input type="text" name="name" value="{0}"></td><tr>'.format(self.name))
        print('<tr><td>Год рождения</td><td><input type="text" name="year" value="{0}"></td></tr>'.format(self.year))
        print('<tr><td>Должность</td><td><input type="text" name="position" value="{0}"></td></tr>'.format(self.position))
        print('<tr><td>Оклад</td><td><input type="text" name="salary" value="{0}"></td></tr>'.format(self.salary))
        
    def Edit_Save(self, q):
        self.name = q.getvalue('name')
        self.year = q.getvalue('year')
        self.position = q.getvalue('position')
        self.salary = q.getvalue('salary')
