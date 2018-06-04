from .Smartphone import *
import pickle
import cgi

class Devices:

    def __init__(self, q, selfurl):
        self.q = q
        self.selfurl = selfurl
        self.dev_list = []
        self.data_file = './cgi-bin/st43/dev_list.pkl'

    def rec(self):
        self.read_list()
        print('<h1><strong>Device List</strong></h1>')
        print('<hr/>')
        print('<table>')
        print("<tbody>")
        print("<tr><td><a href = {0}?student={1}&index=-1&act=add_phone> Add Phone</a></td></tr>"
              .format(self.selfurl,self.q['student'].value))

        print("<tr><td><a href={0}?student={1}&index=-1&act=add_smartphone> Add Smartphone</a></td></tr>"
              .format(self.selfurl,self.q['student'].value))

        print("<tr><td><a href={0}?student={1}&act=display_list> Display List</a></td></tr>"
              .format(self.selfurl,self.q['student'].value))

        print("<tr><td><a href={0}?student={1}&act=clear_list> Clear List</a></td></tr>"
              .format(self.selfurl,self.q['student'].value))

        print("<tr><td><a href={0}> Exit</a></td></tr>".format(self.selfurl))
        print("</tbody>")
        print("</table>")
        print('<hr/>')



    def add_phone(self):
        self.read_list()
        if (self.q["act"].value == "add_phone"):
            Phone().rec(self.q, self.selfurl)
        elif (self.q["act"].value == "ph"):
            p = Phone()
            p.set_data(self.q, self.selfurl)
            self.dev_list.append(p)
            self.write_list()



    def add_smartphone(self):
        self.read_list()
        if (self.q["act"].value == "add_smartphone"):
            Smartphone().rec(self.q, self.selfurl)
        elif (self.q["act"].value == "sph"):
            sp = Smartphone()
            sp.set_data(self.q, self.selfurl)
            self.dev_list.append(sp)
            self.write_list()



    def delete_device(self):
        self.read_list()
        self.dev_list.pop(int(self.q["index"].value))
        self.write_list()


    def edit_device(self):
        self.read_list()
        if (self.q["act"].value == "edit"):
            self.dev_list[int(self.q["index"].value)].rec(self.q, self.selfurl)
        if (self.q["act"].value == "ph") or (self.q["act"].value == "sph"):
            self.dev_list[int(self.q["index"].value)].set_data(self.q, self.selfurl)
        self.write_list()



    def display_list(self):
        print('<h2><strong>List of devices:</strong></h2>')
        print('<hr/>')
        print('<table border="1">')
        print('<tbody>')
        print('<tr><td> Num</td>' +
              '<td> Vendor</td>' +
              '<td> Model</td>' +
              '<td> Battery</td>' +
              '<td> Camera</td>' +
              '<td> Edit|Delete</td></tr>')
        for el in self.dev_list:
            print('<tr>')
            print('<td> {0}</td>'.format(self.dev_list.index(el) + 1))
            print('<td> {0}</td>'.format(el.get_vendor()))
            print('<td> {0}</td>'.format(el.get_model()))
            if type(el) is Phone:
                print('<td></td><td></td>')
            else:
                print('<td> {0}</td>'.format(el.get_battery()))
                print('<td> {0}</td>'.format(el.get_camera()))
            print('<td><a href = {0}?act=edit&index={1}&student={2}> Edit</a> |'
                  .format(self.selfurl,self.dev_list.index(el),self.q['student'].value))
            
            print('<a href = {0}?act=delete&index={1}&student={2}>Delete</a></td></tr>'
                  .format(self.selfurl,self.dev_list.index(el),self.q['student'].value))

        if len(self.dev_list) == 0:
            print("<br>List is empty<br></h1>")



    def clear_list(self):
        self.read_list()
        self.dev_list.clear()
        self.write_list()


    def write_list(self):
        pickle.dump(self.dev_list, open(self.data_file, "wb"))



    def read_list(self):
        self.dev_list = pickle.load(open(self.data_file, "rb"))
