import cgi

from .University import *


def main(q: cgi.FieldStorage, self_url):
    RSU = University(self_url, q)
    student_id = int(q.getvalue('student', 0))
    Menu.response_ok()
    menu = Menu(RSU, self_url, student_id)

    if 'act' not in q:
        menu.show_menu(self_url, student_id)
    else:
        act_id = int(q.getvalue('act', Menu.EXIT_CODE))
        if act_id == -1:  # remove
            RSU.remove_man(q.getvalue('id'))
            return
        menu.start(act_id)
