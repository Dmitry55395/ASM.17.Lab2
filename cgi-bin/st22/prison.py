import pickle
import os
from .overseer import *


class Prison:
    FILENAME = "cgi-bin/st22/storage.pkl"

    def __init__(self, f_param, self_url):
        self.__stack = []
        self.__f_param = f_param
        self.__self_url = self_url
        self.__read_from_file()

    def get_data(self):
        self.__stack[int(self.__f_param.getvalue('id'))].get_data(self.__f_param)
        self.print_data()

    def add_prisoner(self):
        prisoner = Prisoner()
        self.__stack.append(prisoner)
        self.edit_stack()

    def add_overseer(self):
        overseer = Overseer()
        self.__stack.append(overseer)
        self.edit_stack()

    def edit_stack(self):
        print('<form>'
              '<input type="hidden" name="student" value="{}"> '
              '<input type="hidden" name="action" value="get_data">'
              .format(self.__f_param.getvalue('student')))
        if 'id' in self.__f_param:
            current_id = self.__f_param.getvalue('id')
        else:
            current_id = str(len(self.__stack) - 1)
        print('<input type="hidden" name="id" value="{}">'.format(current_id))
        print('<table align="center" border="0">')
        self.__stack[int(current_id)].edit_data()
        print('<td colspan="2" align="center">'
              '<input type="submit" value="Save changes"></td></form></table>')
        self.__write_to_file()

    def remove_person(self):
        self.__stack.pop(int(self.__f_param.getvalue('id')))
        self.print_data()

    def clear_list(self):
        self.__stack.clear()
        self.print_data()

    def print_data(self):
        print('<h2 align="center">Prison persons list</h2>'
              '<table width="800" align="center" border="2" cellspacing="0" cellpadding="0" bgcolor="#D3EDF6">'
              '<tr align="center"><td><b>First name</b></td><td><b>Last name</b></td><td><b>Age</b></td>'
              '<td><b>Salary</b></td><td><b>Phone number</b></td><td><b>Edit</b></td></tr>')
        i = 0
        for each in self.__stack:
            each.print_data()
            print('<td><a href={0}?student={1}&action=edit_stack&id={2}>Edit</a><a>&nbsp &nbsp</a>'
                  '<a href={0}?student={1}&action=delete_person&id={2}>Delete</a></td></tr></tr>'
                  .format(self.__self_url, self.__f_param.getvalue('student'), i))
            i += 1
        print('</table><br><br>'
              '<table align="center" border="0" cellspacing="0"><tr>'
              '<td><a  href={0}?student={1}&action=add_prisoner>Add prisoner</a><br>'
              .format(self.__self_url, self.__f_param.getvalue('student')),
              '</td></tr><tr><td><a href={0}?student={1}&action=add_overseer>Add overseer</a><br>'
              .format(self.__self_url, self.__f_param.getvalue('student')),
              '</td></tr><tr><td><a href={0}?student={1}&action=clear_list>Clear list</a><br>'
              .format(self.__self_url, self.__f_param.getvalue('student')),
              '</td></tr><tr><td><a href={0}>Previous page</a>'
              .format(self.__self_url),
              '</td></tr></table>')
        self.__write_to_file()

    def __write_to_file(self):
        pickle.dump(self.__stack, open(Prison.FILENAME, 'wb'))

    def __read_from_file(self):
        if (os.path.exists(Prison.FILENAME)):
            self.__stack = pickle.load(open(Prison.FILENAME, 'rb'))

