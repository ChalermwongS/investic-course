
print (' ##### Arithmetic Operation #####')
# สร้างตัวแปร number โดยคำนวณ 1 บวก 2 คูณ 3 หาร 4.0
number = 1+2*3/4
print('number', number)
# หาทศนิยมจาก 11 หาร 3
remainder = 11%3
print('remainder', remainder)
# หาพื้นที่สี่เหลี่ยม แต่ละด้านมีค่าเท่ากับ 7
squared = 7**2
print('squared', squared)
# หาปริมาตรลูกบาศก์ แต่ละด้านมีค่าเท่ากับ 2
cubed = 2**3
print('cubed', cubed)
print('\n')
print (' ##### Using Operators with Strings #####')
# Using Operators with Strings
# ปริ้น hello 10 ครั้ง
lotsofhellos ='hello'*10
print(lotsofhellos)
#สร้างตัวเลข 1 ถึง 8 ในรูปแบบ list ที่มีเฉพาะเลขคู่ 
even_numbers = [2,4,6,8]
print(even_numbers)
#สร้างตัวเลข 1 ถึง 8 ในรูปแบบ list ที่มีเฉพาะเลขคู่
odd_numbers = [1,3,5,7]
print(even_numbers)
#นำ odd number กับ even number มาบวกกัน
all_numbers = odd_numbers + even_numbers
print(all_numbers)

print('\n')
print (' ##### String Operation #####')
#String Operation

# astring = "Hello world!"
# 1 หาจำนวนตัวอักษรคำว่า Hello World
astring = "Hello World"
string1 = len(astring)
print(string1)
# 2 slicing ตัวที่ 3 ถึง 7 ของคำว่า Hello World
string2 = astring[3:7]
print(string2)
# 3 slicing ตัวที่ 3 ถึง 7 ของคำว่า Hello World แต่เพิ่มที่ละ 2 ตัว
string3 = astring[3:7:2]
print(string3)
# 4 เปลี่ยนคำว่า Hello World ให้เป็นอักษรตัวพิมพ์ใหญ่
string4 = astring.upper()
print(string4)
# 5 เปลี่ยนคำว่า Hello World ให้เป็นอักษรตัวพิมพ์เล็ก
string5 = astring.lower()
print(string5)

