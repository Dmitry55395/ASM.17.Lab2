from .function import *


class Book:
	__title = ''
	__cost = ''
	__publishing_house = ''
	__author = ''
	id_book = 0
	field = ''

	def __init__(self, q):
		self.q = q

	def print_field(self):
		print("""<input type="hidden" name="id_book" value="{0}">
				Название:<br>
				<input type="text" name="title" value="{1}" autofocus><br>
				Стоимость:<br>
				<input type="text" name="cost" value="{2}"><br>
				Издательство:<br>
				<input type="text" name="publishing_house" value="{3}"><br>
				Автор:<br>
				<input type="text" name="author" value="{4}"><br>""".format(self.id_book, self.__title, self.__cost,
																			self.__publishing_house,
																			self.__author))

	def print_act(self):
		print("""<input type="hidden" name="type" value="save_book">""")

	def print_form(self):
		print("""<br>
				<table width = '50%' align="center">
					<tr align="center">
						<td><h3>Заполните информацию о книге</td>
					</tr>	
					<tr align="center">
						<td> 
							<form action="/cgi-bin/lab2.py">
								<input type="hidden" name="student" value="{0}">
								""".format(
			self.q.getvalue("student")))
		self.print_field()
		self.print_act()
		print("""				<input type="submit">
							</form>
						</td>
					</tr>
			</table>""")

	def book_registration(self, q):
		self.__title = none_to_nbsp(q.getvalue('title'))
		self.__cost = none_to_nbsp(q.getvalue('cost'))
		self.__publishing_house = none_to_nbsp(q.getvalue('publishing_house'))
		self.__author = none_to_nbsp(q.getvalue('author'))

	def show_book(self):
		print("""<td>{0}</td>
 				 <td>{1}</td>
 				 <td>{2}</td>
 				 <td>{3}</td>
 				 <td>{4}</td>""".format(str(self.__class__.__name__), self.__title, self.__cost,
										 self.__publishing_house,
										 self.__author))
