from .part3 import *
import cgi


def main(q, selfurl):
        print ("Content-type: text/html; charset=utf-8\n\n")
        cars = autopark(q,selfurl)
        cars.table()
        if ("action" in q):
                if (q["action"].value == "2") or (q["action"].value == "3")  or (q["action"].value == "5") or (q["action"].value == "6") and (q["index"].value == "-1")  or (q["action"].value == "7") and (q["index"].value == "-1"):
                    cars.add()
                    
                if (q["action"].value == "1"):
                    cars.show_data()
                    
                if (q["action"].value == "8"):
                    cars.clear_data()
                    
                if (q["action"].value == "4") or ((q["action"].value == "6") and (q["index"].value != "-1"))  or ((q["action"].value == "7") and (q["index"].value != "-1")):
                    cars.edit()
