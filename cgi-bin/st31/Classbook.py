from .Book import Book
from .function import *


class Classbook(Book):
	__subject = ''

	def __init__(self, q):
		Book.__init__(self, q)

	def print_form(self):
		Book.print_form(self)

	def print_act(self):
		print("""<input type="hidden" name="type" value="save_classbook">""")

	def print_field(self):
		Book.print_field(self)
		print("""Предмет:<br>
				<input type="text" name="subject" value="{}"><br>""".format(self.__subject))

	def set_subject(self):
		self.__subject = input('Enter the subject to be learned using the book\n')

	def book_registration(self, q):
		Book.book_registration(self, q)
		self.__subject = none_to_nbsp(q.getvalue('subject'))

	def show_book(self):
		Book.show_book(self)
		print("""<td>{0}</td>""".format(self.__subject))
