import cgi, pickle,cgitb,codecs,sys,datetime,os
from st17.Dish import Dish
from st17.ListCommand import *

class VipDish(Dish):
    
    def __init__(self):
        Dish.__init__(self)
        self.bonus=0
        self.calories=0
        self.edit.append(self.AddBonus)
        self.edit.append(self.AddCalories)

    def AddVipDish(self):
        Dish.AddDish(self)
        self.AddBonus()
        self.AddCalories()

    def AddBonus(self):
        self.bonus=input("Enter bonus\n")
        while(True):
            if IsInt(self.bonus):
                break
            else:
                self.bonus=input("Enter bonus\n")

    def AddCalories(self):
        self.calories=input("Enter calories\n")
        while(True):
            if IsFloat(self.calories):
                break
            else:
                self.calories=input("Enter calories\n")

    def ShowDish(self):
        Dish.ShowDish(self)
        #print("4) bonus - "+self.bonus+"\n5) calories - "+self.calories)
        print("<td>{bonus}</td><td>{calories}</td>".format(self.bonus,self.calories))

    def EditDish(self):
        self.ShowDish()
        i=input("\nEnter the parameter dish number for editing. To return enter -1.\n")
        while(True):
            if IsInt(i):
                break
            else:
                i=input("\nEnter the parameter dish number for editing. To return enter -1.\n")
        while (int(i)!=-1):
            self.edit[int(i)]()
            self.ShowDish()
            i=input("\nEnter the parameter dish number for editing. To return enter -1.\n")
            while(True):
                if IsInt(i):
                    break
                else:
                    i=input("\nEnter the parameter dish number for editing. To return enter -1.\n")
