print("Hello world")
name = "Chayakorn Poomoonmueang"
print(name)
print(456)
print(3.14)

#name = input("กรุณากรอกชื่อของคุณ : ")
#print("Hello "+name)

age = 20
height = 160.5
name = "Chayakorn"
is_Student = True

print(type(age))
print(type(height))
print(type(name))  
print(type(is_Student))

a = 10
b = 3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

print(a>b)
print(a<b)
print(a==b)
print(a!=b)

score = input ("กรุณากรอกคะแนน : ")
score = int(score)
if score >= 80:
 print("ดีเยี่ยม")
elif score >= 75:
 print("ดีมาก")
elif score >= 70:
 print("ดี")
elif score >= 65:
 print("ค่อนข้างดี")
elif score >= 60:
 print("ปานกลาง")
elif score >= 55:
 print("พอใช้")
elif score >= 50:
 print("ผ่านเกณฑ์ขั้นต่ำ")
else:
 print("ต่ำกว่าเกณฑ์")

 for i in range(1,6):
  print("รอบที่ ", i )

  count = 1
  while count <=5:
   print("นับ",count)
   count +=1

total = 0
for i in range(5):
  num = float(input(f"กรอกครั้งที่ {i+1} :"))
  total += num
  average = total/5
  print(f"\nรวมทั้งหมด{total}")
  print(f"\nค่าเฉลี่ยทั้งหมด{average}")