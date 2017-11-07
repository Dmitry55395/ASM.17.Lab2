from .Guests import *
from .Registered import *
import pickle, cgi, cgitb, codecs, sys, os, datetime
cgitb.enable()


def loadTpl(nameTpl):
    docrootname = 'PATH_TRANSLATED'
    with open(os.environ[docrootname] + '/cgi-bin/st02/tpl/' + nameTpl + '.tpl', 'r') as f:
        return f.read()

#format(**self.__dict__))

class Library:
    """Класс контейнер - библиотека"""
    def __init__(self, q, selfurl):
        self.l = list()
        self.q = q
        self.selfurl = selfurl
        self.id_count = 0

    def readFromFile(self):
        if (os.path.exists('cgi-bin/st02/file.db')):
            self.l.clear()
            with open('cgi-bin/st02/file.db', 'rb') as f:
                self.l = pickle.load(f)
            if self.l:
                self.id_count = int(self.l[-1].id) + 1

    def writeToFile(self):
        with open('cgi-bin/st02/file.db', 'wb') as f:
            pickle.dump(self.l, f)

    def showForm(self):
        print (loadTpl('menu').format(self.selfurl, self.q.getvalue('student')))
        for item in self.l:
 #           item.q = self.q
            item.show()
        print ('</table>')
        
    def addGuest(self):
        guest = Guest(self.q, self.selfurl)
        guest.add()
        
    def addReg(self):
        reg = Registered(self.q, self.selfurl)
        reg.add()
        
    def edit_student(self):
        id = self.q.getvalue('id')
        for item in self.l:
            if int(item.id) == int(id):
                item.edit()

    def save_student(self):
        id = int(self.q.getvalue('id'))
        #print(str(id))
        if id == -1:
            if self.q.getvalue('obj') == '1':
                obj = Guest(self.q, self.selfurl)
            else:
                obj = Registered(self.q, self.selfurl)
            obj.save(self.id_count)
            self.l.append(obj)
            self.id_count += 1
        else:
            for item in self.l:
                #print('---'+item.id+'---')
                if item.id == id:
 #                   print("!!!")
                    item.q = self.q
                    item.save(int(self.q.getvalue('id')))

        self.showForm()

    def delete(self):
        id = self.q.getvalue('id')
        for item in self.l:
            if str(item.id) == id:
                self.l.remove(item)
                self.showForm()

    def clear(self):
        self.l.clear()
        self.showForm()
        

    
