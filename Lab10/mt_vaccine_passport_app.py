"""
Name: {Chanadda Rakkhaphan}
SID: {364211760005}
Group: {MIT221}
"""

from model import Person, Student, Vaccine, Vaccine_Passport

p1 = Person("Chanadda", 22, 63.4, 155)

v1 = Vaccine("Sinovac")
d1 = "10/7/2565"

vp1 = Vaccine_Passport(p1)

vp1.vaccine_passport_info()
vp1.add_vaccine(v1)
vp1.add_date(d1)
vp1.vaccine_passport_info()

v2 = Vaccine("Sinovac")
d2 = "20/10/2565"
vp1.add_vaccine(v2)
vp1.add_date(d2)
vp1.vaccine_passport_info()

s1 = Student("Chonticha", 25, 48.5, 170, "MIT")

v3 = Vaccine("Astrazeneca")
d3 = "26/10/2565"

vp2 = Vaccine_Passport(s1)
vp2.add_vaccine(v3)
vp2.add_date(d3)
vp2.vaccine_passport_info()