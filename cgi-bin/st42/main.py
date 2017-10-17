from .platform import *
import cgi


def main(q, selfurl):
        print ("Content-type: text/html; charset=utf-8\n\n")
        rig = Platform(q,selfurl)
        rig.intro()
        if ("action" in q):
                if (q["action"].value == "2") or (q["action"].value == "3")  or (q["action"].value == "5") or (q["action"].value == "6") and (q["index"].value == "-1")  or (q["action"].value == "7") and (q["index"].value == "-1"):
                    rig.adding()
                    
                if (q["action"].value == "1"):
                    rig.show_atribut()
                    
                if (q["action"].value == "8"):
                    rig.clear_atribut()
                    
                if (q["action"].value == "4") or ((q["action"].value == "6") and (q["index"].value != "-1"))  or ((q["action"].value == "7") and (q["index"].value != "-1")):
                    rig.edit()
