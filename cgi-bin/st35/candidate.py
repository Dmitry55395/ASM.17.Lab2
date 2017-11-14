import cgi
class Candidate:
    """Класс, описывающий соскателя без опыта работы"""
    def __init__(self, q, selfurl):
        self.q = q
        self.selfurl = selfurl
        self.first_name = ""
        self.last_name = ""
        self.gender = ""
        self.age = ""
        self.mail = ""

    # метод считывания данных с заполненных полей формы и последующей записью в атрибуты объекта класса Candidate
    def form_read(self):
        self.q = cgi.FieldStorage()

        if ('first_name' in self.q):
            self.first_name = self.q['first_name'].value
        else: self.first_name = ""

        if ('last_name' in self.q):
            self.last_name = self.q['last_name'].value
        else: self.last_name = ""

        if ('gender' in self.q):
            self.gender = self.q['gender'].value
        else: self.gender = ""

        if ('age' in self.q):
            self.age = self.q['age'].value
        else: self.age = ""

        if ('mail' in self.q):
            self.mail = self.q['mail'].value
        else: self.mail = ""

    # метод описывает как будет выглядеть форма добавления соискателя без опыта работы
    def form_format(self):
        self.q = cgi.FieldStorage()
        self.q.getfirst("id", "--")
        print('<form action="{0}?student={1}&action=1&type=3&id={2}&add={3}">'.format(self.selfurl, self.q['student'].value, self.q['id'].value, self.q['type'].value))

        print('<input type="text" name="student" value="{0}" style="display:none">'.format(self.q['student'].value))
        print('<input type="text" name="action" value="{0}" style="display:none">'.format("1"))
        print('<input type="text" name="type" value="{0}" style="display:none">'.format("3"))
        print('<input type="text" name="id" value="{0}" style="display:none">'.format(self.q['id'].value))
        print('<input type="text" name="add" value="{0}" style="display:none">'.format(self.q['type'].value))

        print('Имя:<br><input type="text" name="first_name" value="{0}">'.format(self.first_name))
        print('<br>Фамилия:<br><input type="text" name="last_name" value="{0}">'.format(self.last_name))
        print('<br>Пол:<br><input type="text" name="gender" value="{0}">'.format(self.gender))
        print('<br>Возраст:<br><input type="text" name="age" value="{0}">'.format(self.age))
        print('<br>E-mail:<br><input type="text" name="mail" value="{0}">'.format(self.mail))

    # метод, описывающий как будут отображаться считанные данные в таблице
    def form_output(self):
        print('<td>{0}</td>'.format(self.first_name))
        print('<td>{0}</td>'.format(self.last_name))
        print('<td>{0}</td>'.format(self.gender))
        print('<td>{0}</td>'.format(self.age))
        print('<td>{0}</td>'.format(self.mail))
