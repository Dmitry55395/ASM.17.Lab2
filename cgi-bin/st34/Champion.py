from .Sportsman import Sportsman
from .function import *


class Champion(Sportsman):
	__wins = ''

	def print_action(self):
		print(load_template('action_champion'))

	def print_field(self):
		Sportsman.print_field(self)
		print(load_template('form_champion').format(self.__wins))

	def sportsman_registration(self, q):
		Sportsman.sportsman_registration(self, q)
		self.__wins = none_to_nbsp(q.getvalue('wins'))

	def show_sportsman(self):
		Sportsman.show_sportsman(self)
		print(load_template('cell').format(self.__wins))
