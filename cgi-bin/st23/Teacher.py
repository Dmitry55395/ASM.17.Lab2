from .Student import Student


# Класс учителя, который вырос из студента
class Teacher(Student):
    params = Student.params + ['workplace', 'salary']
    placeholder = Student.placeholder + ['Место работы', 'Зарплата']

    def __init__(self, self_url, q):
        Student.__init__(self, self_url, q)
        self.type = 'Преподаватель'
        self.url = self_url
        self.q = q
        self.degree: str = ''  # звание преподавателя
        self.workplace: str = ''  # место работы
        self.salary: int = 1000  # размер зарплаты
