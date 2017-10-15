from .mage import *
import pickle
import  cgi

class Squad:
    
    FILENAME = "cgi-bin/st05/file.txt"
    spisok = []
    
    def __init__(self, q, selfurl):
        self.q = q
        self.selfurl = selfurl
        pass
        
    def tbl(self):
        #self.wrtf()
        self.rff()
        print("<style> table, td, th { border-collapse: collapse; border-left: 10px solid #663399; background-color: lightgrey;} ")
        print("table { width: 100%; } td {height: 50px; text-align: center;font-size: 20px;font-family: Monaco, Courier, monospace; } ")
        print("h1 { font-size: 15px; font-style: oblique; } </style>")
        
        print('<table>')
        print("<tr>")
        print("<td><a href = {0}?action=2&index=-1&student={1}> Добавить воина</a></td>".format(self.selfurl, self.q['student'].value))
        print("<td><a href = {0}?action=3&index=-1&student={1}> Добавить воина-мага</a></td>".format(self.selfurl, self.q['student'].value))
        print("<td><a href = {0}?action=1&student={1}> Показать список</a></td>".format(self.selfurl, self.q['student'].value))
        print("<td><a href = {0}?action=8&student={1}> Очистить список</a></td>".format(self.selfurl, self.q['student'].value))
        print("<td><a href = {0}?action=0> В главное меню</a></td>".format(self.selfurl))
        print("</tr>")
        print("</table>")


    def show_spisok(self):
        print('<br><br><h1>Список воинов<br><br>')
        for i in self.spisok:
            print("   {0}-й воин".format(self.spisok.index(i) + 1))
            i.write()
            print("<br><a href = {0}?action=4&index={1}&student={2}> Редактировать</a> / ".format(self.selfurl, self.spisok.index(i), self.q['student'].value))
            print("<a href = {0}?action=5&index={1}&student={2}>Удалить<br><br></a>".format(self.selfurl, self.spisok.index(i), self.q['student'].value))
        if len(self.spisok) == 0:
            print("<br>Список пуст<br></h1>")

    def add(self):
        self.rff()
        if self.q["action"].value == "2":
            Warrior().tbl(self.q, self.selfurl)
        elif self.q["action"].value == "3":
            Mage().tbl(self.q, self.selfurl)
        elif self.q["action"].value == "6":
            warrior = Warrior()
            warrior.read(self.q, self.selfurl)
            self.spisok.append(warrior)
        elif self.q["action"].value == "7":
            warrior = Mage()
            warrior.read(self.q, self.selfurl)
            self.spisok.append(warrior)
        elif self.q["action"].value == "5":
            self.spisok.pop(int(self.q["index"].value))
        self.wrtf()
        self.show_spisok()

    def edit(self):
        self.rff()      
        if self.q["action"].value == "4":
            self.spisok[int(self.q["index"].value)].tbl(self.q, self.selfurl)
        elif (self.q["action"].value == "6") or (self.q["action"].value == "7"):
            self.spisok[int(self.q["index"].value)].read(self.q,self.selfurl)
        self.wrtf()
        self.show_spisok()
        
    def clear_spisok(self):
        self.rff()
        self.spisok.clear()
        self.wrtf()

        
    def wrtf(self):
        pickle_out = open(Squad.FILENAME,"wb")
        pickle.dump(self.spisok,pickle_out)
        
    def rff(self):
        pickle_in = open(Squad.FILENAME,"rb")
        self.spisok = pickle.load(pickle_in)


