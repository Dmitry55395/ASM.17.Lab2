from .group import *
import cgi

def main(q, selfurl):
    print ("Content-type: text/html; charset=utf-8\n\n")
    y=group(q,selfurl)
    y.me()
        
    if ("i" in q):
        if (q["i"].value == "add_person") and (q["index"].value == "-1") or (q["i"].value == "ok") and (q["index"].value == "-1"): 
            y.add_person()
        if (q["i"].value == "add_new_person") and (q["index"].value == "-1") or (q["i"].value == "okok") and (q["index"].value == "-1"): 
            y.add_new_person()
        if (q["i"].value == "display_spisok"): 
            y.display_spisok()
        if (q["i"].value == "clean_out"): 
            y.clean_out()
        if (q["i"].value == "edit") and (q["index"].value != "-1") or (q["i"].value == "ok") and (q["index"].value != "-1")or(q["i"].value == "okok") and (q["index"].value != "-1"): 
            y.edit()
        if (q["i"].value == "delete") and (q["index"].value != "-1"): 
            y.delete()
