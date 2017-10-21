import pickle
from st20.car import car
from st20.truck import truck

class car_park:

    def __init__(self,q,selfurl):
        self.q=q
        self.selfurl=selfurl
        try:
            self.load()
        except:
            self.park = []

    def show_add_car(self):
        print("""<form action={0} method=GET>
<input type=hidden name=type value=add_car>
<input type=hidden name=student value={1}>
gosnomer: <input type=text name=gosnomer><br>
mark: <input type=text name=mark><br>
model: <input type=text name=model><br>
horsepower: <input type=text name=horsepower><br>
mileage: <input type=text name=mileage><br>
<input type=submit value="OK"><br>
</form>""".format(self.selfurl,self.q.getvalue("student")))

    def show_add_truck(self):
        print("""<form action={0} method=GET>
<input type=hidden name=type value=add_truck>
<input type=hidden name=student value={1}>
gosnomer: <input type=text name=gosnomer><br>
mark: <input type=text name=mark><br>
model: <input type=text name=model><br>
horsepower: <input type=text name=horsepower><br>
mileage: <input type=text name=mileage><br>
height: <input type=text name=height><br>
carrying: <input type=text name=carrying><br>
<input type=submit value="OK"><br>
</form>""".format(self.selfurl,self.q.getvalue("student")))

    def show_edit(self):
        try:
            print("""<form action={0} method=GET>
<input type=hidden name=type value=edit>
<input type=hidden name=student value={1}>
<input type=hidden name=nomcar value={9}>
gosnomer: <input type=text name=gosnomer value={2}><br>
mark: <input type=text name=mark value={3}><br>
model: <input type=text name=model value={4}><br>
horsepower: <input type=text name=horsepower value={5}><br>
mileage: <input type=text name=mileage value={6}><br>
height: <input type=text name=height value={7}><br>
carrying: <input type=text name=carrying value={8}><br>
<input type=submit value="OK"><br>
</form>""".format(self.selfurl,self.q.getvalue("student"),self.park[int(self.q.getvalue("nomcar"))].gosnomer,self.park[int(self.q.getvalue("nomcar"))].mark,self.park[int(self.q.getvalue("nomcar"))].model,self.park[int(self.q.getvalue("nomcar"))].horsepower,self.park[int(self.q.getvalue("nomcar"))].mileage,self.park[int(self.q.getvalue("nomcar"))].height,self.park[int(self.q.getvalue("nomcar"))].carrying,self.q.getvalue("nomcar")))
        except:
            print("""<form action={0} method=GET>
<input type=hidden name=type value=edit>
<input type=hidden name=student value={1}>
<input type=hidden name=nomcar value={7}>
gosnomer: <input type=text name=gosnomer value={2}><br>
mark: <input type=text name=mark value={3}><br>
model: <input type=text name=model value={4}><br>
horsepower: <input type=text name=horsepower value={5}><br>
mileage: <input type=text name=mileage value={6}><br>
<input type=submit value="OK"><br>
</form>""".format(self.selfurl,self.q.getvalue("student"),self.park[int(self.q.getvalue("nomcar"))].gosnomer,self.park[int(self.q.getvalue("nomcar"))].mark,self.park[int(self.q.getvalue("nomcar"))].model,self.park[int(self.q.getvalue("nomcar"))].horsepower,self.park[int(self.q.getvalue("nomcar"))].mileage,self.q.getvalue("nomcar")))

    def add_car(self):
        c=car()
        c.add(self.q)
        self.park.append(c)
        self.show()

    def add_truck(self):
        t=truck()
        t.add(self.q)
        self.park.append(t)
        self.show()

    def edit(self):
        self.park[int(self.q.getvalue("nomcar"))].add(self.q)
        self.show()

    def delete(self):
        del self.park[int(self.q.getvalue("nomcar"))]
        self.show()

    def clear(self):
        self.park.clear()
        self.show()

    def show(self):
        if (len(self.park)>0):
            print("""<table border="1">
     <tr>
      <th>Gosnomer</th>
      <th>Mark</th>
      <th>Model</th>
      <th>Horsepower</th>
      <th>Mileage</th>
      <th>Height</th>
      <th>Carrying</th>
      <th>Control</th>
     </tr>""")
            for i in self.park:
                print("<tr>")
                i.show_car(self.q,self.selfurl,self.park.index(i))
                print("</tr>")
            print("</table>")
        print("""<a href="{0}?type=show_add_car&student={1}">add_car</a><br>
<a href="{0}?type=show_add_truck&student={1}">add_truck</a><br>
<a href="{0}?type=clear&student={1}">clear_car_park</a><br>
<a href="{0}">back</a><br>""".format(self.selfurl,self.q.getvalue("student")))

    def safe(self):
        with open('cgi-bin/st20/car_park.db',"wb")as f:
            pickle.dump(self.park,f)

    def load(self):
        with open('cgi-bin/st20/car_park.db',"rb") as f:
            self.park=pickle.load(f)
