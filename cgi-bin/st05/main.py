from .squad import *
import cgi


def main(q, selfurl):
        print ("Content-type: text/html; charset=utf-8\n\n")
        war=Squad(q,selfurl)
        war.tbl()
        if ("action" in q):
                if (q["action"].value == "2") or (q["action"].value == "3")  or (q["action"].value == "5") or (q["action"].value == "6") and (q["index"].value == "-1")  or (q["action"].value == "7") and (q["index"].value == "-1"):
                    war.add()
                    
                if (q["action"].value == "1"):
                    war.show_spisok()
                    
                if (q["action"].value == "8"):
                    war.clear_spisok()
                    
                if (q["action"].value == "4") or ((q["action"].value == "6") and (q["index"].value != "-1"))  or ((q["action"].value == "7") and (q["index"].value != "-1")):
                    war.edit()
                    
#main()
