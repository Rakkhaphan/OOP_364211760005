"""
Name: {Chanadda Rakkhaphan}
SID: {364211760005}
Group: {MIT221}
"""
class Labtop:
    my_labtop = []


    def __init__(self, brand, model, cpu, ram, display, storage, price):
        self.__brand = brand
        self.__model = model
        self.__cpu = cpu
        self.__ram = ram
        self.__display = display
        self.__storage = storage
        self.__price = price
        self.my_labtop.append(self)

        # getter and setter

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_cpu(self):
        return self.__cpu

    def set_cpu(self, cpu):
        self.__cpu = cpu

    def get_ram(self):
        return self.__ram

    def set_ram(self, ram):
        self.__ram = ram

    def get_display(self):
        return self.__display

    def set_display(self, display):
        self.__display = display

    def get_storage(self):
        return self.__storage

    def set_storage(self, storage):
        self.__storage = storage

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price


    def display_labtop(self):
        print(f'Brand:{self.__brand}, '
              f'Model:{self.__model}, '
              f'CPU:{self.__cpu}, '
              f'RAM(GB):{self.__ram}, '
              f'Display(inch):{self.__display}, '
              f'Storage(GB):{self.__storage}, '
              f'Price:{self.__price}')







