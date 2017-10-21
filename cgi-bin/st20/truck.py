from st20.car import car 

class truck(car):

    def __init__(self):
        car.__init__(self)
        self.height=0
        self.carrying=0

    def add(self,q):
        car.add(self,q)
        self.add_height(q)
        self.add_carrying(q)

    def add_height(self,q):
        self.height=q.getvalue("height")

    def add_carrying(self,q):
        self.carrying=q.getvalue("carrying")

    def show_car(self,q,selfurl,nomcar):
        print("""<td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td><td>{8}</td><td>{9}</td>
<td><a href="{6}?type=show_edit&student={5}&nomcar={7}">edit</a><br>
<a href="{6}?type=delete&student={5}&nomcar={7}">delete</a></td>""".format(self.gosnomer,self.mark,self.model,self.horsepower,self.mileage,q.getvalue("student"),selfurl,nomcar,self.height,self.carrying))
