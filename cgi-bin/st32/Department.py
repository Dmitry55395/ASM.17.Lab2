class Department:
    def __init__(self):
        self.DepName=""
        self.OrganizationName=""
        self.Floor=0
        self.info=""
#        self.editlist={
#            "1": ['Organization Name', self.Set_OrgName],
#            "2": ['Department Name', self.Set_DepName],
#            "3": ['Floor', self.Set_Floor],
#            "4": ['Info', self.Set_Info],
#        }
    
    def Add(self,q):
        self.Set_OrgName(q)
        self.Set_DepName(q)
        self.Set_Floor(q)
        self.Set_Info(q)

    def Set_DepName(self,q):
        self.DepName = q.getvalue("OrganizationName")

    def Set_OrgName(self,q):
        self.OrganizationName = q.getvalue("DepName")

    def Set_Floor(self,q):
        self.Floor = q.getvalue("Floor")

    def Set_Info(self,q):
        self.info = q.getvalue("info")

    def Show(self,q,selfurl,nomer):
#        print("\n1. Organization: "+self.OrganizationName+"\n2. Department Name: "+self.DepName+"\n3. Floor: "+self.Floor+"\n4. Info: "+self.info)
        print("""<td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td></td><td></td><td></td><td></td><td></td>
<td><a href="{5}?type=10&student={4}&nomer={6}">Edit</a><br>
<a href="{5}?type=12&student={4}&nomer={6}">Delete</a></td>""".format(self.DepName,self.OrganizationName,self.Floor,self.info,q.getvalue("student"),selfurl,nomer))


