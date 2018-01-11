from .Sportsman import Sportsman
from .Champion import Champion
from .function import *
import pickle


class Sportclub():
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
		with open('cgi-bin/st29/sportclub.db', 'rb')as f:
			(self.maxid, self.__base) = pickle.load(f)

	def save_base(self):
		with open('cgi-bin/st29/sportclub.db', 'wb')as f:
			pickle.dump((self.maxid, self.__base), f)

	def get_sportsman(self, id_sportsman):
		if id_sportsman <= 0:
			return Sportsman(self.q)
		else:
			return self.__base[int(id_sportsman)]

	def get_champion(self, id_sportsman):
		if id_sportsman <= 0:
			return Champion(self.q)
		else:
			return self.__base[int(id_sportsman)]

	def show_form_sportsman(self):
		id_sportsman = int(self.q.getvalue('id_sportsman', 0))
		self.get_sportsman(id_sportsman).print_form()

	def add_sportsman(self):
		id_sportsman = int(self.q.getvalue('id_sportsman', 0))
		sportsman = self.get_sportsman(id_sportsman)
		sportsman.sportsman_registration(self.q)
		if id_sportsman <= 0:
			self.maxid += 1
			sportsman.id_sportsman = self.maxid
			self.__base[self.maxid] = sportsman

	def show_form_champion(self):
		id_sportsman = int(self.q.getvalue('id_sportsman', 0))
		self.get_champion(id_sportsman).print_form()

	def add_champion(self):
		id_sportsman = int(self.q.getvalue('id_sportsman', 0))
		Champion = self.get_champion(id_sportsman)
		Champion.sportsman_registration(self.q)
		if id_sportsman <= 0:
			self.maxid += 1
			Champion.id_sportsman = self.maxid
			self.__base[self.maxid] = Champion

	def show_base(self):
		print(load_template('header_table'))
		for i, item in enumerate(self.__base):
			print("<tr align = 'center' valign = 'middle'>")
			print(load_template('cell').format((i + 1)))
			self.__base[item].show_sportsman()
			if self.__base[item].__class__.__name__ == 'Sportsman':
				print("""<td bgcolor="#000000"</td>""")
			print(load_template('column_action').format(self.selfurl, self.q.getvalue("student"),
														self.__base[item].id_sportsman))

		print("""</table>""")

	def delete_sportsman(self):
		try:
			del self.__base[int(self.q.getvalue("id_sportsman"))]
		except Exception as e:
			print(e, '<br>')
		self.maxid -= 1

	def clear_base(self):
		self.__base = {}
		self.maxid = 0
