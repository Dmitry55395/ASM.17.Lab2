def is_float(value):
	try:
		float(value)
		return True
	except ValueError:
		return False


def is_int(value):
	try:
		int(value)
		return True
	except ValueError:
		return False

def print_header():
	print("Content-type: text/html; charset=utf-8\n\n")
	print("""<html> 
	    	 <head>
				 <title>Книжный магазин</title>
	    	 </head> 
	    	 <body>""")


def show_menu(q, selfurl):
	print("""<br><table width = '50%' align="center">
				<tr align="center">
					<td><h2>Работа с книгами</h2></td>
				</tr>
				<tr align="center">
					<td>
						<a href='{0}?type=show_form_book&student={1}'>Добавить книгу</a><br>
						<a href='{0}?type=show_form_classbook&student={1}'>Добавить учебник</a><br>
						<a href='{0}?type=clear_shop&student={1}'>Удалить базу</a><br>
						<a href='{0}'>В основное меню</a><br>
					</td>
				</tr>
			</table>""".format(selfurl, q.getvalue("student")))


def print_footer():
	print("</body></html>")

def none_to_nbsp(value):
	return value if value else ''
