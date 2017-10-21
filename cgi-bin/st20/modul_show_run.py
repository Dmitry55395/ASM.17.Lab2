def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def is_file(value):
    try:
        open("st21/"+value, 'rb')
        return True
    except FileNotFoundError:
        return False

def show_menu():
    return input("""
add_car - add car
add_truck - add truck
edit - edit car
clear - clear car park
show - show car park
safe - safe car park in file
load - load car park form file
exit - exit
""")

def run_f_car_park(cpf):
    cpf()
