from .supercar import *
import pickle
import  cgi

class Autocenter:
    
    FILENAME = "cgi-bin/st36/file.txt"
    spisok = []
    
    def __init__(self, q, selfurl):
        self.q = q
        self.selfurl = selfurl
        pass
        
    def tbl(self):
        #self.wrtf()
        self.rff()

        
        print('<table>')
        print("<tr>")
        print("<td><a href = {0}?action=2&index=-1&student={1}> Add car</a></td>".format(self.selfurl, self.q['student'].value))
        print("<td><a href = {0}?action=3&index=-1&student={1}> Add supercar</a></td>".format(self.selfurl, self.q['student'].value))
        print("<td><a href = {0}?action=1&student={1}> Show list</a></td>".format(self.selfurl, self.q['student'].value))
        print("<td><a href = {0}?action=8&student={1}> Clear list</a></td>".format(self.selfurl, self.q['student'].value))
        print("<td><a href = {0}?action=0> Main menu</a></td>".format(self.selfurl))
        print("</tr>")
        print("</table>")


    def show_spisok(self):
        print('<br><br><h1>List autocenters<br><br>')
        for i in self.spisok:
            print("   {0} autocenter".format(self.spisok.index(i) + 1))
            i.write()
            print("<br><a href = {0}?action=4&index={1}&student={2}> Edit</a> / ".format(self.selfurl, self.spisok.index(i), self.q['student'].value))
            print("<a href = {0}?action=5&index={1}&student={2}>Delete<br><br></a>".format(self.selfurl, self.spisok.index(i), self.q['student'].value))
        if len(self.spisok) == 0:
            print("<br>List is empty<br></h1>")

    def add(self):
        self.rff()
        if self.q["action"].value == "2":
            Car().tbl(self.q, self.selfurl)
        elif self.q["action"].value == "3":
            Supercar().tbl(self.q, self.selfurl)
        elif self.q["action"].value == "6":
            car = Supercar()
            car.read(self.q, self.selfurl)
            self.spisok.append(car)
        elif self.q["action"].value == "7":
            car = Supercar()
            car.read(self.q, self.selfurl)
            self.spisok.append(car)
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
        pickle_out = open(Autocenter.FILENAME,"wb")
        pickle.dump(self.spisok,pickle_out)
        
    def rff(self):
        pickle_in = open(Autocenter.FILENAME,"rb")
        self.spisok = pickle.load(pickle_in)


