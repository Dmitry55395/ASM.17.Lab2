import pickle, cgi, cgitb, codecs, sys, os, datetime
cgitb.enable()

def loadTpl(nameTpl):
    docrootname = 'PATH_TRANSLATED'
    with open(os.environ[docrootname] + '/cgi-bin/st02/tpl/' + nameTpl + '.tpl', 'r') as f:
        return f.read()


class Guest(object):
    """Базовый класс - гость"""
    def __init__(self, q, selfurl):
        self.name = ''
        self.surname = ''
        self.id = None
        self.q = q
        self.selfurl = selfurl

    def show(self):
        print (loadTpl('show_guest').format(self.q.getvalue('student'), self.name, self.surname, self.id))

    def add(self):
        print (loadTpl('form_guest').format(self.q['student'].value, -1, self.name, self.surname))

    def save(self, id_count):
        self.id = id_count
        self.name = self.q.getvalue('name', '')
        self.surname = self.q.getvalue('surname', '')

    def edit(self):
        print (loadTpl('form_guest').format(self.q.getvalue('student'), self.id, self.name, self.surname))
                
