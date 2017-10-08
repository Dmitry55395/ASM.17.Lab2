import pickle, os
from .used import *

class Catalog:
    
    def __init__(self, q, selfurl):
        self.catalog = []
        self.q = q
        self.selfurl = selfurl
        
    def show(self):
        print('<table border cellspacing="0"><tr align="center"><td>Название</td><td>Год выпуска</td><td>Цвет</td><td>Кол-во владельцев</td><td>Пробег</td><td>Опции</td></tr>')
        i = 0
        for item in self.catalog:
            print('<br>')
            item.show()
            print('<td><a href={0}?student={1}&act=edit&id={2}>Редактировать</a><br><a href={0}?student={1}&act=delete&id={2}>Удалить</a></td></tr></tr>'.format(self.selfurl, self.q.getvalue('student'), i))
            i += 1
        print('</table><br>')
        print('<a href={0}?student={1}&act=addnew>Добавить новый автомобиль</a><br>'.format(self.selfurl, self.q.getvalue('student')))
        print('<a href={0}?student={1}&act=addused>Добавить подержанный автомобиль</a><br>'.format(self.selfurl, self.q.getvalue('student')))
        print('<a href={0}?student={1}&act=clear>Очистить список</a><br>'.format(self.selfurl, self.q.getvalue('student')))
        print('<a href={0}>Назад</a>'.format(self.selfurl))

    def get(self):
        self.load()
        self.catalog[int(self.q.getvalue('id'))].get(self.q)
        self.save()
        self.show()

    def add_new(self):
        auto = Auto()
        self.catalog.append(auto)
        self.save()
        self.edit_catalog()

    def add_used(self):
        self.load()
        auto = Used()
        self.catalog.append(auto)
        self.save()
        self.edit_catalog()

    def edit_catalog(self):
        self.load()
        print("""<form>
<input type="hidden" name="student" value="{}" />
<input type="hidden" name="act" value="get" />""".format(self.q.getvalue('student')))
        sid = str()
        if 'id' in self.q:
            sid = self.q.getvalue('id')
        else:
            sid = str(len(self.catalog)-1)
        print('<input type="hidden" name="id" value="{}" />'.format(sid))
        print('<table>')
        self.catalog[int(sid)].edit()
        print('</table> <P></P>')
        print('<input type="submit" value="Сохранить изменения"></form>')

    def delete_auto(self):
        self.catalog.pop(int(self.q.getvalue('id')))
        self.show()

    def clear_catalog(self):
        self.catalog.clear()
        self.show()

    def save(self):
        pickle.dump(self.catalog, open('cgi-bin/st24/catalog.dat', 'wb'))

    def load(self):
        if (os.path.exists('cgi-bin/st24/catalog.dat')):
            self.catalog = pickle.load(open('cgi-bin/st24/catalog.dat', 'rb'))
        
