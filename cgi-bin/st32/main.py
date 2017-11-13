import os
__path__ = [os.path.dirname(os.path.abspath(__file__))]
from .Office import Office

def main(q,selfurl):
        office = Office(q,selfurl)
        func = {"1": ['Add a department', office.Add_Department],
                "2": ['Add an employee', office.Add_Employee],
                "3": ['Edit Database', office.EditDB],
                "4": ['Show Database', office.ShowDB],
                "5": ['Save Database', office.SaveDB],
                "6": ['Load Database', office.loadDB],
                "7": ['Clear the Database', office.ClearDB],
                "8": ['Form Add Department',office.Form_Add_Department],
                "9": ['Form Add Employee',office.Form_Add_Employee],
                "10": ['Form Edit Department',office.Form_Edit_Department],
                "11": ['Form Edit Employee',office.Form_Edit_Employee],
                "12": ['Delete',office.Delete]
        }

        print("""Content-type:text/html

<html>
<head><title>office</title></head>
<body>
<h3>Office</h3>""")
        
        try:
                func[q.getvalue("type")][1]()
        except Exception as e:
#                print(e, '<br>')
                func["4"][1]()
        print("""</body>
</html>""")
        func["5"][1]()

if __name__ == "__main__":
        main()





