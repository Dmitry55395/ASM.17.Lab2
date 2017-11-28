import os, cgi, pickle, cgitb, sys, codecs

from .Stable import Stable

def loadTpl(file_name):
        with open(os.environ['PATH_TRANSLATED']+'/cgi-bin/st40/template/'+file_name+'.tpl', 'rt') as f:
                return f.read()
	
	
new_stable = Stable()

actions = {
	"show_list": new_stable.show_list,
	
	"add_horse": new_stable.add_horse,
	"add_sport_horse": new_stable.add_sport_horse,
    
	"show_horse": new_stable.show_horse,
	"show_sport_horse": new_stable.show_sport_horse,
	
    "show_edit_form": new_stable.show_edit_form,
    "clear": new_stable.clear,
 
    "delete": new_stable.delete,
    "edit_horse": new_stable.edit_horse
}


def main(q, self_url):
 action_name = q.getvalue('action', 'show_list')
 action = actions[action_name]
 print("Content-type: text/html; charset=utf-8\n\n")
 action(q, self_url)
	
	

	
