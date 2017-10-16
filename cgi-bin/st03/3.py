from .Army import Staff


Military_unit=Staff()
menu = {"1":("Add object", Military_unit.add),
        "2":("Edit", Military_unit.edit),
        "3":("Delete object", Military_unit.delete),
        "4":("Show list", Military_unit.out),
        "5":("Save to file", Military_unit.write),
        "6":("Load from file", Military_unit.read),
        "7":("Exit", "")}


def main(selfurl,q):
    print("Content-type: text/html \n")
    print("<h1>Вот это меню</h1>")
     print("""
<form action="/cgi-bin/st03/main.py"  method="get">
        <input type="password" name='user_input'>
        <input type="submit">
    </form>""")
    user_input =q.getvalue('user_input')
    for key in menu:
        print(key + " " + menu[key][0])
            
        #if int(user_input) == 7:
        #    break
        menu[user_input][1]()

if __name__ == "__main__":
    main()
