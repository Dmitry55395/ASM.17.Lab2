from .Student import *

class Undergraduate(Student):
    def __init__(self):
        super().__init__()
        self.advisor = ''
        self.topic = ''
        
    def Write(self):
       print('<td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td><td>{5}</td>'.format(self.name, self.age, self.year, self.payment, self.advisor, self.topic))

    def ShowEdit(self):
        super().ShowEdit()
        print('<tr><td>Научный руководитель:</td><td><input type="text" name="advisor" value="{0}"></td></tr>'.format(self.advisor))
        print('<tr><td>Тема диплома:</td><td><input type="text" name="topic" value="{0}"></td></tr>'.format(self.topic))
        
    def SaveEdit(self, q):
        super().SaveEdit(q)
        self.advisor = q.getvalue('advisor')
        self.topic = q.getvalue('topic')
