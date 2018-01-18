from .Soldier import Private
from .TplLoader import *

class Officer(Private):
    def __init__(self, q, selfurl, rank = ' ' , salary = ' '):
        super(Officer, self).__init__(q, selfurl)
        self.rank = ''
        self.salary = ''
        
    def data_input(self,e):
        print(LoadTpl('OfficerForm').format(self.q['student'].value,self.url,e,self.name,self.surname,self.age,self.specialization, self.rank, self.salary))

    def edit(self,e):
        print(LoadTpl('OfficerForm').format(self.q['student'].value,self.url,e,self.name,self.surname,self.age,self.specialization, self.rank, self.salary))

    def save_input(self):
        self.name = self.q.getvalue('name')
        self.surname = self.q.getvalue('surname')
        self.age = self.q.getvalue('age')
        self.specialization = self.q.getvalue('specialization')
        self.rank = self.q.getvalue('rank')
        self.salary = self.q.getvalue('salary')
        
    def output(self, index):
        #print(self.name,' ', self.surname,' ', self.age,' ',self.specialization,' ',self.rank,' ',self.salary)
        print(LoadTpl('ElementShowOfficer').format(self.q['student'].value,self.url, self.name,self.surname,self.age,self.specialization, self.rank, self.salary,index))


