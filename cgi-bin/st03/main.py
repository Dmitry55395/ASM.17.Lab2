import cgi, cgitb, os, sys, codecs
from .Army import Staff

def LoadTpl(tplName):
    docrootname = 'PATH_TRANSLATED'
    with open(os.environ[docrootname]+'/cgi-bin/st03/tpl/'+tplName+'.html', 'rt') as f:
        return f.read()

Military_unit=Staff()
menu = {"1":("Add object", Military_unit.add),
        "2":("Edit", Military_unit.edit),
        "3":("Delete object", Military_unit.delete),
        "4":("Show list", Military_unit.out),
        "5":("Save to file", Military_unit.write),
        "6":("Load from file", Military_unit.read),
        "7":("Exit", "")}


def main(q, selfurl):
    print('Content-type: text/html')
    print(LoadTpl('header').format(q['student'].value,selfurl))
    act =int(q.getvalue('action', 0))
    if act > 0 and act < 7:
        menu[str(act)][1]()
    #else:
        #for key in menu:
            #print(key + " " + menu[key][0] + '<br>')
            

if __name__ == "__main__":
    main()
