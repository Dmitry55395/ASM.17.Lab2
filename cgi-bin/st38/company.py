import pickle

from .emploee import Employee
from .developer import Developer
from .function import *

class Company:
    employees = []

    def __init__(self, q, selfurl):
	    self.q = q
	    self.selfurl = selfurl
	    try:
		    self.load_base()
	    except:
		    self.__base = {}
		    self.maxid = 0
		    print('!!! Базы не существует !!!')

    def add(self):
         ids = list(map(lambda e: e.id, self.employees))
        if len(ids) > 0:
            next_id = max(ids) + 1
        else:
            next_id = 1
        employee_type = input("Кого вы хотите добавить?\n1.Обычный сотрудник\n2.Разработчик\n")
        if employee_type == "1":
            employee = Employee(next_id)
        else:
            if employee_type == "2":
                employee = Developer(next_id)
            else:
                print("Ошибка! Неверный тип сотрудника")
                self.add()
                return
        self.employees.append(employee)

    def edit(self):
        employee = self.get_employee()
        if employee is not None:
            employee.edit()

    def remove(self):
        employee = self.get_employee()
        if employee is not None:
            self.employees.remove(employee)

    def print(self):
       print(load_template('header_table'))
		for i, item in enumerate(self.__base):
			print("<tr align = 'center' valign = 'middle'>")
			print(load_template('cell').format((i + 1)))
			self.__base[item].show_book()
			if self.__base[item].__class__.__name__ == 'Компания':
				print("""<td bgcolor="#FFF8DC"></td>""")
			print(load_template('column_action').format(self.selfurl, self.q.getvalue("student"),
														self.__base[item].id_book))

		print("""</table>""")

    def clear(self):
        self.employees.clear()

    def serialize(self):
        with open('cgi-bin/st38/company.db', 'wb') as f:
         pickle.dump((self.maxid, self.__base), f)

    def deserialize(self):
        with open('cgi-bin/st38/company.db', 'rb') as f:
           (self.maxid, self.__base) = pickle.load(f)

                
    def get_employee(self):
        try:
            id = int(input("Введите номер сотрудника, которого вы хотите отредактировать\n"))
        except:
            print("Ошибка! Введите число")
            self.get_employee()
            return
        employees = [e for e in self.employees if e.id == id]
        if len(employees) == 0:
            print("Сотрудника с таким номером не существует")
            return
        else:
            return employees[0]
