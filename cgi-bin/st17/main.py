import cgi
from st17.Menu import Menu
from st17.FormShow import *

def main(q,selfurl):
    m=Menu(q,selfurl)
    HeaderPrint()
    
    l=[m.AddDishMenu,m.AddVipDishMenu,m.EditDishMenu,m.DeleteDishMenu,m.ShowDishMenu,m.ShowInputDishForm,m.ShowInputVipDishForm,m.ShowEditDishMenu,m.CleareDishMenu]
    try:
        l[int(q.getvalue('type'))]()
    except Exception as e:
        #print(e, '<br>')
        l[4]()
    
    FooterPrint()
    m.SafeDishMenu()

if __name__ == "__main__":
    main()
