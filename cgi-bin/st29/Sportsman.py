from .function import *


class Sportsman:
	__full_name = ''
	__age = ''
	__rating = ''
	id_sportsman = 0

	def __init__(self, q):
		self.q = q

	def print_field(self):
		print(load_template('form_sportsman').format(self.id_sportsman, self.__full_name, self.__age,
												self.__rating))

	def print_action(self):
		print(load_template('action_sportsman'))

	def print_form(self):
		print(load_template('header_form').format(
			self.q.getvalue("student")))
		self.print_field()
		self.print_action()
		print(load_template('footer_form'))

	def sportsman_registration(self, q):
		self.__full_name = none_to_nbsp(q.getvalue('full_name'))
		self.__age = none_to_nbsp(q.getvalue('age'))
		self.__rating = none_to_nbsp(q.getvalue('rating'))

	def show_sportsman(self):
		print(load_template('cell').format(str(self.__class__.__name__)))
		print(load_template('cell').format(self.__full_name))
		print(load_template('cell').format(self.__age))
		print(load_template('cell').format(self.__rating))
		
