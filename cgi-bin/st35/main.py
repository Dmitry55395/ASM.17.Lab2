from .data_base import *

def main(q, selfurl):

	data_base = Data_Base(q, selfurl)

	print ("Content-type: text/html; charset=utf-8\n\n")
	if 'action' in q:
		if (q['action'].value == "1"):
			""" создаем форму для добавления в список кандидата без опыта (type=1) или с опытом (type=2)
			работы, либо считываем данные с заполненной формы (type=3), либо редактируем выбранного кандидата из списка (type=4) """
			data_base.read()
		if (q['action'].value == "2"):
			data_base.write()
		if (q['action'].value == "3"):
			data_base.delete() # удаляем выбранного кандидата из списка
	else:
		# выводим таблицу; добавляем ссылки 'назад' и 'редактировать'
		data_base.write()


