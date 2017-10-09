import os


def loadTpl(f_name):
        docrootname = 'PATH_TRANSLATED'
        with open(os.environ[docrootname]+'/cgi-bin/st09/tpl/'+f_name+'.txt', 'rt') as f:
                return f.read()
