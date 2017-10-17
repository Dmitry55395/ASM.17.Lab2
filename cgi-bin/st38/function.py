import os


def load_template(tpl_name):
	with open(os.environ['PATH_TRANSLATED'] +
					  '/cgi-bin/st31/template/' +
					  tpl_name + '.tpl', 'r') as f:
		return f.read()


def show_menu(q, selfurl):
	print(load_template('menu').format(selfurl, q.getvalue("student")))


def none_to_nbsp(value):
	return value if value else ''
