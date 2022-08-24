"""
Name: {Chanadda Rakkhaphan}
SID: {364211760005}
Group: {MIT221}
"""

"""
เขียนโปรแกรมไพธอนเพื่อนำเลขบัตรประชาชนมาบวกกันเพื่อทำนายดวงชะตาดังนี้
• สร้างฟังก์ชันเพื่อหาผลรวมของเลขบัตรประชาชน โดยใช้ชื่อฟังก์ชั่นว่า sumPID()
• สร้างฟังชั่นชื่อ getFortune() เพื่อทำนายดวงชะตา ถ้าเป็นเลขคู่ให้ทำนายว่า your fortune is good
• ถ้าเป็นเลขคี่ ให้ทำนายว่า your fortune is very good

ใช้ฟังก์ชั่น split()
"""

def getPID():
    pid = input('Enter your PID : ') #str
    lpid = [int(x) for x in pid]
    return lpid #List

def getFortune(var):
        if var % 2 == 0:
            print('Your fortune is good')
        else:
            print('Your fortune is very good')


PID = getPID()
print(f'The data from user : {sum(PID)}')
print(f'The prediction result is : {getFortune(sum(PID))}')

print("Hello-MIT221")
