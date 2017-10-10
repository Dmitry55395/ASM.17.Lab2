import cgi,os

def LoadTpl(tplName):
    docrootname='PATH_TRANSLATED'
    with open(os.environ[docrootname]+'/cgi-bin/st17/tpl/'+tplName+'.tpl','rt')as filetpl:
        return filetpl.read()

def HeaderPrint():
    print(LoadTpl("header"))

def ShowHeadTable():
    print(LoadTpl("headtable"))

def ShowLink(q,selfurl):
    print(LoadTpl("link").format(selfurl, q.getvalue("student")))

def FooterPrint():
    print(LoadTpl("footer"))
