"""
Name: {Chanadda Rakkhaphan}
SID: {364211760005}
Group: {MIT221}
"""

class Student:
    #class attributes
    uni = "RUTS"

    def __init__(self,name,id,major):
        #object attributes
        self.name = name
        self.id = id
        self.major = major

    def introduce(self):
        print(f'My name is {self.name}, my id is {self.id} and I am studying in {self.major} major.')


s1 = Student("Chanadda Rakkhaphan", "005", "MIT")
s1.introduce()

s2 = Student("Phattraphon Rakkhaphan", "235", "DBM")
s2.introduce()

s1.major = "LM"
s1.introduce()

print(s1.uni)
print(s2.uni)

Student.uni = "PSU"
print(s1.uni)
print(s2.uni)