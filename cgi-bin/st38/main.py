from .company import Company
import cgi 

def main(q, selfurl):
    print("Content-type: text/html; charset=utf-8\n\n") 
    comp = Company(q, selfurl)
    comp.menu() 
    if "action" in q: 
        if (q["action"].value == "0"):
            selfurl 
        if (q["action"].value == "1"):
            comp.show_list()
        if (q["action"].value == "2") or (q["action"].value == "3") or ((q["action"].value == "6") and (q["index"].value == "8")) or ((q["action"].value == "7") and (q["index"].value == "8")):
            comp.add()
        if (q["action"].value == "4") or ((q["action"].value == "6") and (int(q["index"].value)<len(comp.company)))  or ((q["action"].value == "7") and (int(q["index"].value)<len(comp.company))):
            comp.edit()
        if (q["action"].value=="5"):
            comp.delete()

