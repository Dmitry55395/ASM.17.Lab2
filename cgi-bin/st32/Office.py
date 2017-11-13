from .Department import Department
from .Employee import Employee
import pickle

class Office:

    def __init__(self,q,selfurl):
        self.q=q
        self.selfurl=selfurl
        try:
            self.loadDB()
        except:
            self.dbase = []

    def Form_Add_Department(self):
        print("""<form action={0} method=GET>
<input type=hidden name=type value=1>
<input type=hidden name=student value={1}>
Organization Name: <input type=text name=OrganizationName><br>
Department Name: <input type=text name=DepName><br>
Floor: <input type=text name=Floor><br>
Info: <input type=text name=info><br>
<input type=submit value="OK"><br>
</form>""".format(self.selfurl,self.q.getvalue("student")))

    def Add_Department(self):
        department = Department()
        department.Add(self.q)
        self.dbase.append(department)
        self.ShowDB()

    def Form_Add_Employee(self):
        print("""<form action={0} method=GET>
<input type=hidden name=type value=2>
<input type=hidden name=student value={1}>
Organization Name: <input type=text name=OrganizationName><br>
Department Name: <input type=text name=DepName><br>
Floor: <input type=text name=Floor><br>
Info: <input type=text name=info><br>
Full Name: <input type=text name=FullName><br>
Age: <input type=text name=Age><br>
Extension Phone Number: <input type=text name=PhoneNum><br>
Salary: <input type=text name=Salary><br>
<input type=submit value="OK"><br>
</form>""".format(self.selfurl,self.q.getvalue("student")))

    def Add_Employee(self):
        employee = Employee()
        employee.Add(self.q)
        self.dbase.append(employee)
        self.ShowDB()

    def Form_Edit_Department(self):
        print("""<form action={0} method=GET>
<input type=hidden name=type value=3>
<input type=hidden name=student value={1}>
<input type=hidden name=nomer value={6}>
Organization Name: <input type=text name=OrganizationName value={2}><br>
Department Name: <input type=text name=DepName value={3}><br>
Floor: <input type=text name=Floor value={4}><br>
Info: <input type=text name=info value={5}><br>
<input type=submit value="OK"><br>
</form>""".format(self.selfurl,
                  self.q.getvalue("student"),
                  self.dbase[int(self.q.getvalue("nomer"))].OrganizationName,
                  self.dbase[int(self.q.getvalue("nomer"))].DepName,
                  self.dbase[int(self.q.getvalue("nomer"))].Floor,
                  self.dbase[int(self.q.getvalue("nomer"))].info,
                  self.q.getvalue("nomer")))

    def Form_Edit_Employee(self):
        print("""<form action={0} method=GET>
<input type=hidden name=type value=3>
<input type=hidden name=student value={1}>
<input type=hidden name=nomer value={6}>
Organization Name: <input type=text name=OrganizationName value={2}><br>
Department Name: <input type=text name=DepName value={3}><br>
Floor: <input type=text name=Floor value={4}><br>
Info: <input type=text name=info value={5}><br>
Full Name: <input type=text name=FullName value={7}><br>
Age: <input type=text name=Age value={8}><br>
Extension Phone Number: <input type=text name=PhoneNum value={9}><br>
Salary: <input type=text name=Salary value={10}><br>
<input type=submit value="OK"><br>
</form>""".format(self.selfurl,
                  self.q.getvalue("student"),
                  self.dbase[int(self.q.getvalue("nomer"))].OrganizationName,
                  self.dbase[int(self.q.getvalue("nomer"))].DepName,
                  self.dbase[int(self.q.getvalue("nomer"))].Floor,
                  self.dbase[int(self.q.getvalue("nomer"))].info,
                  self.q.getvalue("nomer"),
                  self.dbase[int(self.q.getvalue("nomer"))].FullName,
                  self.dbase[int(self.q.getvalue("nomer"))].Age,
                  self.dbase[int(self.q.getvalue("nomer"))].PhoneNum,
                  self.dbase[int(self.q.getvalue("nomer"))].Salary))

    def ShowDB(self):
        if (len(self.dbase)>0):
            print("""<table border="1">
     <tr>
      <th>Organization Name</th>
      <th>Department Name</th>
      <th>Floor</th>
      <th>Info</th>
      <th>Full Name</th>
      <th>Age</th>
      <th>Phone Number</th>
      <th>Turn To</th>
      <th>Salary</th>
      <th>Control</th>
     </tr>""")
            for i in self.dbase:
                print("<tr>")
                i.Show(self.q,self.selfurl,self.dbase.index(i))
                print("</tr>")
            print("</table>")
        print("""<a href="{0}?type=8&student={1}">Add Department</a><br>
<a href="{0}?type=9&student={1}">Add Employee</a><br>
<a href="{0}?type=7&student={1}">Clear</a><br>
<a href="{0}">Back</a><br>""".format(self.selfurl,self.q.getvalue("student")))

    def SaveDB(self):
        with open('cgi-bin/st32/office.db',"wb")as f:
            pickle.dump(self.dbase,f)

    def loadDB(self):
        with open('cgi-bin/st32/office.db',"rb") as f:
            self.dbase=pickle.load(f)

    def ClearDB(self):
        self.dbase.clear()
        self.ShowDB()

    def EditDB(self):
        self.dbase[int(self.q.getvalue("nomer"))].Add(self.q)
        self.ShowDB()

    def Delete(self):
        del self.dbase[int(self.q.getvalue("nomer"))]
        self.ShowDB()


