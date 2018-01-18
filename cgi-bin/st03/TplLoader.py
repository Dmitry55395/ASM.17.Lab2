import  os

def LoadTpl(tplName):
    docrootname = 'PATH_TRANSLATED'
    with open(os.environ[docrootname]+'/cgi-bin/st03/tpl/'+tplName+'.html', 'rt') as f:
        return f.read()
