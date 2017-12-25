import os


def loadTpl(f_name):
        docrootname = 'PATH_TRANSLATED'
        with open(os.environ[docrootname]+'/cgi-bin/st25/tpl/'+f_name+'.tpl', 'rt') as f:
                return f.read()
