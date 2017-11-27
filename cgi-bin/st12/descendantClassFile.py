from  .myClassFile import myClass

class descendantClass(myClass):

    def __init__(self,q,givenName,givenParam,givenAdditionalAttribute,givenSecondAdditionalAttribute):
        self.name = givenName
        self.param = givenParam
        self.additionalAttribute=givenAdditionalAttribute
        self.secondAdditionalAttribute=givenSecondAdditionalAttribute

        
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
