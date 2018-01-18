from .Soldier import Private
from .Mercenary import Officer
from .TplLoader import *
import pickle


class Staff:
       def __init__(self,q,selfurl):
              self.q=q
              self.url=selfurl
              self.staff=[]            

       def add_private(self):
              military = Private(self.q,self.url)
              military.data_input(self.e)
              
       def add_officer(self):
              military = Officer(self.q,self.url)
              military.data_input(self.e)

       def add(self):
              self.e = int(self.q.getvalue('edit',-1))
              if self.e==-1:
                     print(LoadTpl('ClassSelect').format(self.q['student'].value,self.url))
              cls=int(self.q.getvalue('class', 0))
              if (cls==1):
                     self.add_private()
              if (cls==2):
                     self.add_officer()

       def list_append(self, military):
              self.read()
              e = int(self.q.getvalue('edit',-1))
              if e==-1:
                     self.staff.append(military)
              else:
                     self.staff[e]=military
              self.write()

       def save(self):
              save_value=int(self.q.getvalue('save', 0))
              if (save_value==1):
                     military = Private(self.q,self.url)
                     military.save_input()
                     self.list_append(military)
              if (save_value==2):
                     military = Officer(self.q,self.url)
                     military.save_input()
                     self.list_append(military)

       def out(self):
              self.read()
              for index,military in enumerate(self.staff):
                     military.output(index)

       def write(self):
              f=open("cgi-bin/st03/staff.dat", "wb")
              pickle.dump(self.staff, f)

       def read(self):
              f=open("cgi-bin/st03/staff.dat", "rb")
              self.staff=pickle.load(f)
             # print(self.staff[0])
              return self.staff

       def clean(self):
              self.staff.clear()

       def edit(self):
              self.read()
              idd = int(self.q.getvalue('id'))
              mil= self.staff[idd]
              mil.edit(idd)
              

       def delete(self):
              self.read()
              d = int(self.q.getvalue('delete'))
              self.staff.pop(d)
              self.write()
              

              

