import pickle, cgi, os
from .Fired import *

class Company:
    def __init__(self, q, selfurl):
        self.company = []
        self.q = q
        self.selfurl = selfurl

    def Add_Worker(self):
        worker = Worker()
        self.company.append(worker)
        self.Write_File()
        self.Edit_Worker()

    def Add_Fired(self):
        worker = Fired()
        self.company.append(worker)
        self.Write_File()
        self.Edit_Worker()

    def Show_List(self):
        i = 0
        for worker in self.company:
            print('<br>')
            print(worker)
            print('<a href={0}?student={1}&act=edit&id={2}>Редактировать</a> <a href={0}?student={1}&act=delete&id={2}>Удалить</a><br>'.format(self.selfurl, self.q.getvalue('student'), i))
            i+=1
        print('<input type="hidden" name="student" value={0} />'.format(self.q.getvalue('student')))
        print('<input type="hidden" name="act" value="show" /><br>')
        print('<p><a href={0}?student={1}&act=addworker>Добавить сотрудника</a>'.format(self.selfurl, self.q.getvalue('student')))
        print('<p><a href={0}?student={1}&act=addfired>Добавить бывшего сотрудника</a>'.format(self.selfurl, self.q.getvalue('student')))
        print('<p><a href={0}?student={1}&act=clear>Очистить список</a>'.format(self.selfurl, self.q.getvalue('student')))
        print('<a href={0}>Назад</a>'.format(self.selfurl))

    def Save_Info(self):
        self.Read_File()
        self.company[int(self.q.getvalue('id'))].Edit_Save(self.q)
        self.Write_File()
        self.Show_List()

    def Edit_Worker(self):
        print('<form>')
        print('<input type="hidden" name="student" value="{0}" />'.format(self.q.getvalue('student')))
        print('<input type="hidden" name="act" value="save" />')
        if 'id' in self.q:
            wid = self.q.getvalue('id')
        else:
            wid = str(len(self.company)-1)
        print('<input type="hidden" name="id" value="{0}" />'.format(wid))
        print('<table>')
        self.company[int(wid)].Edit_Show()
        print('</table>')
        print('<input type="submit" value="Сохранить">')
        print('</form>')

    def Write_File(self):
        pickle.dump(self.company, open('cgi-bin/st06/file.dat', 'wb'))

    def Read_File(self):
        if (os.path.exists('cgi-bin/st06/file.dat')):
            self.company = pickle.load(open('cgi-bin/st06/file.dat', 'rb'))

    def Delete_Worker(self):
        self.company.pop(int(self.q.getvalue('id')))
        self.Show_List()

    def Clear_List(self):
        self.company.clear()
        self.Show_List()





