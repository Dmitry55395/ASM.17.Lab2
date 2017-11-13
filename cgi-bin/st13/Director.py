from .Person import Person


# Класс руководителя, расширяющий класс сотрудника
class Director(Person):
    params = Person.params + ['workplace', 'salary']
    placeholder = Person.placeholder + ['Место работы', 'Зарплата']

    def __init__(self, self_url, q):
        Person.__init__(self, self_url, q)
        self.type = 'Руководитель'
        self.url = self_url
        self.q = q
        self.degree: str = ''  # должность руководителя
        self.workplace: str = ''  # место работы
        self.salary: int = 1000  # размер зарплаты
