from .descendantClassFile import descendantClass
from .myClassFile import myClass
import pickle, cgi, cgitb, os, sys, codecs

class classContainer:
    # classList = []

    def __init__(self,q,selfurl):
        self.classList = list()
        self.q=q
        self.selfurl=selfurl

    def addClass(self):
        self.readListFromFile()
        classExemplar = myClass(self.q)
        self.classList.append(classExemplar)
        self.writeListInFile()

    def addDescendantClass(self):
        self.readListFromFile()
        classExemplar = descendantClass(self.q)
        self.classList.append(classExemplar)
        self.writeListInFile()

    def editClassParam(self):
        self.readListFromFile()
        # print('<form action="/cgi-bin/lab2.py" >')
        # print('Введите порядковый номер элемента:<input type="text" name= "i" value=""><br>')
        # print('Введите новое имя:<input type="text" name= "name" value=""><br>')
        # print('Введите новый  параметр:<input type="text" name= "param" value=""><br>')
        # print('<input  type="submit" value="Изменить" />')
        # print('<input type="hidden" name = "action" value="editClassParam" />')
        # print('<input type="hidden" name = "student" value={0} />'.format(int(self.q.getvalue('student'))))
        # print('</form>')
        # print(self.q)
        # if self.q.getvalue('action1') == 'editClassParam':
        #     self.classList[int(i)].name = (self.q.getvalue('name'))
        #     self.classList[int(i)].param =(self.q.getvalue('param'))
        #     self.writeListInFile()
        # print(self.q)
        self.writeListInFile()


    def showList(self):
        self.readListFromFile()
        print('<br>Размер массива:{0}<br>'.format(len(self.classList)))
        for i in range(0,len(self.classList)):
            print('Имя:{0}<br>'.format(self.classList[i].name))


    def readListFromFile(self):
     try:
        with open("cgi-bin/st12/1.txt", "rb") as file:
            self.classList = pickle.load(file)
     except EOFError:
        return {}


    def writeListInFile(self):
        with open("cgi-bin/st12/1.txt", "wb") as file:
            pickle.dump(self.classList, file)

    def clearList(self):
        self.readListFromFile()
        self.classList.clear()
        self.writeListInFile()