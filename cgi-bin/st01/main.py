from .customers import *
import cgi

def add(customers, q, selfurl):
    #print("Нажмите 1 для добавления обычного клиента")
    #print("Нажмите 2 для добавления vip клиента")
    typeadd = q.getfirst("typeadd", None)
    #typeadd = input(" >>  ")
    try:
        add_actions[typeadd](customers, q, selfurl)
    except KeyError:
        print("Ошибка ввода! Попробуйте еще\n")
        add_actions['add'](customers, q, selfurl)
    global flag_action
    flag_action = 1
    return

def client(customers, q, selfurl):
    client = Client(q, selfurl)
    customers.load()
    customers.add(client)
    customers.save()
    return

def vipclient(customers, q, selfurl):
    vipclient = Vipclient(q, selfurl)
    customers.load()
    customers.add(vipclient)
    customers.save()
    return

add_actions = {
    'add': add,
    '1': client,
    '2': vipclient
}


def edit(customers, q, selfurl):
    editnum = q.getfirst("editnum", None)
    try:
        customers.edit(int(editnum)-1,q)
    except (ValueError, IndexError):
        print("Ошибка ввода!\n")
        edit(customers, q, selfurl)
    customers.save()
    global flag_action
    flag_action = 1
    return

def delete(customers, q, selfurl):
    delnum = q.getfirst("delnum", None)
    try:
        customers.delete(int(delnum)-1)
    except (ValueError, IndexError):
        print("Ошибка ввода!\n")
        delete(customers, q, selfurl)
    customers.save()
    global flag_action
    flag_action = 1
    return

def print_customers(customers, q, selfurl):
    print(customers)


def save(customers):
    customers.save()   
    print("Сохранено\n")

def load(customers, q, selfurl):
    customers.load()

    
def clear(customers):
    customers.clear()
    print("Очищено\n")
    return

def exit(customers):
    return

flag_action = 0

def main(q, selfurl):
    customers = Customers(q, selfurl)
    
    menu_actions['7'](customers, q, selfurl)
    action = q.getfirst("action", None)
    global flag_action
    if (flag_action):
        action = None
        flag_action = 0
    if action is not None:
        menu(action, q, selfurl,customers)
    else:
        print ("Content-type: text/html; charset=utf-8\n\n")
        print('''<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
              <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
              <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap-theme.min.css"> 
              <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>''')
        menu_actions['4'](customers, q, selfurl)
        print ('<br><div style="margin-top: 20px" class="container"><a href="{0}">Назад</a></div>'.format(selfurl))
    #choice = input(" >>  ")
    #menu(choice)

 
def menu(choice, q, selfurl, customers):
    try:
        menu_actions[choice](customers, q, selfurl)
    except KeyError:
        print("Ошибка ввода\n")
    if choice != '0':       
        menu_actions['main'](q, selfurl)


menu_actions = {
    'main': main,
    '1': add,
    '2': edit,
    '3': delete,
    '4': print_customers,
    #'5': clear,
    #'6': save,
    '7': load,
    #'0': exit,
}
 
if __name__ == "__main__":
    main()