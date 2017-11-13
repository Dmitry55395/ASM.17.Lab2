from .Company import *
import cgi

def main(q, selfurl):
    company = Company(q, selfurl)
    company.Read_File()
    MENU = {
        'show': company.Show_List,
        'save': company.Save_Info,
        'delete': company.Delete_Worker,
        'edit': company.Edit_Worker,
        'addworker': company.Add_Worker,
        'addfired': company.Add_Fired,
        'clear': company.Clear_List
    }
    print ("Content-type: text/html; charset=utf-8\n\n")
    if 'act' in q:
        MENU[q['act'].value]()
    else:
        MENU['show']()
    company.Write_File()
