from st20.car_park import car_park

def main(q,selfurl):
    cp=car_park(q,selfurl)
    cpf={"add_car":cp.add_car,
         "add_truck":cp.add_truck,
         "edit":cp.edit,
         "clear":cp.clear,
         "show":cp.show,
         "safe":cp.safe,
         "load":cp.load,
         "delete":cp.delete,
         "show_add_car":cp.show_add_car,
         "show_add_truck":cp.show_add_truck,
         "show_edit":cp.show_edit}
    
    print("""Content-type:text/html

<html>
<head><title>car park</title></head>
<body>
<h3>Car Park</h3>""")
    
    try:
        cpf[q.getvalue("type")]()
    except Exception as e:
        #print(e, '<br>')
        cpf["show"]()

    print("""</body>
</html>""")
    cpf["safe"]()

if __name__ == "__main__":
    main()
