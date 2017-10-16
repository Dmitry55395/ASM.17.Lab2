#from .Soldier import Private
from .Mercenary import Officer
import pickle 

class Staff:
       def __init__(self):
              self.staff=[]

       def add_private(self):
              military = Private()
              military.data_input()
              self.staff.append(military)

       def add_officer(self):
              military = Officer()
              military.data_input()
              self.staff.append(military)

       def add(self):
              if int(input("input 0 for soldier or 1 for officer " ,)):
                     self.add_officer()
              else:
                     self.add_private()

              
       def out(self):
              print('')
              for i,military in enumerate(self.staff):
                     military.output()

       def write(self):
              f=open("cgi-bin/st03/staff.dat", "wb")
              pickle.dump(self.staff, f)

       def read(self):
              f=open("cgi-bin/st03/staff.dat", "rb")
              self.staff=pickle.load(f)

       def clean(self):
              self.staff.clear()

       def edit(self):
              self.out()
              c = int(input("Chose number of edited object " ,))
              self.staff[c].data_input()

       def delete(self):
              d = int(input("Chose number of deleted object " ,))
              self.staff.pop(d)
              

              
              
