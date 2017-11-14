from .part2 import *
import pickle
import cgi

class autopark:
    
    FILENAME = "cgi-bin/st18/file.txt"
    data = []
    
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
        print("<td><a href = {0}?action=2&index=-1&student={1}> Добавить информацию об автомобиле</a></td>".format(self.selfurl, self.q['student'].value))
        print("<td><a href = {0}?action=3&index=-1&student={1}> Добавить полную информацию об автомобиле</a></td>".format(self.selfurl, self.q['student'].value))
        print("<td><a href = {0}?action=1&student={1}> Показать список</a></td>".format(self.selfurl, self.q['student'].value))
        print("<td><a href = {0}?action=8&student={1}> Очистить список</a></td>".format(self.selfurl, self.q['student'].value))
        print("<td><a href = {0}?action=0> В главное меню</a></td>".format(self.selfurl))
        print("</tr>")
        print("</table>")


    def show_data(self):
        print('<br><br><h1>Список автомобилей<br><br>')
        for i in self.data:
            print("   {0}-й автомобиль".format(self.data.index(i) + 1))
            i.write()
            print("<br><a href = {0}?action=4&index={1}&student={2}> Редактировать</a> / ".format(self.selfurl, self.data.index(i), self.q['student'].value))
            print("<a href = {0}?action=5&index={1}&student={2}>Удалить<br><br></a>".format(self.selfurl, self.data.index(i), self.q['student'].value))
        if len(self.data) == 0:
            print("<br>Список пуст<br></h1>")

    def add (self):
        self.rff()
        if self.q["action"].value == "2":
            infcar().tbl(self.q, self.selfurl)
        elif self.q["action"].value == "3":
            fullinfcar().tbl(self.q, self.selfurl)
        elif self.q["action"].value == "6":
            part1 = infcar()
            part1.read(self.q, self.selfurl)
            self.data.append(part1)
        elif self.q["action"].value == "7":
            part1 = fullinfcar()
            part1.read(self.q, self.selfurl)
            self.data.append(part1)
        elif self.q["action"].value == "5":
            self.data.pop(int(self.q["index"].value))
        self.wrtf()
        self.show_data()

    def edit(self):
        self.rff()      
        if self.q["action"].value == "4":
            self.data[int(self.q["index"].value)].tbl(self.q, self.selfurl)
        elif (self.q["action"].value == "6") or (self.q["action"].value == "7"):
            self.data[int(self.q["index"].value)].read(self.q,self.selfurl)
        self.wrtf()
        self.show_data()
        
    def clear_data(self):
        self.rff()
        self.data.clear()
        self.wrtf()

        
    def wrtf(self):
        pickle_out = open(autopark.FILENAME,"wb")
        pickle.dump(self.data,pickle_out)
        
    def rff(self):
        pickle_in = open(autopark.FILENAME,"rb")
        self.data = pickle.load(pickle_in)


