"""
OOP Exercise Chapter 6
Name: {Chanadda Rakkhaphan}
SID: {364211760005}
Group: {MIT221}

1. จงเขียนโปรแกรมภาษาไพธอนเพื่อสร้างคลาสพาหนะชื่อ Vehicle ที่ประกอบไปด้วยคุณลักษณะ (attributes) คือ 
ยี่ห้อรถ (brand) 
รุ่นรถ (model)
สีรถ (color)
ความเร็วสูงสุด (max speed)
ราคา (price)

2.จากข้อที่ 1 เขียนโปรแกรมเพื่อสร้างวัตถุ (object) จากคลาส Vehicle โดยรับข้อมูลจากผู้ใช้ตามคุณลักษณะ
 (attributes)ของคลาสจากนั้นแสดงข้อมูลทางหน้าจอภาพ

15 นาที
"""

class Vehicle:

    brand = input("Enter brand : ")
    model = input("Enter model : ")
    color = input("Enter color : ")
    max_speed = input("Enter max speed : ")
    price = input("Enter price : ")

    def __init__(self, brand, model, color, max_speed, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.max_speed = max_speed
        self.price = price

    print(f'Brand', brand, 'Model', model, 'Molor', color, 'Max speed', max_speed, 'Price', price, 'THB')

