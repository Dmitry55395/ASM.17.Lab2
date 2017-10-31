from .emploee import Employee
from .developer import Developer
import pickle 
import os, cgi

class Company():
    def __init__(self, q, selfurl):
        Employee.__init__(self)
        Developer.__init__(self)
        self.company = []
        self.q = q
        self.selfurl = selfurl

    def menu(self):
        self.read_from_file()
        print('<table cellpadding="10" border="1"> <caption>Опции</caption>')
        print("<tr>")
        print("<td><a href = {0}?student={1}&action=1> Показать список </a></td>".format(self.selfurl, self.q['student'].value))
        print("<td><a href = {0}?student={1}&action=2&index={2}> Добавить сотрудника</a></td>".format(self.selfurl, self.q['student'].value,"add"))
        print("<td><a href = {0}?student={1}&action=3&index={2}> Добавить разработчика</a></td>".format(self.selfurl, self.q['student'].value,"add"))
        print("<td><a href = {0}?action=0> В главное меню</a></td>".format(self.selfurl))
        print("</tr>")
        print("</table>")

    def show_list(self):
        print('<br><br><b>_____Список сотрудников_____</b><br><br>')
        for elem in self.company:
            print("   {0}-й сотрудник".format(self.company.index(elem) + 1))
            elem.show()
            print("<br><a href = {0}?student={1}&action=4&index={2}> Редактировать</a> / ".format(self.selfurl, self.q['student'].value, self.company.index(elem)))
            print("<a href = {0}?student={1}&action=5&index={2}>Удалить<br><br></a>".format(self.selfurl, self.q['student'].value, self.company.index(elem)))
        if len(self.company) == 0:
            print("<br>Список пуст<br>")

    def add(self):
        self.read_from_file()
        if self.q["action"].value == "2": 
            Employee().form(self.q, self.selfurl)
        elif self.q["action"].value == "3":
            Developer().form(self.q, self.selfurl)
        elif self.q["action"].value == "6":
            person = Employee()
            person.read(self.q,self.selfurl)
            self.company.append(person)
        elif self.q["action"].value == "7":
            person = Developer()
            person.read(self.q,self.selfurl)
            self.company.append(person)
        self.write_to_file()
        self.show_list()

    def edit(self):
        self.read_from_file()
        person = self.company[int(self.q["index"].value)]
        if self.q["action"].value == "4":
            person.form(self.q, self.selfurl)
        elif (self.q["action"].value == "6") or (self.q["action"].value == "7"):
            self.company.pop(int(self.q["index"].value))
            person.read(self.q,self.selfurl)
            self.company.insert(int(self.q["index"].value), person)
            self.write_to_file()
        self.show_list()

    def delete(self): 
        self.read_from_file()
        self.company.pop(int(self.q["index"].value))
        self.write_to_file()
        self.show_list()

    def read_from_file(self):
        with open("cgi-bin/st38/file.txt", 'rb') as f:
            self.company = pickle.load(f)

    def write_to_file(self):
        with open("cgi-bin/st38/file.txt", 'wb') as f:
            pickle.dump(self.company, f)
