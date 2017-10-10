from .Book import Book
from .function import *


class Classbook(Book):
	__subject = ''

	def print_action(self):
		print(load_template('action_classbook'))

	def print_field(self):
		Book.print_field(self)
		print(load_template('form_classbook').format(self.__subject))

	def book_registration(self, q):
		Book.book_registration(self, q)
		self.__subject = none_to_nbsp(q.getvalue('subject'))

	def show_book(self):
		Book.show_book(self)
		print(load_template('cell').format(self.__subject))
