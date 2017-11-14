from .part3 import *
import cgi


def main(q, selfurl):
        print ("Content-type: text/html; charset=utf-8\n\n")
        car=autopark(q,selfurl)
        car.tbl()
        if ("action" in q):
                if (q["action"].value == "2") or (q["action"].value == "3")  or (q["action"].value == "5") or (q["action"].value == "6") and (q["index"].value == "-1")  or (q["action"].value == "7") and (q["index"].value == "-1"):
                    car.add()
                    
                if (q["action"].value == "1"):
                    car.show_data()
                    
                if (q["action"].value == "8"):
                    car.clear_data()
                    
                if (q["action"].value == "4") or ((q["action"].value == "6") and (q["index"].value != "-1"))  or ((q["action"].value == "7") and (q["index"].value != "-1")):
                    car.edit()
                    
#main()
