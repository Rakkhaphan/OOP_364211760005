"""
Name: {Chanadda Rakkhaphan}
SID: {364211760005}
Group: {MIT221}
"""

class Student:
    def __init__(self, name, id):
        #attributes
        self.name = name #public member
        self.__id = id #private member
    def __str__(self):
        print(f'Name: {self.name} ID: {self.__id}')


std = Student("Chanadda", "005")
#direct access
#print(std.name, std.__id)
std.__str__()

std.name = "Chonticha" #change data attributes
std.__str__()

std.__id = "026"
std.__str__()

#name mangling
print(std._Student__id)

std._Student__id = "026"
std.__str__()