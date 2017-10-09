import cgi, pickle,cgitb,codecs,sys,datetime,os
def IsFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def IsInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def IsFile(value):
    try:
        open(value, 'rb')
        return True
    except FileNotFoundError:
        return False

def ShowList():
    i = input("""
0 - добавить обычное блюдо
1 - добавить VIP блюдо
2 - редактировать блюдо
3 - очистить меню
4 - вывести на экран меню
5 - сохранить меню в файл
6 - загрузить меню из файла
other numbers - выход
""")
    while(True):
        if IsInt(i):
            return i
        else:
            i = input("""
0 - добавить обычное блюдо
1 - добавить VIP блюдо
2 - редактировать блюдо
3 - очистить меню
4 - вывести на экран меню
5 - сохранить меню в файл
6 - загрузить меню из файла
other numbers - выход
""")

def MenuFunction(l):
    l()
