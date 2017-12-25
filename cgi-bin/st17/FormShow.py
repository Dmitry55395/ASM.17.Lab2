import cgi,os

def LoadTpl(tplName):
    docrootname='PATH_TRANSLATED'
    with open(os.environ[docrootname]+'/cgi-bin/st17/tpl/'+tplName+'.tpl','rt')as filetpl:
        return filetpl.read()

def HeaderPrint():
    print(LoadTpl("header"))

def FooterPrint():
    print(LoadTpl("footer"))

def PrintLink(q,selfurl):
    print(LoadTpl("link").format(selfurl, q.getvalue("student")))

def PrintHeadTable():
    print(LoadTpl("head_table"))

def PrintOpenTR():
    print(LoadTpl("open_tr"))

def PrintCloseTR():
    print(LoadTpl("close_tr"))

def PrintCloseTable():
    print(LoadTpl("close_table"))
