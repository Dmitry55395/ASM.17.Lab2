import cgi, pickle,cgitb,codecs,sys,datetime,os
from st17.Menu import Menu
from st17.Dish import Dish
from st17.VipDish import VipDish
from st17.ListCommand import *
from st17.FormShow import *

def main(q,selfurl):
    m=Menu(q,selfurl)
    HeaderPrint()
    l=[m.AddDishMenu,m.AddVipDishMenu,m.EditDishMenu,m.ClearDishMenu,m.ShowDishMenu,m.SafeDishMenu,m.LoadDishMenu]
    #l = {
    #        'ShowForm':m.AddDishMenu,
    #        'AddItem':m.AddVipDishMenu,
    #        'DeleteItem':m.ShowDishMenu
    #    }
    try:
        l[int(q.getvalue('type'))]()
    except Exception as e:
        #print(e, '<br>')
        if (len(m.listdish)>0):
            ShowTable(l[4])
        ShowLink(q,selfurl)
    #while (True):
    #    i=int(ShowList())
    #    if ((i>len(l)) or (i<0)):
    #        break
    #    MenuFunction(l[i])
    FooterPrint()

if __name__ == "__main__":
    main()
