from .catalog import Catalog



def main(q, selfurl):
	cat = Catalog(q, selfurl)
	user_menu = {"plus_dc" : cat.plus_dc,
				 "plus_dcsh" : cat.plus_dcsh,
				 "print" : cat.print,
				 "rewrite" : cat.rewrite,
				 "delete" : cat.delete,
				 "clear_catalog" : cat.clear_catalog
				 }

	print("Content-type: text/html; charset=utf-8\n\n")  # Определение типа HTML, http-заголовок плюс пустая строка
	cat.mn()
	if ("i" in q):
		if (q['i'].value in user_menu) :
			user_menu[q['i'].value ] ()

	cat.write_file()

#в атрибуте action этой формы определяется сценарий, который будет обрабатывать ее
