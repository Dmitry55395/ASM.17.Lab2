import pickle, cgi, os
from .Undergraduate import *

class Group:
    def __init__(self, q, selfurl):
        self.group = []
        self.q = q
        self.selfurl = selfurl

    def AddStudent(self):
        print('<form>')
        print('<input type="hidden" name="student" value="{0}" />'.format(self.q.getvalue('student')))
        print('<input type="hidden" name="act" value="get" />')
        print('<input type="hidden" name="id" value="addstudent" />')
        print('<table>')
        Student().ShowEdit()
        print('</table>')
        print('<input type="submit" value="Сохранить">')
        print('</form>')

    def AddUndergraduate(self):
        print('<form>')
        print('<input type="hidden" name="student" value="{0}" />'.format(self.q.getvalue('student')))
        print('<input type="hidden" name="act" value="get" />')
        print('<input type="hidden" name="id" value="addundergraduate" />')
        print('<table>')
        Undergraduate().ShowEdit()
        print('</table>')
        print('<input type="submit" value="Сохранить">')
        print('</form>')

    def ShowList(self):
        print('<table border cellspacing="0"><tr align="center" bgcolor="#99ff66"><td>Имя</td><td>Возраст</td><td>Курс</td><td>Тип оплаты</td><td>Науч. рук.</td><td>Тема диплома</td><td></td></tr>')
        i = 0
        for item in self.group:
            print('<br>')
            item.Write()
            print('<td><a href={0}?student={1}&act=edit&id={2}>Редактировать</a><br><a href={0}?student={1}&act=delete&id={2}>Удалить</a></td></tr></tr>'.format(self.selfurl, self.q.getvalue('student'), i))
            #print('<br>')
            i += 1
        print('</table><br>')
        print('<a href={0}?student={1}&act=addstudent>Добавить студента</a><br>'.format(self.selfurl, self.q.getvalue('student')))
        print('<a href={0}?student={1}&act=addundergraduate>Добавить старшекурсника</a><br>'.format(self.selfurl, self.q.getvalue('student')))
        print('<a href={0}?student={1}&act=clear>Очистить список</a><br>'.format(self.selfurl, self.q.getvalue('student')))
        print('<a href={0}>Назад</a>'.format(self.selfurl))

    def Get(self):
        if self.q.getvalue('id') == 'addstudent':
            student = Student()
            student.SaveEdit(self.q)
            self.group.append(student)
        elif self.q.getvalue('id') == 'addundergraduate':
            student = Undergraduate()
            student.SaveEdit(self.q)
            self.group.append(student)
        else:
            self.group[int(self.q.getvalue('id'))].SaveEdit(self.q)
        self.ShowList()

    def Edit(self):
        print('<form>')
        print('<input type="hidden" name="student" value="{0}" />'.format(self.q.getvalue('student')))
        print('<input type="hidden" name="act" value="get" />')
        iid = self.q.getvalue('id')
        print('<input type="hidden" name="id" value="{0}" />'.format(iid))
        print('<table>')
        self.group[int(iid)].ShowEdit()
        print('</table>')
        print('<input type="submit" value="Сохранить">')
        print('</form>')

    def Save(self):
        pickle.dump(self.group, open('cgi-bin/st07/file.dat', 'wb'))

    def Load(self):
        if (os.path.exists('cgi-bin/st07/file.dat')):
            self.group = pickle.load(open('cgi-bin/st07/file.dat', 'rb'))

    def Delete(self):
        self.group.pop(int(self.q.getvalue('id')))
        self.ShowList()

    def Clear(self):
        self.group.clear()
        self.ShowList()
