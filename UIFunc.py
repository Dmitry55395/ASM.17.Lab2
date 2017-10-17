import os


def LoadTemplate(Tpl_name):
    docrootname = 'PATH_TRANSLATED'
    with open(os.environ[docrootname]+'/cgi-bin/st35/tpl/'+Tpl_name+'.tpl', 'rt') as f:
        return f.read()
    
    
    