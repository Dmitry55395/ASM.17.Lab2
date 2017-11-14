from .dinner import *
import cgi

def main(q, selfurl):
    print ("Content-type: text/html; charset=utf-8\n\n")
    y=dinner(q,selfurl)
    y.me()
        
    if ("j" in q):
        if (q["j"].value == "add_food") and (q["index"].value == "-1") or (q["j"].value == "ok") and (q["index"].value == "-1"): 
            y.add_food()
        if (q["j"].value == "add_drink") and (q["index"].value == "-1") or (q["j"].value == "okok") and (q["index"].value == "-1"): 
            y.add_drink()
        if (q["j"].value == "all_"): 
            y.all_()
        if (q["j"].value == "clear"): 
            y.clear()
        if (q["j"].value == "edit") and (q["index"].value != "-1") or (q["j"].value == "ok") and (q["index"].value != "-1")or(q["j"].value == "okok") and (q["index"].value != "-1"): 
            y.edit()
        if (q["j"].value == "delete") and (q["index"].value != "-1"): 
            y.delete()
                    
