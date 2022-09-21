"""
Name: {Chanadda Rakkhaphan}
SID: {364211760005}
Group: {MIT221}
"""
class Labtop:
    my_labtop = []

    def __init__(self, no, brand, model, cpu, ram, display, storage, price):
        self.no = no
        self.brand = brand
        self.model = model
        self.cpu = cpu
        self.ram = ram
        self.display = display
        self.storage = storage
        self.price = price

    def display_labtop(self):
        print(f'No.:{self.no}, '
              f'Brand:{self.brand}, '
              f'Model:{self.model}, '
              f'CPU:{self.cpu}, '
              f'RAM(GB):{self.ram}, '
              f'Display(inch):{self.display}, '
              f'Storage(GB):{self.storage}, '
              f'Price:{self.price}')



