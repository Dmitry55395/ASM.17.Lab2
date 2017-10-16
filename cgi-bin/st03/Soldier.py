
class Private(object):
    def __init__(self , name = ' ' , surname = ' ', age = ' ', specialization = ' '):
        self.name = name
        self.surname = surname
        self.age = age
        self.specialization = specialization
        
    def __str__(self):
        rep = "This is object of class Private"
        return rep
    
    def data_input(self):
        self.name = input("Name: " ,)
        self.surname =  input("Surname: " ,)
        self.age = input("Age: " ,)
        self.specialization = input("Specialization: " ,)
        
    def output(self):
        print(self.name,' ', self.surname, ' ', self.age,' ',self.specialization)


               
         
    
             
        


