import cgi
from st17.Menu import Menu
from st17.FormShow import *

def main(q,selfurl):
    m=Menu(q,selfurl)
    HeaderPrint()
    
    l=[m.AddDishInMenu,m.AddVipDishInMenu,m.EditDishInMenu,m.DeleteDishInMenu,m.ShowMenu,m.DishForm,m.VipDishForm,m.EditForm,m.ClearMenu]
    
    try:
        l[int(q.getvalue('type'))]()
    except Exception as e:
        #print(e, '<br>')
        l[4]()
    
    FooterPrint()
    m.SafeMenu()

if __name__ == "__main__":
    main()
