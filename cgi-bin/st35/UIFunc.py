import os, sys, threading, time

def LoadTemplate(Tpl_name):
    docrootname = 'PATH_TRANSLATED'
    with open(os.environ[docrootname]+'/cgi-bin/st35/Templates/'+Tpl_name+'.tpl', 'rt') as f:
        return f.read()