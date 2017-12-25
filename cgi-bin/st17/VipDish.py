import cgi
from st17.Dish import Dish
from st17.FormShow import *

class VipDish(Dish):
    
    def __init__(self):
        Dish.__init__(self)
        self.bonus=0
        self.calories=0

    def AddDish(self,q):
        Dish.AddDish(self,q)
        self.bonus=q.getvalue("bonus")
        self.calories=q.getvalue("calories")
        
    def Form(self,q,selfurl):
        Dish.Form(self,q,selfurl)
        print(LoadTpl("vipdish_form").format(self.bonus,self.calories))
        
    def ShowDish(self,q,selfurl,inx):
        print(LoadTpl("show_vipdish").format(self.name,self.price,self.grams,self.description,self.bonus,self.calories,q.getvalue("student"),selfurl,inx))
