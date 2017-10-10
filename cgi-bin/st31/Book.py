from .function import *


class Book:
	__title = ''
	__cost = ''
	__publishing_house = ''
	__author = ''
	id_book = 0

	def __init__(self, q):
		self.q = q

	def print_field(self):
		print(load_template('form_book').format(self.id_book, self.__title, self.__cost,
												self.__publishing_house,
												self.__author))

	def print_action(self):
		print(load_template('action_book'))

	def print_form(self):
		print(load_template('header_form').format(
			self.q.getvalue("student")))
		self.print_field()
		self.print_action()
		print(load_template('footer_form'))

	def book_registration(self, q):
		self.__title = none_to_nbsp(q.getvalue('title'))
		self.__cost = none_to_nbsp(q.getvalue('cost'))
		self.__publishing_house = none_to_nbsp(q.getvalue('publishing_house'))
		self.__author = none_to_nbsp(q.getvalue('author'))

	def show_book(self):
		print(load_template('cell').format(str(self.__class__.__name__)))
		print(load_template('cell').format(self.__title))
		print(load_template('cell').format(self.__cost))
		print(load_template('cell').format(self.__publishing_house))
		print(load_template('cell').format(self.__author))
