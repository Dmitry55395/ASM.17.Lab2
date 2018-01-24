import cgi
class Category:
    def __init__(self, q, selfurl):
        self.q=q
        self.selfurl=selfurl
        self.tittle=""

    def read(self):
        self.q = cgi.FieldStorage()
        self.q.getfirst("tittle","--")
        if ('tittle' in self.q):
            self.tittle = self.q['tittle'].value
        else: self.tittle=""
        
    def write_ch(self):
        self.q = cgi.FieldStorage()
        self.q.getfirst("id","--")
        print('<form action="{0}?student={1}&action=1&type=3&id={2}&add={3}">'.format(self.selfurl, self.q['student'].value, self.q['id'].value, self.q['type'].value))
        print('<input type="text" name="student" value="{0}" style="display:none">'.format(self.q['student'].value))
        print('<input type="text" name="action" value="{0}" style="display:none">'.format("1"))
        print('<input type="text" name="type" value="{0}" style="display:none">'.format("3"))
        print('<input type="text" name="id" value="{0}" style="display:none">'.format(self.q['id'].value))
        print('<input type="text" name="add" value="{0}" style="display:none">'.format(self.q['type'].value))
        print('Название категории:<br><input type="text" name="tittle" value="{0}">'.format(self.tittle))

    def write(self):
        print('<td>{0}</td>'.format(self.tittle))

