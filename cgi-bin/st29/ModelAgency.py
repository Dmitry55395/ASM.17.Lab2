from .SuperModel import *
import pickle


class ModelAgency:
    def __init__(self, q, instance_url):
        self.agency = []
        self.__q = q
        self.__instance_url = instance_url

    def show_agency_and_menu(self):
        student_id = self.__q['student'].value
        self.read_file()

        if len(self.agency) != 0:
            print('<table border="1" border cellspacing="0" cellpadding=5 align=center >')
            print('<tr><th>#</th><th>Surname</th><th>Name</th><th>Age</th><th>Growth</th><th>Weight</th><th>Magazine</th'
                  '><th></th></tr>')
            for i, model in enumerate(self.agency):
                model.show_self(self.__q, i)
            print('</table>')

        print(f'''
            <br><fieldset style="width:400px; margin: auto; text-align: center">
            <a href="?student={student_id}&model_id=-1&is_supermodel=0&action=show_edit">Add model</a>&nbsp&nbsp&nbsp
            <a href="?student={student_id}&model_id=-1&is_supermodel=1&action=show_edit">Add supermodel</a>&nbsp&nbsp&nbsp
            <a href="?student={student_id}&model_id=-1&action=clear_agency">Clear agency</a>
            <br><a href="{self.__instance_url}">Back</a>
            </fieldset>
            ''')

    def save_model(self):
        model_id = int(self.__q['model_id'].value)

        self.read_file()

        if model_id == -1:
            is_supermodel = int(self.__q['is_supermodel'].value)
            model = Model() if is_supermodel == 0 else SuperModel()

            model.edit_self(self.__q)
            self.agency.append(model)
        else:
            model = self.agency[model_id]
            model.edit_self(self.__q)

        self.write_file()

        self.__back_to_menu()

    def show_model_edit(self):
        model_id = int(self.__q['model_id'].value)
        is_supermodel = int(self.__q['is_supermodel'].value)
        if model_id == -1:
            model = Model() if is_supermodel == 0 else SuperModel()
        else:
            self.read_file()
            model = self.agency[model_id]

        print('<form action="/cgi-bin/lab2.py" align="center">')
        print('<table align="center" border=0>')
        print(f'<input type="hidden" name = "student" value={self.__q["student"].value} />')
        print(f'<input type="hidden" name = "model_id" value={self.__q["model_id"].value} />')
        print(f'<input type="hidden" name = "is_supermodel" value={self.__q["is_supermodel"].value} />')
        print('<input type="hidden" name = "action" value="save_model" />')
        print(f'<a href="{self.__instance_url}?student={self.__q["student"].value}">Back to the menu</a><br>')
        print(f'<tr><td>Surname</td><td><input value = "{model.surname}" type="text" name="surname"></td></tr>')
        print(f'<tr><td>Name</td><td><input value = "{model.name}" type="text" name="name"><br></td></tr>')
        print(f'<tr><td>Age</td><td><input value = "{model.age}" type="text" name="age"><br></td></tr>')
        print(f'<tr><td>Growth</td><td><input value = "{model.growth}" type="text" name="growth"><br></td></tr>')
        print(f'<tr><td>Weight</td><td><input value = "{model.weight}" type="text" name="weight"><br></td></tr>')
        if is_supermodel == 1:
            print(f'<tr><td>Magazine</td><td><input value = "{model.magazine}" type="text" name="magazine"><br></td></tr>')
        print('<tr><td colspan=2 align=center><input value="Save" type="submit" style="width:100px"></td></tr>')
        print('</table></form>')

    def remove_model(self):
        model_id = int(self.__q['model_id'].value)

        self.read_file()
        del self.agency[model_id]
        self.write_file()

        self.__back_to_menu()

    def clear_agency(self):
        self.read_file()
        self.agency.clear()
        self.write_file()

        self.__back_to_menu()

    def write_file(self):
        f = open('cgi-bin/st29/Storage/agency.dat', 'wb')
        pickle.dump(self.agency, f)
        f.close()

    def read_file(self):
        f = open('cgi-bin/st29/Storage/agency.dat', 'rb')
        self.agency = pickle.load(f)
        f.close()

    def __back_to_menu(self):
        print('<meta http-equiv=refresh content="0; URL=http://localhost{0}?student={1}">'
              .format(self.__instance_url, self.__q['student'].value))
