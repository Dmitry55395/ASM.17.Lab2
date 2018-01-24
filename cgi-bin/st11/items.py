import pickle, copy, os
from .category import *
from .dish import *

class Items:
    def __init__(self, q, selfurl):
       self.it=list()
       self.q = q
       self.selfurl = selfurl


    def f(self):
        print(self.selfurl)
        print('<a href="{0}?student={1}&lol={2}">{3}</a>'.format(self.selfurl, self.q['student'].value))
        print(self.q)

    def read(self):
        self.read_file()
        if ('type' in self.q):       
            if (self.q['type'].value!="3"):
                if (self.q['type'].value=="1"): Category(self.q, self.selfurl).write_ch()
                if (self.q['type'].value=="2"): Dish(self.q, self.selfurl).write_ch()
                if (self.q['type'].value=="4"): self.it[int(self.q['id'].value)].write_ch()
                print('<br><br><input type="submit" value="Сохранить">')
                print('</form>')
            else:
                if (len(self.it)==int(self.q['id'].value)):
                    if (self.q['add'].value=="1"): self.it.append(Category(self.q, self.selfurl))
                    if (self.q['add'].value=="2"): self.it.append(Dish(self.q, self.selfurl))
                self.it[int(self.q['id'].value)].read()
                self.write_file()
                self.write()
        else:
            k=len(self.it)
            print('<a href="{0}?student={1}&action=1&type=1&id={2}">Категория</a> или <a href="{0}?student={1}&action=1&type=2&id={2}">Блюдо</a>'.format(self.selfurl, self.q['student'].value, k))

    def write(self):
        self.read_file()
        if (len(self.it)!=0):
            print('<table><Caption><H3>Меню</H3></Caption><tr><td>Название категории</td><td>Название блюда</td><td>Цена</td><td>Вес</td><td>Действие</td></tr>')
            i=0
            for o in self.it:
                print('<tr height="20">')
                o.write()
                if type(o) is Category: print('<td>---</td><td>---</td><td>---</td>')
                print('<td><a href="{0}?student={1}&action=1&type=4&id={2}">Редактировать</a> | <a href="{0}?student={1}&action=3&id={2}">Удалить</a></td>'.format(self.selfurl, self.q['student'].value,i))
                print('</tr>')
                i+=1
            print('</table>')
        print('<br><br><a href="{0}">Назад</a> | <a href="{0}?student={1}&action=1">Добавить</a>'.format(self.selfurl, self.q['student'].value))

    def delete(self):
        self.read_file()
        self.l.pop(int(self.q['id'].value))
        self.write_file()
        self.write()       
            
       
    def read_file(self):
        try:
            if (os.path.exists("cgi-bin/st11/file.txt")):
                self.it = pickle.load(open("cgi-bin/st11/file.txt", "rb"))
        except EOFError:
            return {}

    def write_file(self):
        pickle.dump(self.it, open("cgi-bin/st11/file.txt", "wb"))
