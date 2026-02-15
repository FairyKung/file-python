#List เก็บข้อมูล
fruits = ["apple","banana","mango"]
print(fruits)
print(fruits[0])
fruits.append("orange")
print(fruits)
fruits.insert(2,"grape")
print(fruits)
fruits.remove("banana")
print(fruits)
fruits.pop(-1)
print(fruits)
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)

nums = [0,1,2,3,4,5]
print(nums)
print(nums[1:4])
print(nums[:3])
print(nums[3:])

#dictonary กำหนดค่าในข้อมูลนั้นๆเช่น ชื่อ อายุ
student={
    "name": "Anna",
    "age" : 20,
    "grade" :"A"
}
print(student)
print(student["name"])

#Tuple เก็บข้อมูลและแสดงผล ไม่สามารถทำการกระทำใดๆได้
colors = ("red","green","blue")
print(colors)