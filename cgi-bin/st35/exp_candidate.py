from .candidate import *

class Exp_Candidate(Candidate):
    """Класс, описывающий соскателя c опытом работы"""
    def __init__(self, q, selfurl):
        self.q = q
        self.selfurl = selfurl
        super().__init__(q, selfurl)
        self.experience = ""
        self.last_job = ""

    # метод считывания данных с заполненных полей формы и последующей записью в атрибуты объекта класса EXP_Candidate
    def form_read(self):
        Candidate.form_read(self)

        if ('experience' in self.q):
            self.experience = self.q['experience'].value
        else: self.experience = ""

        if ('last_job' in self.q):
            self.last_job = self.q['last_job'].value
        else: self.last_job = ""

    # метод описывает как будет выглядеть форма добавления соискателя с опытом работы
    def form_format(self):
        Candidate.form_format(self)
        print('<br>Опыт работы:<br><input type="text" name="experience" value="{0}">'.format(self.experience))
        print('<br>Последнее место работы:<br><input type="text" name="last_job" value="{0}">'.format(self.last_job))

    # метод, описывающий как будут отображаться считанные данные в таблице
    def form_output(self):
        Candidate.form_output(self)
        print('<td>{0}</td>'.format(self.experience))
        print('<td>{0}</td>'.format(self.last_job))
