from  .myClassFile import myClass

class descendantClass(myClass):

    def __init__(self,q):
        self.name=0
        self.param=0
        self.additionalAttribute=0
        self.secondAdditionalAttribute=0
        # print('<form action="/cgi-bin/lab2.py" >')
        # print('Введите имя:<input type="text" name= "name" value=""><br>')
        # print('Введите параметр:<input type="text" name= "param" value=""><br>')
        # print('Введите дополнительный параметр:<input type="text" name= "additionalAttribute" value=""><br>')
        # print('Введите второй дополнительный параметр:<input type="text" name= "secondAdditionalAttribute" value=""><br>')
        # print('<input  type="submit" value="Создать" />')
        # print('<input type="hidden" name = "action" value="addDescendantClass" />')
        # print('<input type="hidden" name = "student" value={0} />'.format(int(q.getvalue('student'))))
        # print('</form>')
        print(q)
        if q.getvalue('action') == 'addDescendantClass':
         self.name = (q.getvalue('name'))
         self.param = (q.getvalue('param'))
         self.additionalAttribute=(q.getvalue('additionalAttribute'))
         self.secondAdditionalAttribute=(q.getvalue('secondAdditionalAttribute'))
        
    def printAdditionalAttribute(self):
        print( self.additionalAttribute)
        
    def printSecondAdditionalAttribute(self):
        print(self.secondAdditionalAttribute)
        
    def writeAdditionalAttribute(self):
         print("Введите параеметр")
         self.additionalAttribute=input()
         
    def writeSecondAdditionalAttribute(self):
        print("Введите второй паареметр")
        self.secondAdditionalAttribute=input()
