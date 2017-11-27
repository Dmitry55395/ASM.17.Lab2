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
        print('<form action="/cgi-bin/lab2.py" >')
        print('Введите имя:<input type="text" name= "name" value=""><br>')
        print('Введите параметр:<input type="text" name= "param" value=""><br>')
        print('<input  type="submit" value="Создать" />')
        print('<input type="hidden" name = "secondAction" value="addclass" />')
        print('<input type="hidden" name = "student" value={0} />'.format(int(self.q.getvalue('student'))))
        print('<input type="hidden" name = "action" value="addClass" />')
        print('</form>')
        print(self.q)
        if self.q.getvalue('secondAction') == 'addclass':
            print('<br>Размер массива при добавлении:{0}<br>'.format(len(self.classList)))
            classExemplar = myClass(self.q,self.q.getvalue('name'),self.q.getvalue('param'))
            self.classList.append(classExemplar)
            self.writeListInFile()


    def addDescendantClass(self):
        self.readListFromFile()
        print('<form action="/cgi-bin/lab2.py" >')
        print('Введите имя:<input type="text" name= "name" value=""><br>')
        print('Введите параметр:<input type="text" name= "param" value=""><br>')
        print('Введите дополнительный параметр:<input type="text" name= "additionalAttribute" value=""><br>')
        print('Введите второй дополнительный параметр:<input type="text" name= "secondAdditionalAttribute" value=""><br>')
        print('<input  type="submit" value="Создать" />')
        print('<input type="hidden" name = "secondAction" value="addDescendantClass" />')
        print('<input type="hidden" name = "student" value={0} />'.format(int(self.q.getvalue('student'))))
        print('<input type="hidden" name = "action" value="addDescendantClass" />')
        print('</form>')
        print(self.q)
        if self.q.getvalue('secondAction') == 'addDescendantClass':
            print('<br>Размер массива при добавлении:{0}<br>'.format(len(self.classList)))
            classExemplar = descendantClass(self.q, self.q.getvalue('name'), self.q.getvalue('param'),self.q.getvalue('additionalAttribute'),self.q.getvalue('secondAdditionalAttribute'))
            self.classList.append(classExemplar)
            self.writeListInFile()

    def editClassParam(self):
        self.readListFromFile()
        print('<form action="/cgi-bin/lab2.py" >')
        print('Введите имя:<input type="text" name= "name" value=""><br>')
        print('Введите параметр:<input type="text" name= "param" value=""><br>')
        print('Введите номер элемента:<input type="text" name= "number" value=""><br>')
        print('<input  type="submit" value="Редактировать" />')
        print('<input type="hidden" name = "secondAction" value="editClassParam" />')
        print('<input type="hidden" name = "student" value={0} />'.format(int(self.q.getvalue('student'))))
        print('<input type="hidden" name = "action" value="editClassParam" />')
        print('</form>')
        print(self.q)
        if self.q.getvalue('secondAction') == 'editClassParam':
            print('<br>Размер массива при добавлении:{0}<br>'.format(len(self.classList)))
            self.classList[int(self.q.getvalue('number'))].name = (self.q.getvalue('name'))
            self.classList[int(self.q.getvalue('number'))].param = (self.q.getvalue('param'))
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