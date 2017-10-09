import cgi, pickle,cgitb,codecs,sys,datetime,os
from st17.VipDish import VipDish
from st17.Dish import Dish
from st17.ListCommand import *
import pickle

cgitb.enable()

class Menu:

    def __init__(self,q,selfurl):
        self.listdish=[]
        self.q=q
        self.selfurl=selfurl
    
    def AddDishMenu(self):
        d=Dish()
        d.AddDish(self.q,self.selfurl)
        self.listdish.append(d)

    def AddVipDishMenu(self):
        vd=VipDish()
        vd.AddVipDish()
        self.listdish.append(vd)

    def ShowDishMenu(self):
        for i in self.listdish:
            #print("")
            #print("id -",self.listdish.index(i))
            print("<tr>")
            i.ShowDish()
            print("""</tr>
edit delete""")

    def ClearDishMenu(self):
        self.listdish.clear()
        print("Menu cleared.\n")

    def SafeDishMenu(self):
        nf=input("Enter the name of the file to save\n")
        with open(nf,"wb")as f:
            pickle.dump(self.listdish,f)
        print("File saved")

    def LoadDishMenu(self):
        nf=input("Enter the name of the file to upload\n")
        if (IsFile(nf)):
            with open(nf,"rb") as f:
                self.listdish=pickle.load(f)
            print("File downloaded")
        else:
            print("This file does not exist")
        
    def EditDishMenu(self):
        if (len(self.listdish)>0):
            self.ShowDishMenu()
            i=int(input("Enter the dish id for editing. To return to the menu enter -1.\n"))
            while(i!=-1):
                self.listdish[i].EditDish()
                self.ShowDishMenu()
                i=int(input("Enter the dish id for editing. To return to the menu enter -1.\n"))
        else:
            print("The menu is empty")
            
