from .exp_candidate import *
import pickle


class Data_Base:
    def __init__(self, q, selfurl):
        self.q = q
        self.selfurl = selfurl
        self.l = list()

    def read(self):
        self.read_file()
        if ('type' in self.q):
            if (self.q['type'].value != "3"):
                if (self.q['type'].value == "1"):
                    Candidate(self.q, self.selfurl).form_format()
                if (self.q['type'].value == "2"):
                    Exp_Candidate(self.q, self.selfurl).form_format()
                if (self.q['type'].value == "4"):
                    self.l[int(self.q['id'].value)].form_format()
                print('<br><br><input type="submit" value="Сохранить">')
                print('</form>')
            else:
                if (len(self.l) == int(self.q['id'].value)):
                    if (self.q['add'].value == "1"):
                        self.l.append(Candidate(self.q, self.selfurl))
                    if (self.q['add'].value == "2"):
                        self.l.append(Exp_Candidate(self.q, self.selfurl))
                self.l[int(self.q['id'].value)].form_read()
                self.write_file()
                self.write()
        else:
            k = len(self.l)
            print('<a href="{0}?student={1}&action=1&type=1&id={2}">Без опыта работы</a> | <a href="{0}?student={1}&action=1&type=2&id={2}">С опытом работы</a>'.format(self.selfurl, self.q['student'].value, k))

    def write(self):
        self.read_file()
        if (len(self.l) != 0):
            print('<table border><Caption><H3>Список соискателей</H3></Caption><tr><td>Имя</td><td>Фамилия</td><td>Пол</td><td>Возраст</td><td>E-mail</td><td>Опыт работы</td><td>Предыдущее место работы</td><td>Действие</td></tr>')
            i = 0
            for element in self.l:
                print('<tr height="20">')
                element.form_output()
                if type(element) is Candidate:
                    print('<td>-----</td><td>-----</td>')
                print('<td><a href="{0}?student={1}&action=1&type=4&id={2}">Редактировать</a> | <a href="{0}?student={1}&action=3&id={2}">Удалить</a></td>'.format(self.selfurl, self.q['student'].value, i))
                print('</tr>')
                i += 1
            print('</table>')
        print('<br><br><a href="{0}">Назад</a> | <a href="{0}?student={1}&action=1">Добавить соискателей</a>'.format(self.selfurl, self.q['student'].value))

    def delete(self):
        self.read_file()
        self.l.pop(int(self.q['id'].value))
        self.write_file()
        self.write()


    def read_file(self):
        try:
            with open('cgi-bin/st13/pickledata.dat', "rb") as f:
                self.l = pickle.load(f)
        except EOFError:
            return {}

    def write_file(self):
        try:
            with open('cgi-bin/st13/pickledata.dat', "wb")as f:
                pickle.dump(self.l, f)
        except EOFError:
            return {}
