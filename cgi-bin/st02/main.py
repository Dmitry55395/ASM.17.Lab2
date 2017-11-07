from .Library import *
import pickle, cgi, cgitb, codecs, sys, os, datetime
cgitb.enable()
#sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

def main(q, selfurl):
    print ("Content-type: text/html; charset=utf-8\n\n")
    lib = Library(q, selfurl)
    lib.readFromFile()
##    print ("""
##<html>
##<head>
##<title>Library</title>
##</head>
##<body>""")
    
    MENU = {
        'show_form' : lib.showForm,
        'add_guest' : lib.addGuest,
        'add_reg' : lib.addReg,
        'edit_reg' : lib.edit_student,
        'edit_guest' : lib.edit_student,
        'delete' : lib.delete,
        'clear' : lib.clear,
        'save_guest' : lib.save_student,
        'save_reg' : lib.save_student}

    MENU[q.getvalue('act', 'show_form')]()
    lib.writeToFile()
##    print ("</body></html>")

