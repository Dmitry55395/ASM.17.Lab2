import cgi, cgitb, os, sys, codecs

cgitb.enable()
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stdin = codecs.getreader("utf-8")(sys.stdin.detach())

import st00.main
import st01.main
import st02.main
import st03.main
import st05.main
import st07.main
import st09.main
import st10.main
import st16.main
import st17.main
import st21.main
import st22.main
import st23.main
import st24.main
import st26.main
import st28.main
import st30.main
import st31.main
import st33.main
import st34.main
import st35.main
import st38.main
import st39.main
import st42.main
import st20.main
import st37.main
#	добавить импорт своего модуля по шаблону 
#	import st<номер по журналу>.main


MENU = [
	["[00] Образец", st00.main.main],
	["[01] Абдуллатипова", st01.main.main],
        ["[02] Аганов", st02.main.main],
	["[03] Антипов", st03.main.main],
	["[05] Баганов", st05.main.main],
	["[07] Белова", st07.main.main],
	["[09] Беркита", st09.main.main],
	["[10] Бледных", st10.main.main],
	["[16] Гаврилов", st16.main.main],
	["[17] Григорян", st17.main.main],
	["[21] Иванов", st21.main.main],
	["[22] Ишмаметьев", st22.main.main],
	["[23] Кондрат", st23.main.main],
	["[24] Костырко", st24.main.main],
	["[26] Ларионов", st26.main.main],
	["[28] Макарик", st28.main.main],
	["[30] Николаева", st30.main.main],
	["[31] Паньшина", st31.main.main],
	["[33] Попова", st33.main.main],
	["[34] Проценко", st34.main.main],
	["[35] Сидоренко", st34.main.main],
	["[38] Солопеева", st38.main.main],
	["[39] Тимошин", st39.main.main],
        ["[42] Худояров", st42.main.main],
        ["[20] Зубарева", st20.main.main],
        ["[37] Смирнов", st37.main.main],

#		добавить пункт меню для вызова своей главной функции по шаблону:
#		["[<номер по журналу>] <Фамилия>", <ссылка на функцию>],
	]


def menu(selfurl):
	print ("Content-type: text/html; charset=utf-8\n\n")
	print ('<pre>------------------------------');
	for i, item in enumerate(MENU):
		print('<a href="{0}?student={1}">{2}</a>'.format(selfurl, i+1, item[0]))
	print ("------------------------------</pre>");


def main():
	q = cgi.FieldStorage()
	selfurl = os.environ['SCRIPT_NAME']
	st = int(q.getvalue('student', 0))
	if st > 0 and st <= len(MENU):
		MENU[st-1][1](q, selfurl)
	else:
		menu(selfurl)

main()
