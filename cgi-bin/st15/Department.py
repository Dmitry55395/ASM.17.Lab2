class Department:
    def __init__(self):
        self.DepName=""
        self.OrganizationName=""
        self.Floor=0
        self.info=""
    
    def Add(self,q):
        self.Set_OrgName(q)
        self.Set_DepName(q)
        self.Set_Floor(q)
        self.Set_Info(q)

    def Set_DepName(self,q):
        self.DepName = q.getvalue("DepName")

    def Set_OrgName(self,q):
        self.OrganizationName = q.getvalue("OrganizationName")

    def Set_Floor(self,q):
        self.Floor = q.getvalue("Floor")

    def Set_Info(self,q):
        self.info = q.getvalue("info")

    def Show(self,q,selfurl,nomer):
        print("""<td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td></td><td></td><td></td><td></td><td></td>
<td><a href="{5}?type=10&student={4}&nomer={6}">Edit</a><br>
<a href="{5}?type=12&student={4}&nomer={6}">Delete</a></td>""".format(self.OrganizationName,self.DepName,self.Floor,self.info,q.getvalue("student"),selfurl,nomer))


