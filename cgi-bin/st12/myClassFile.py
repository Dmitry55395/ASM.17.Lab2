class myClass:

    def __init__(self,q):
         self.name = 0
         self.param = 0
         print('<form action="/cgi-bin/lab2.py" >')
         print('Введите имя:<input type="text" name= "name" value=""><br>')
         print('Введите параметр:<input type="text" name= "param" value=""><br>')
         print('<input  type="submit" value="Создать" />')
         print('<input type="hidden" name = "action1" value="addclass" />')
         print('<input type="hidden" name = "student" value={0} />'.format(int(q.getvalue('student'))))
         print('</form>')
         if q.getvalue('action1') == 'addclass':
            self.name = (q.getvalue('name'))
            print(self.name)
            self.param = (q.getvalue('param'))

        
    def printName(self):
        print(self.name)
        
    def printParam(self):
        print(self.param)
        
    def writeName(self):
        print("Введите имя")
        self.name=input()
        
    def writeParam(self):
        print("Введите паареметр")
        self.param=input()
