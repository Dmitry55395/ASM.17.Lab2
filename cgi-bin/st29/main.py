from .Sportclub import Sportclub
from .function import *


def main(q, selfurl):
	sport_club = Sportclub(q, selfurl)
	menu = {
		'show_form_sportsman': sport_club.show_form_sportsman,
		'show_form_champion': sport_club.show_form_champion,
		'save_sportsman': sport_club.add_sportsman,
		'save_champion': sport_club.add_champion,
		'delete_sportsman': sport_club.delete_sportsman,
		'clear_base': sport_club.clear_base,
	}

	print("Content-type: text/html; charset=utf-8\n\n")
	load_template('header')

	if 'type' in q:
		try:
			menu[q.getvalue('type')]()
			sport_club.show_base()
			show_menu(q, selfurl)
		except Exception as e:
			print(e, '<br>')
	else:
		sport_club.show_base()
		show_menu(q, selfurl)

	load_template('footer')
	sport_club.save_base()


if __name__ == "__main__":
	main()
