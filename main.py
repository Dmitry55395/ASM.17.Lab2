from .Container import *
from .UIFunc import *
import os


class main:
    __Container: Container = None

    def __init__(self, Container, url, q):
        self.__Container = Container
        self.__url = url
        self.__q = q

    def show_content(self):
        content = {
            'show_menu': self.show_menu,
            'show_edit': self.__Container.show_edit,
            'save_PersonalCard': self.__Container.save_PersonalCard,
            'remove_PersonalCard': self.__Container.remove_PersonalCard,
			'save_EmployeeCard': self.__Container.save_EmployeeCard,
            'remove_EmployeeCard': self.__Container.remove_EmployeeCard,
            'clear_Container': self.__Container.clear
        }

        if 'action' in self.__q:
            content[self.__q['action'].value]()
        else:
            content['show_menu']()

    def show_menu(self):
        self.__Container.show_Container()
        print(Tpl_name('Container_menu').format(
            self.__q['student'].value,
            self.__url
        ))

def main(q, selfurl):
	print ("Content-type: text/html; charset=utf-8\n\n")
