from .Journal import Journal

def stripes(func):
    def wrapper(self):
        print('<pre>------------------------------')
        func(self)
        print("------------------------------</pre>")
    
    return wrapper

class Menu:
    def __init__(self, q, selfurl):
        self.q = q
        self.selfurl = selfurl
        
        self.indexurl = '{0}?student={1}'.format(selfurl, q['student'].value)
        
        self.journal = Journal()
        self.journal.load()
        
    def actButton(self, value, title):
        return '<a href="{0}&act={1}">{2}</a>'.format(self.indexurl, value, title)
        
    def indexButton(self):
        print('<a href="{0}">Назад</a>'.format(self.indexurl))
        
    @stripes
    def index(self):
        print(
            self.actButton('add&type=run', "Записать пробежку"), 
            '|', 
            self.actButton('add&type=marathon', "Записать марафон"),
            '<br>'
        )
        
        if len(self.journal.runs) > 0:
            print('<table>')
            for i, run in enumerate(self.journal.runs):
                print('<tr><td>{0}</td><td>{1}</td><td>{2}</td></tr>'.format(
                    run.show(),
                    self.actButton('edit&id={0}'.format(i), "Редактировать"),
                    self.actButton('delete&id={0}'.format(i), "Удалить")
                ))
            print('</table>')
            print(self.actButton('clear', "Очистить журнал"), '<br>')
        else:
            print('Пока в журнале нет записей.<br>')
        
        print('<a href="{0}">Назад</a>'.format(self.selfurl))
    
    @stripes
    def act(self):  
        commands = {
            'add': self.journal.add,
            'edit': self.journal.edit,
            'delete': self.journal.delete,
            'clear': self.journal.clear
        }
        actValue = self.q['act'].value
        
        try:
            commands[actValue](self.q)
        except KeyError:
            print("Команда не найдена!<br>")
        
        self.indexButton()