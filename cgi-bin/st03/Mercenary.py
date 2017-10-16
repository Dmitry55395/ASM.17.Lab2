from .Soldier import Private

class Officer(Private):
    def __init__(self, name = ' ', surname = ' ', age = ' ', specialization = ' ', rank = ' ' , salary = ' '):
        super(Officer, self).__init__(name , surname, age, specialization)
        self.rank = rank
        self.salary = salary
    def data_input(self):
        super(Officer, self).data_input()
        self.rank  = input("Rank: " ,)
        self.salary = input("Salary: " ,)
    def output(self):
        print(self.name,' ', self.surname,' ', self.age,' ',self.specialization,' ',self.rank,' ',self.salary)


