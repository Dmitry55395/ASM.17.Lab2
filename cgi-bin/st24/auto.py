class Auto:

    def __init__(self):
        self.name = ''
        self.year = ''
        self.color = '' 

    def show(self):
        print('<td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td>'.format(self.name, self.year, self.color, '-', '-'))

    def edit(self):
        print('<tr><td>Название:</td><td><input type="text" name="name" value="{}"></td><tr>'.format(self.name))
        print('<tr><td>Год выпуска:</td><td><input type="text" name="year" value="{}"></td></tr>'.format(self.year))
        print('<tr><td>Цвет:</td><td><input type="text" name="color" value="{}"></td></tr>'.format(self.color))
    
    def get(self, q): 
        self.name = q.getvalue('name')
        self.year = q.getvalue('year')
        self.color = q.getvalue('color')
