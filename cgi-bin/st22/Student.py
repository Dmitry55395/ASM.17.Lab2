# Класс студента
class Student:
    params = ['first_name', 'last_name', 'age']
    placeholder = ['Имя', 'Фамилия', 'Возраст']

    def __init__(self, self_url, q):
        self.url = self_url
        self.q = q
        self.first_name: str = ''  # имя
        self.last_name: str = ''  # фамилия
        self.age: int = 18  # возраст
        self.type: str = 'Студент'

    def save(self):
        for param in self.params:
            if param in self.q:
                setattr(self, param, self.q.getvalue(param))

    def __str__(self):
        naming = self.type + ' '
        for ind, param in enumerate(self.params):
            naming += '{0}: {1} '.format(self.placeholder[ind], getattr(self, param))
        return naming + '</br>'
