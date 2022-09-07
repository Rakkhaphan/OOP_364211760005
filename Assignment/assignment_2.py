"""
Name: {Chanadda Rakkhaphan}
SID: {364211760005}
Group: {MIT221}
"""

myList = [10, 20, 30, 40, 50]
# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList)
# แสดงผลข้อมูล 20 จาก myList
print(myList[1])
# แสดงผลข้อมูล 50 จาก myList
print(myList[4])

# แสดงผลข้อมูล {20,30,40} โดยใช้ range index
print(myList[1:4])
# แสดงผลข้อมูล {40,50} โดยใช้ range index
print(myList[3:5])
# แสดงผลข้อมูล {10,20} โดยใช้ range negative index
print(myList[0:2])

# แสดงผลข้อมูลใน myList ทั้งหมด โดยการใช้ while loop
i = 0
while i < len(myList):
    print(myList[i])
    i += 1

# แสดงผลข้อมูลใน myList ทั้งหมด โดยการใช้ for loop
for x in range(len(myList)):
    print(myList[x])

# เพิ่มข้อมูล 100,200,300 ใน myList
myList.append(100)
myList.append(200)
myList.append(300)
print(myList)
# เพิ่มข้อมูล 400 ใน myList ในตำแหน่งที่ 0
myList.insert(0,400)
print(myList)
# เพิ่มข้อมูล 500 ใน myList ในตำแหน่งที่ 3
myList.insert(3,500)
print(myList)
# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList)

# ลบข้อมูล 10
myList.remove(10)
print(myList)
# ลบข้อมูล 100
myList.remove(100)
print(myList)
# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList)
# ลบข้อมูลตำแหน่งสุดท้ายใน myList
myList.pop(7)
# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList)

# เรียงข้อมูล myList จาก น้อย-มาก
myList.sort()
# แสดงผลข้อมูลใน myList ทั้งหมด
print('myList จาก น้อย-มาก :', myList)
# เรียงข้อมูล myList จาก มาก-น้อย
myList.sort(reverse=True)
# แสดงผลข้อมูลใน myList ทั้งหมด
print('myList จาก มาก-น้อย :', myList)

# comprehension
myList=[45, 22, 56, 99, 34]
# คัดลอกข้อมูลใน myList ที่มีค่ามากกว่า 50 มาเก็บไว้ใน newList
newList = [x for x in myList if x >= 50]
# แสดงผลข้อมูลใน newList ทั้งหมด
print(newList)

# นำข้อมูลใน mylist และ newList มารวมกัน และเก็บไว้ในตัวแปร myFinalList
myFinalList = myList+newList
# แสดงผลข้อมูลใน myFinalList ทั้งหมด
print(myFinalList)