from .Department import Department
import datetime
now = datetime.datetime.now()
class Employee(Department):
    def __init__(self):
        Department.__init__(self)
        self.FullName = ""
        self.Age = 0
        self.PhoneNum = ""
        self.TurnTo = str(now.day)+"/"+str(now.month)+"/"+str(now.year)
        self.Salary = 0
        
    def Add(self,q):
        Department.Add(self,q)
        self.Set_Name(q)
        self.Set_Age(q)
        self.Set_Phone(q)
        self.Set_Salary(q)

    def Set_Name(self,q):
        self.FullName = q.getvalue("FullName")

    def Set_Age(self,q):
        self.Age = q.getvalue("Age")

    def Set_Phone(self,q):
        self.PhoneNum = q.getvalue("PhoneNum")

    def Set_Salary(self,q):
        self.Salary = q.getvalue("Salary")

    def Show(self,q,selfurl,nomer):
        print("""<td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{7}</td><td>{8}</td><td>{9}</td><td>{10}</td><td>{11}</td>
<td><a href="{5}?type=11&student={4}&nomer={6}">Edit</a><br>
<a href="{5}?type=12&student={4}&nomer={6}">Delete</a></td>""".format(self.OrganizationName,self.DepName,self.Floor,self.info,q.getvalue("student"),selfurl,nomer,self.FullName,self.Age,self.PhoneNum,self.TurnTo,self.Salary)) 
