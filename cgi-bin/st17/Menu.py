import cgi,pickle,os
from st17.VipDish import VipDish
from st17.Dish import Dish
from st17.FormShow import *

class Menu:

    def __init__(self,q,selfurl):
        self.q=q
        self.selfurl=selfurl
        try:
            self.LoadMenu()
        except:
            self.listdish = []

    def AddDishInMenu(self):
        d=Dish()
        d.AddDish(self.q)
        self.listdish.append(d)
        self.ShowMenu()

    def DishForm(self):
        d=Dish()
        print(LoadTpl("form_type1").format(self.selfurl,0))
        d.Form(self.q,self.selfurl)
        print(LoadTpl("submit_and_endform"))

    def AddVipDishInMenu(self):
        vd=VipDish()
        vd.AddDish(self.q)
        self.listdish.append(vd)
        self.ShowMenu()

    def VipDishForm(self):
        vd=VipDish()
        print(LoadTpl("form_type1").format(self.selfurl,1))
        vd.Form(self.q,self.selfurl)
        print(LoadTpl("submit_and_endform"))

    def ShowMenu(self):
        if (len(self.listdish)>0):
            PrintHeadTable()
            for i in self.listdish:
                PrintOpenTR()
                i.ShowDish(self.q,self.selfurl,self.listdish.index(i))
                PrintCloseTR()
            PrintCloseTable()
        PrintLink(self.q,self.selfurl)

    def DeleteDishInMenu(self):
        del self.listdish[int(self.q.getvalue("inx"))]
        self.ShowMenu()

    def ClearMenu(self):
        self.listdish.clear()
        self.ShowMenu()
        
    def SafeMenu(self):
        with open('cgi-bin/st17/menu.db',"wb")as f:
            pickle.dump(self.listdish,f)

    def LoadMenu(self):
        with open('cgi-bin/st17/menu.db',"rb") as f:
            self.listdish=pickle.load(f)
        
    def EditForm(self):
        print(LoadTpl("form_type2").format(self.selfurl,self.q.getvalue("inx")))
        self.listdish[int(self.q.getvalue("inx"))].Form(self.q,self.selfurl)
        print(LoadTpl("submit_and_endform"))

    def EditDishInMenu(self):
        self.listdish[int(self.q.getvalue("inx"))].AddDish(self.q)
        self.ShowMenu()
            
