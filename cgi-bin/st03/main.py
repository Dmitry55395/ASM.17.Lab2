import cgi, cgitb, os, sys, codecs
from .army import Staff
from .TplLoader import *


def main(q, selfurl):
    Military_unit=Staff(q,selfurl)
    menu = {"1":("Add object", Military_unit.add),
        "2":("Edit", Military_unit.edit),
        "3":("Delete object", Military_unit.delete),
        "4":("Show list", Military_unit.out),
        "5":("Exit", "")}
    print ("Content-type: text/html; charset=utf-8\n\n")
    print(LoadTpl('header').format(q['student'].value,selfurl))
    act =int(q.getvalue('action', 4))
    if act > 0 and act < 5:
        menu[str(act)][1]()

    
    Military_unit.save()
        

