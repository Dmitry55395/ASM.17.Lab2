from .developed_rig import *
import pickle
import  cgi

class Platform:
    
    FILENAME = "cgi-bin/st42/file.txt"
    atribut = []
    
    def __init__(self, q, selfurl):
        self.q = q
        self.selfurl = selfurl
        pass
        
    def intro(self):
        #self.wrtf()
        self.rff()
             
        print('<table>')
        print("<tr>")
        print("<td><a href = {0}?action=2&index=-1&student={1}> Добавить оборудование</a></td>".format(self.selfurl, self.q['student'].value))
        print("<td><a href = {0}?action=3&index=-1&student={1}> Добавить обновленнное оборудование</a></td>".format(self.selfurl, self.q['student'].value))
        print("<td><a href = {0}?action=1&student={1}> Показать список</a></td>".format(self.selfurl, self.q['student'].value))
        print("<td><a href = {0}?action=8&student={1}> Очистить список</a></td>".format(self.selfurl, self.q['student'].value))
        print("<td><a href = {0}?action=0> В главное меню</a></td>".format(self.selfurl))
        print("</tr>")
        print("</table>")


    def show_atribut(self):
        print('<br><br><h1>Атрибут оборудований<br><br>')
        for i in self.atribut:
            print("   {0}-ое оборудование".format(self.atribut.index(i) + 1))
            i.letter()
            print("<br><a href = {0}?action=4&index={1}&student={2}> Редактировать</a> / ".format(self.selfurl, self.atribut.index(i), self.q['student'].value))
            print("<a href = {0}?action=5&index={1}&student={2}>Удалить<br><br></a>".format(self.selfurl, self.atribut.index(i), self.q['student'].value))
        if len(self.atribut) == 0:
            print("<br>Атрибут пустой<br></h1>")

    def adding(self):
        self.rff()
        if self.q["action"].value == "2":
            Drilling_rig().intro(self.q, self.selfurl)
        elif self.q["action"].value == "3":
            Developed_rig().intro(self.q, self.selfurl)
        elif self.q["action"].value == "6":
            drilling_rig = Drilling_rig()
            drilling_rig.look(self.q, self.selfurl)
            self.atribut.append(drilling_rig)
        elif self.q["action"].value == "7":
            drilling_rig = Developed_rig()
            drilling_rig.look(self.q, self.selfurl)
            self.atribut.append(drilling_rig)
        elif self.q["action"].value == "5":
            self.atribut.pop(int(self.q["index"].value))
        self.wrtf()
        self.show_atribut()

    def edit(self):
        self.rff()      
        if self.q["action"].value == "4":
            self.atribut[int(self.q["index"].value)].intro(self.q, self.selfurl)
        elif (self.q["action"].value == "6") or (self.q["action"].value == "7"):
            self.atribut[int(self.q["index"].value)].look(self.q,self.selfurl)
        self.wrtf()
        self.show_atribut()
        
    def clear_atribut(self):
        self.rff()
        self.atribut.clear()
        self.wrtf()

        
    def wrtf(self):
        pickle_out = open(Platform.FILENAME,"wb")
        pickle.dump(self.atribut,pickle_out)
        
    def rff(self):
        pickle_in = open(Platform.FILENAME,"rb")
        self.atribut = pickle.load(pickle_in)
