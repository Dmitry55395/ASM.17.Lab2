class myClass:

    def __init__(self,q,givenName,givenParam):
         self.name =givenName
         self.param =givenParam


        
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
