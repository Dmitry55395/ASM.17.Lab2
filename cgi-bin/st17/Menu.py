import cgi,pickle,os
from st17.VipDish import VipDish
from st17.Dish import Dish
from st17.FormShow import *

class Menu:

    def __init__(self,q,selfurl):
        self.q=q
        self.selfurl=selfurl
        try:
            self.LoadDishMenu()
        except:
            self.listdish = []

    def AddDishMenu(self):
        d=Dish()
        d.AddDish(self.q)
        self.listdish.append(d)
        self.ShowDishMenu()

    def ShowInputDishForm(self):
        d=Dish()
        print(LoadTpl("formtype0").format(self.selfurl))
        d.DishForm(self.q,self.selfurl)
        print(LoadTpl("submitendform"))

    def AddVipDishMenu(self):
        vd=VipDish()
        vd.AddDish(self.q)
        self.listdish.append(vd)
        self.ShowDishMenu()

    def ShowInputVipDishForm(self):
        vd=VipDish()
        print(LoadTpl("formtype1").format(self.selfurl))
        vd.DishForm(self.q,self.selfurl)
        print(LoadTpl("submitendform"))

    def ShowDishMenu(self):
        if (len(self.listdish)>0):
            ShowHeadTable()
            for i in self.listdish:
                print("<tr>")
                i.ShowDish(self.q,self.selfurl,self.listdish.index(i))
                print("</tr>")
            print("</table>")
        ShowLink(self.q,self.selfurl)

    def DeleteDishMenu(self):
        del self.listdish[int(self.q.getvalue("inx"))]
        self.ShowDishMenu()

    def CleareDishMenu(self):
        self.listdish.clear()
        self.ShowDishMenu()
        
    def SafeDishMenu(self):
        with open('cgi-bin/st17/menu.db',"wb")as f:
            pickle.dump(self.listdish,f)

    def LoadDishMenu(self):
        with open('cgi-bin/st17/menu.db',"rb") as f:
            self.listdish=pickle.load(f)
        
    def ShowEditDishMenu(self):
        print(LoadTpl("formtype2").format(self.selfurl,self.q.getvalue("inx")))
        self.listdish[int(self.q.getvalue("inx"))].DishForm(self.q,self.selfurl)
        print(LoadTpl("submitendform"))

    def EditDishMenu(self):
        self.listdish[int(self.q.getvalue("inx"))].AddDish(self.q)
        self.ShowDishMenu()
            
