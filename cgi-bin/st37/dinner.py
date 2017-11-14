from .drink import *
import pickle
import  cgi

class dinner:
    kartoteka = []
    f = 'cgi-bin/st37/kartoteka.pkl'

    def __init__(self, q, selfurl):
        self.q = q
        self.selfurl = selfurl
        
        

    def me(self):
        self.read()
        print("<style> table, td, th { border-collapse: separate;  border-left: 10px solid #0000FF; background-color: lavender;} ")
        print("table { width: 100%; } td {height: 50px; text-align: center;font-size: 20px;font-family: Georgia  } ")
        print("h1 { font-size: 20px; font-style: Georgia } </style>")
        
        print('<table>')
        print("<tr>")
        print("<td><a href = {0}?student={1}&index=-1&j=add_food> Добавить блюдо</a></td>".format(self.selfurl, self.q['student'].value))
        print("<td><a href = {0}?student={1}&index=-1&j=add_drink> Добавить напиток</a></td>".format(self.selfurl, self.q['student'].value))
        print("<td><a href = {0}?student={1}&j=all_> Показать картотеку</a></td>".format(self.selfurl, self.q['student'].value))
        print("<td><a href = {0}?student={1}&j=clear> Очистить картотеку</a></td>".format(self.selfurl, self.q['student'].value))
        print("<td><a href = {0}> В главное меню</a></td>".format(self.selfurl))
        print("</tr>")
        print("</table>")

    def add_food(self):
        self.read()
        if (self.q["j"].value == "add_food"): 
            food().me(self.q, self.selfurl)
        elif (self.q["j"].value == "ok"):
            g = food()
            g.vvod(self.q, self.selfurl)
            self.kartoteka.append(g)
            self.write()
            self.all_()

    

    def add_drink(self):
        self.read()
        if (self.q["j"].value == "add_drink"): 
            drink().me(self.q, self.selfurl)
        elif (self.q["j"].value == "okok"):
            d = drink()
            d.vvod(self.q, self.selfurl)
            self.kartoteka.append(d)
            self.write()
            self.all_()

    def all_(self):
        print('<br><br><h1>Список блюд<br><br>')
        for i in self.kartoteka:
            print(" {0}".format(self.kartoteka.index(i) + 1))
            i.vyvod()
            print("<br><a href = {0}?j=edit&index={1}&student={2}> Редактировать</a> / ".format(self.selfurl, self.kartoteka.index(i), self.q['student'].value))
            print("<a href = {0}?j=delete&index={1}&student={2}>Удалить<br><br></a>".format(self.selfurl, self.kartoteka.index(i), self.q['student'].value))
        if len(self.kartoteka) == 0:
            print("<br>Список пуст<br></h1>")
          

    def write(self):
        s = open(dinner.f,'wb')
        pickle.dump(self.kartoteka,s)

    def read(self):
        r = open(dinner.f,'rb')
        self.kartoteka = pickle.load(r)

    def edit(self):
        self.read()
        if (self.q["j"].value == "edit"):
            self.kartoteka[int(self.q["index"].value)].me(self.q, self.selfurl)
        if (self.q["j"].value == "ok") or (self.q["j"].value == "okok"):
            self.kartoteka[int(self.q["index"].value)].vvod(self.q, self.selfurl)
        self.write()
        self.all_()

    def clear(self):
        self.read()
        self.kartoteka.clear()
        self.write()
        
    def delete(self):
        self.read()
        self.kartoteka.pop(int(self.q["index"].value))
        self.write()
        self.all_()
