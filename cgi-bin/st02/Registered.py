from .Guests import *
#import Guests

def loadTpl(nameTpl):
    docrootname = 'PATH_TRANSLATED'
    with open(os.environ[docrootname] + '/cgi-bin/st02/tpl/' + nameTpl + '.tpl', 'r') as f:
        return f.read()


class Registered(Guest):
    """Класс потомок - зарегистрированный пользователь"""
    def __init__(self, q, selfurl):
        self.q = q
        self.selfurl = selfurl
        self.number = ''
        self.name = ''
        self.surname = ''
        self.id = None

    def add(self):
        print (loadTpl('form_reg').format(self.q.getvalue('student'), -1, self.number, self.name, self.surname))

    def save(self, id_count):
        self.number = self.q.getvalue('number', '')
        self.name = self.q.getvalue('name', '')
        self.surname = self.q.getvalue('surname', '')
        self.id = id_count

    def show(self):
        print (loadTpl('show_reg').format(self.q.getvalue('student'), self.number, self.name, self.surname, self.id))

    def edit(self):
        print (loadTpl('form_reg').format(self.q.getvalue('student'), self.id,  self.number, self.name, self.surname))

        
