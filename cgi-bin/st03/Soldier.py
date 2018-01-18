from .TplLoader import *

class Private(object):
    def __init__(self , q, selfurl):
        self.q=q
        self.url=selfurl
        self.name = ''
        self.surname = ''
        self.age = ''
        self.specialization = ''
            
    def data_input(self,e):
        print(LoadTpl('SoldierForm').format(self.q['student'].value,self.url,e,self.name,self.surname,self.age,self.specialization))

    def edit(self,e):
        print(LoadTpl('SoldierForm').format(self.q['student'].value,self.url,e,self.name,self.surname,self.age,self.specialization))

    def save_input(self):
        self.name = self.q.getvalue('name')
        self.surname = self.q.getvalue('surname')
        self.age = self.q.getvalue('age')
        self.specialization = self.q.getvalue('specialization')

        
    def output(self, index):
        #print(self.name,' ', self.surname, ' ', self.age,' ',self.specialization)
        print(LoadTpl('ElementShowSoldier').format(self.q['student'].value,self.url, self.name,self.surname,self.age,self.specialization,index))


               
         
    
             
        


