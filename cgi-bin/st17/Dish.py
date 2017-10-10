import cgi,os
from st17.FormShow import *

class Dish:

    def __init__(self):
        self.name=""
        self.price=0
        self.grams=0
        self.description=""
    
    def AddDish(self,q):
        self.name=q.getvalue("name")
        self.price=q.getvalue("price")
        self.grams=q.getvalue("grams")
        self.description=q.getvalue("description")

    def DishForm(self,q,selfurl):
        print(LoadTpl("dishdishform").format(self.name,self.price,self.grams,self.description,q.getvalue("student")))

    def ShowDish(self,q,selfurl,inx):
        print(LoadTpl("dishshowdish").format(self.name,self.price,self.grams,self.description,q.getvalue("student"),selfurl,inx))
