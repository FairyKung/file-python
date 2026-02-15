#dictonary กำหนดค่าในข้อมูลนั้นๆเช่น ชื่อ อายุ
students=[{
    "name": "Anna",
    "age" : 20,
    "grade" :"A",
    "city":"bangkok",
    "hobbies":["อ่านหนังสือ","เขียนโค้ด"]
},{
    "name": "Kafei",
    "age" : 20,
    "grade" :"A",
    "city":"bangkok",
    "hobbies":["อ่านหนังสือ","เขียนโค้ด"]
}]
print(students)
print("\n")
for student in students:
 print(f"ชื่อ : {student['name']}")
students.append({
 "name": "Man",
 "age": 21,
 "grade" : "A",
 "city" : "boagkok",
 "hobbies": ["อ่านหนังสือ","อ่านข่าว"]
})
print(students)

for student in students:
    if student["name"] == "Anna":
        students.remove(student)
        break

print("\n")
print(students)

new_student = {
   "name":"Chiayo",
   "age":"21",
   "grade":"B",
   "city":"bangkok",
   "hobbies":["นอน","เล่นเกม"]
}
students.append(new_student)
print("\n")
for student in students:
   print(f"ชื่อ : {new_student['name']}")
   print(new_student)