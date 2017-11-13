from .classContainerFIle import classContainer

#
def printMenu(q):
    print("Content-type: text/html; charset=utf-8\n\n")
    print('<form action="/cgi-bin/lab2.py" >')
    print('<input type="hidden" name = "action" value="editClassParam" />')
    print('<input type="hidden" name = "student" value={0} />'.format(int(q.getvalue('student'))))
    print('<a href="?student={0}&action=addClass">Добавить экземпляр класса родителя в лист</a><br>'.format(int(q.getvalue('student'))))
    print('<a href="?student={0}&action=addDescendantClass">Добавить экземпляр класса наследника в лист</a><br>'.format(int(q.getvalue('student'))))
    print('<a href="?student={0}&action=editClassParam">Редактировать выбранный экземпляр</a><br>'.format(int(q.getvalue('student'))))
    # print('   <input type="text" name= "i" value=''><br>')
    print('<a href="?student={0}&action=showList">Вывести список</a><br>'.format((q.getvalue('student'))))
    print('<a href="?student={0}&action=writeListInFile">Записать в файл</a><br>'.format((q.getvalue('student'))))
    print('<a href="?student={0}&action=readListFromFile">Считать с файла</a><br>'.format((q.getvalue('student'))))
    print('<a href="?student={0}&action=clearList">Очистить лист</a><br><br>'.format((q.getvalue('student'))))
    # print('Введите  имя:<input type="text" name= "name" value=''><br><br>')
    # print('Введите  параметр:<input type="text" name= "param" value=''><br><br>')
    # print('Введите дополнительный параметр(для наследника):<input type="text" name= "additionalAttribute" value=''><br><br>')
    # print('Введите второй дополнительный параметр(для наследника):<input type="text" name= "secondAdditionalAttribute" value=''><br><br>')
    print('</form>')

def main(q,selfurl):

    printMenu(q)
    classContainerExemplar = classContainer(q,selfurl)
    menu={}
    menu['addClass']=classContainerExemplar.addClass()
    menu['addDescendantClass']=classContainerExemplar.addDescendantClass()
    menu['editClassParam']=classContainerExemplar.editClassParam()
    menu['showList']=classContainerExemplar.showList()
    menu['writeListInFile']=classContainerExemplar.writeListInFile()
    menu['readListFromFile']=classContainerExemplar.readListFromFile()
    menu['clearList']=classContainerExemplar.clearList()

    # if q.getvalue('action')=='addclass':
    #      i =(q.getvalue('O_number'))
    #menu[i]()
    if 'action' in q:
        menu[q['action'].value]

if __name__=="__main__":
    main()


