import cgi, pickle,cgitb,codecs,sys,datetime,os
from st17.ListCommand import *

class Dish:

    def __init__(self):
        self.name=""
        self.price=0
        self.grams=0
        self.description=""
        self.edit=[self.AddName,self.AddPrice,self.AddGrams,self.AddDescription]
    
    def AddDish(self,q,selfurl):
        #self.AddName()
        #self.AddPrice()
        #self.AddGrams()
        #self.AddDescription()
        #print("""<input type=hidden name=name value="{name}">
#<input type=hidden name=price value="{price}">
#<input type=hidden name=grams value="{grams}">
#<input type=hidden name=description value="{description}">""")
#        self.name=q.getvalue('name')
#        self.price=q.getvalue('price')
#        self.grams=q.getvalue('grams')
#        self.description=q.getvalue('description')

        
        print("""<form action='st17/Dish.py' method=GET>
Name: <input type=text name=name value="{0}"><br>
Price: <input type=text name=price value="{1}"><br>
Grams: <input type=text name=grams value="{2}"><br>
Description: <input type=text name=description value="{3}"><br>
<input type=submit value="OK"><br>
</form>""".format(self.name,self.price,self.grams,self.description)

    def AddName(self):
        self.name=input("Enter name\n")
    
    def AddPrice(self):
        self.price=input("Enter price\n")
        while(True):
            if IsFloat(self.price):
                break
            else:
                self.price=input("Enter price\n")

    def AddGrams(self):
        self.grams=input("Enter grams\n")
        while(True):
            if IsFloat(self.grams):
                break
            else:
                self.grams=input("Enter price\n")

    def AddDescription(self):
        self.description=input("Enter description\n")

    def ShowDish(self):
        #print("\n0) name - "+self.name+"\n1) price - "+self.price+"\n2) grams - "+self.grams+"\n3) description - "+self.description)
        print("<td>{name}</td><td>{price}</td><td>{grams}</td><td>{description}</td>".format(self.__dict__))

    def EditDish(self):
        self.ShowDish()
        i=input("\nEnter the parameter dish number for editing. To return enter -1.\n")
        while(True):
            if IsInt(i):
                break
            else:
                i=input("\nEnter the parameter dish number for editing. To return enter -1.\n")
        while(int(i)!=-1):
            self.edit[int(i)]()
            self.ShowDish()
            i=input("\nEnter the parameter dish number for editing. To return enter -1.\n")
            while(True):
                if IsInt(i):
                    break
                else:
                    i=input("\nEnter the parameter dish number for editing. To return enter -1.\n")
