import cgi, pickle, cgitb, codecs, sys, datetime, os
from .Book import Book
from .Classbook import Classbook
from .function import *
import pickle


class BookShop():
	__base = {}

	def __init__(self, q, selfurl):
		self.q = q
		self.selfurl = selfurl
		try:
			self.load_base()
		except:
			self.__base = {}
			self.maxid = 0
			print('!!! base does not exist !!!')

	def load_base(self):
		with open('cgi-bin/st31/book.db', 'rb')as f:
			(self.maxid, self.__base) = pickle.load(f)

	def save_base(self):
		with open('cgi-bin/st31/book.db', 'wb')as f:
			pickle.dump((self.maxid, self.__base), f)

	def get_book(self, id_book):
		if id_book <= 0:
			return Book(self.q)
		else:
			return self.__base[int(id_book)]

	def get_classbook(self, id_book):
		if id_book <= 0:
			return Classbook(self.q)
		else:
			return self.__base[int(id_book)]

	def show_form_book(self):
		id_book = int(self.q.getvalue('id_book', 0))
		self.get_book(id_book).print_form()

	def add_book(self):
		id_book = int(self.q.getvalue('id_book', 0))
		book = self.get_book(id_book)
		book.book_registration(self.q)
		if id_book <= 0:
			self.maxid += 1
			book.id_book = self.maxid
			self.__base[self.maxid] = book

	def show_form_classbook(self):
		id_book = int(self.q.getvalue('id_book', 0))
		self.get_classbook(id_book).print_form()

	def add_classbook(self):
		id_book = int(self.q.getvalue('id_book', 0))
		Classbook = self.get_classbook(id_book)
		Classbook.book_registration(self.q)
		if id_book <= 0:
			self.maxid += 1
			Classbook.id_book = self.maxid
			self.__base[self.maxid] = Classbook

	def show_base(self):
		print("""<table width = '50%' align="center">
					<tr align = 'center'>
						<td><h1>Книжный магазин</td>
					</tr> 
				 </table>
				 <table width = '70%' align="center" border = '1' cellspacing="0">
					<tr align = 'center' valign = 'middle'>
						<td width = '1'><b>№</td>
						<td><b>Тип</td>
						<td><b>Название</td>
						<td><b>Стоимость</td>
						<td><b>Издательство</td>
						<td><b>Автор</td>
						<td><b>Предмет</td>
						<td></td>
						<td></td>
					</tr>""")
		for i, item in enumerate(self.__base):
			print("""<tr align = 'center' valign = 'middle'>
						<td>
							{}
						</td>""".format((i + 1)))
			self.__base[item].show_book()
			if self.__base[item].__class__.__name__ == 'Book':
				print("""<td bgcolor="#FFF8DC"></td>""")
			print("""<td>
						<a href='{0}?type=delete_book&student={1}&id_book={2}'>Удалить</a><br>
					</td>
					<td>
						<a href='{0}?type=show_form_book&student={1}&id_book={2}'>Редактировать</a><br>
					</td>
			</tr>""".format(self.selfurl, self.q.getvalue("student"), self.__base[item].id_book))

		print("""</table>""")

	def delete_book(self):
		try:
			del self.__base[int(self.q.getvalue("id_book"))]
		except Exception as e:
			print(e, '<br>')
		self.maxid -= 1

	def clear_shop(self):
		self.__base = {}
		self.maxid = 0
