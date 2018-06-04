from .Devices import *

def main(q, selfurl):
    print("Content-type: text/html;\n")
    dev = Devices (q, selfurl)
    dev.rec()

    if ("act" in q):
        if (q["act"].value == "add_phone") and (q["index"].value == "-1") or (q["act"].value == "ph") and (
                q["index"].value == "-1"):
            dev.add_phone()

        if (q["act"].value == "add_smartphone") and (q["index"].value == "-1") or (q["act"].value == "sph") and (
                q["index"].value == "-1"):
            dev.add_smartphone()

        if q["act"].value == "display_list":
            dev.display_list()

        if q["act"].value == "clear_list":
            dev.clear_list()

        if (q["act"].value == "edit") and (q["index"].value != "-1") or (q["act"].value == "ph") and (
                q["index"].value != "-1") or (q["act"].value == "sph") and (q["index"].value != "-1"):
            dev.edit_device()

        if (q["act"].value == "delete") and (q["index"].value != "-1"):
            dev.delete_device()


