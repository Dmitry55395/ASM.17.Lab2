import cgi
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

    def Form(self,q,selfurl):
        print(LoadTpl("dish_form").format(self.name,self.price,self.grams,self.description,q.getvalue("student")))

    def ShowDish(self,q,selfurl,inx):
        print(LoadTpl("show_dish").format(self.name,self.price,self.grams,self.description,q.getvalue("student"),selfurl,inx))
