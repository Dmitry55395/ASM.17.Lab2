class car:

    def __init__(self):
        self.gosnomer=""
        self.mark=""
        self.model=""
        self.horsepower=0
        self.mileage=0

    def add(self,q):
        self.add_gosnomer(q)
        self.add_mark(q)
        self.add_model(q)
        self.add_horsepower(q)
        self.add_mileage(q)

    def add_gosnomer(self,q):
        self.gosnomer=q.getvalue("gosnomer")

    def add_mark(self,q):
        self.mark=q.getvalue("mark")

    def add_model(self,q):
        self.model=q.getvalue("model")
        
    def add_horsepower(self,q):
        self.horsepower=q.getvalue("horsepower")

    def add_mileage(self,q):
        self.mileage=q.getvalue("mileage")

    def show_car(self,q,selfurl,nomcar):
        print("""<td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td><td></td><td></td>
<td><a href="{6}?type=show_edit&student={5}&nomcar={7}">edit</a><br>
<a href="{6}?type=delete&student={5}&nomcar={7}">delete</a></td>""".format(self.gosnomer,self.mark,self.model,self.horsepower,self.mileage,q.getvalue("student"),selfurl,nomcar))
