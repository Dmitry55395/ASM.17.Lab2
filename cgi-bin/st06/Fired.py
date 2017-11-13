from .Worker import *

class Fired(Worker):
    def __init__(self):
        super().__init__()
        self.type = 'Бывший сотрудник'
        self.date = ''
        self.reason = ''

    def __str__(self):
        return super().__str__() + '<b>Дата увольнения:</b> {}<br><b>Причина увольнения:</b> {}<br>'.format(self.date, self.reason)

    def Edit_Show(self):
        super().Edit_Show()
        print('<tr><td>Дата увольнения</td><td><input type="text" name="date" value="{0}"></td></tr>'.format(self.date))
        print('<tr><td>Причина увольнения</td><td><input type="text" name="reason" value="{0}"></td></tr>'.format(self.reason))
        
    def Edit_Save(self, q):
        super().Edit_Save(q)
        self.date = q.getvalue('date')
        self.reason = q.getvalue('reason')
