"""
Name: {Chanadda Rakkhaphan}
SID: {364211760005}
Group: {MIT221}
"""

from Laptop import Labtop

# display
def display_laptop():
    if len(my_labtop) == 0:
        print("You had no laptop data.")
    else:
        print(f'You had {len(my_labtop)} following')
    for x in my_labtop:
        x.display_labtop()
    print("\n")

# option
def display_option_system():
    print("Welcome to Laptop Data Store System")
    print("1.เพิ่มข้อมูล Laptop")
    print("2.แสดงข้อมูล Laptop")
    print("3.ออกจากระบบ")
    select = int(input("select(1-3)? : "))
    if select == 1:
        input_laptop_data()
    elif select == 2:
        display_laptop()
    elif select == 3:
        print("Good Bye.")
        exit(0)
    else:
        print("Please, select number 1-3.")

# input data
def input_laptop_data():
    brand = input("Enter laptop brand : ")
    model = input("Enter laptop model : ")
    cpu = input("Enter laptop CPU : ")
    ram = int(input("Enter laptop RAM(GB) : "))
    display = float(input("Enter laptop display(inch) : "))
    storage = int(input("Enter laptop storage(GB) : "))
    price = int(input("Enter laptop price : "))

    my_labtop.append(Labtop(brand, model, cpu, ram, display, storage, price))
    print("\n------------------------------------")
    print("Already add laptop to store.")
    print("--------------------------------------")

my_labtop = []
s = 0
while s == 0:
    display_option_system()