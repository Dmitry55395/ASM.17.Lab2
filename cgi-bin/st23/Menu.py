class Menu:
    EXIT_CODE: int = 6

    def __init__(self, university, url, student_id):
        self.university = university
        self.instance = self.get()
        self.url = url
        self.student_id = student_id

    def get(self):
        return [
            ['Добавить студента', self.university.add_student],
            ['Добавить преподавателя', self.university.add_teacher],
            ['Редактировать университет', self.university.edit],
            ['Показать список людей', self.university.show_people],
            ['Очистить', self.university.clear_men]
        ]

    # если student_id == None, то возвращаем на стартовую страницу курса
    # иначе на мою стартовую страницу
    @staticmethod
    def back_button(url, student_id=None):
        if student_id is None:
            print('<a href="{0}">Назад</a>'.format(url))
        else:
            print('<a href="{0}?student={1}">Назад</a>'.format(url, student_id))

    def show_menu(self, self_url, student_id):
        print('<pre>------------------------------')
        for i, item in enumerate(self.instance):
            print('<a href="{0}?student={1}&act={3}">[{3}] {2}</a>'.format(self_url, student_id, item[0], i))
        Menu.back_button(self.url)
        print("------------------------------</pre>")

    @staticmethod
    def not_found():
        print('<html><head></head><body><h1>404 Not Found</h1></body></html>')

    @staticmethod
    def response_ok():
        print("Content-type: text/html; charset=utf-8\n\n")

    def start(self, index):
        try:
            if index != Menu.EXIT_CODE:
                self.instance[index][1]()
        except IndexError:
            Menu.not_found()
