from .Group import *
import cgi

def main(q, selfurl):
    group = Group(q, selfurl)
    group.Load()
    MENU = {
        'display': group.ShowList,
        'get': group.Get,
        'delete': group.Delete,
        'edit': group.Edit,
        'addstudent': group.AddStudent,
        'addundergraduate': group.AddUndergraduate,
        'clear': group.Clear
    }
    print("Content-type: text/html; charset=utf-8\n\n")
    if 'act' in q:
        MENU[q['act'].value]()
    else:
        MENU['display']()
    group.Save()
