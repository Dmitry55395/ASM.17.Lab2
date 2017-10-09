from .BookShop import BookShop
from .function import *


def main(q, selfurl):
	book_shop = BookShop(q, selfurl)
	menu = {
		'show_form_book': book_shop.show_form_book,
		'show_form_classbook': book_shop.show_form_classbook,
		'save_book': book_shop.add_book,
		'save_classbook': book_shop.add_classbook,
		'delete_book': book_shop.delete_book,
		'clear_shop': book_shop.clear_shop,
	}

	print("Content-type: text/html; charset=utf-8\n\n")
	load_template('header')

	if 'type' in q:
		try:
			menu[q.getvalue('type')]()
			book_shop.show_base()
			show_menu(q, selfurl)
		except Exception as e:
			print(e, '<br>')
	else:
		book_shop.show_base()
		show_menu(q, selfurl)

	load_template('footer')
	book_shop.save_base()
