from .mayor import *
import pickle
import cgi

class group:    
    spisok = []
    Gubkin = 'cgi-bin/st19/file.pkl'

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
        print("<td><a href = {0}?student={1}&index=-1&i=add_person> Добавить студента</a></td>".format(self.selfurl, self.q['student'].value))
        print("<td><a href = {0}?student={1}&index=-1&i=add_new_person> Добавить преподавателя</a></td>".format(self.selfurl, self.q['student'].value))
        print("<td><a href = {0}?student={1}&i=display_spisok> Показать список</a></td>".format(self.selfurl, self.q['student'].value))
        print("<td><a href = {0}?student={1}&i=clean_out> Очистить список</a></td>".format(self.selfurl, self.q['student'].value))
        print("<td><a href = {0}>В главное меню</a></td>".format(self.selfurl))
        print("</tr>")
        print("</table>")
        

    def add_person(self):
        self.read()
        if (self.q["i"].value == "add_person"):
            Student().me(self.q, self.selfurl)
        elif (self.q["i"].value == "ok"):
            s=Student()
            s.vvod(self.q, self.selfurl)
            self.spisok.append(s)
            self.write()
            self.display_spisok()
       

    def add_new_person(self):
        self.read()
        if (self.q["i"].value == "add_new_person"):
            Mayor().me(self.q, self.selfurl)
        elif (self.q["i"].value == "okok"):
            np=Mayor()
            np.vvod(self.q, self.selfurl)
            self.spisok.append(np)
            self.write()
            self.display_spisok()


    def display_spisok(self):
        print('<br><br><h1>Список<br><br>')
        for m in self.spisok:
            print(" {0}".format(self.spisok.index(m) + 1))
            m.vyvod()
            print("<br><a href = {0}?i=edit&index={1}&student={2}> Редактировать</a> / ".format(self.selfurl, self.spisok.index(m), self.q['student'].value))
            print("<a href = {0}?i=delete&index={1}&student={2}>Удалить<br><br></a>".format(self.selfurl, self.spisok.index(m), self.q['student'].value))
        if len(self.spisok) == 0:
            print("<br>Список пуст<br></h1>")


    def write(self):
        o = open(group.Gubkin,'wb')
        pickle.dump(self.spisok,o)

    def read(self):
        r = open(group.Gubkin,'rb')
        self.spisok = pickle.load(r)

    def edit(self):
        self.read()
        if (self.q["i"].value == "edit"):
            self.spisok[int(self.q["index"].value)].me(self.q, self.selfurl)
        if (self.q["i"].value == "ok") or (self.q["i"].value == "okok"):
            self.spisok[int(self.q["index"].value)].vvod(self.q, self.selfurl)
        self.write()
        self.display_spisok()

    def clean_out(self):
        self.read()
        self.spisok.clear()
        self.write()

    def delete(self):
        self.read()
        self.spisok.pop(int(self.q["index"].value))
        self.write()
        self.display_spisok()
