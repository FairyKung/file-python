class Student:
    def __init__(self,name,student_id,point,mid_term,final_exam):#attribute
        self.name = name
        self.student_id = student_id
        self.point = int (point)
        self.mid_term = int (mid_term)
        self.final_exam = int (final_exam)
        #self.score = score
    def introduce(self):#method
        print(f"ฉันชื่อ {self.name} รหัสนักศึกษา {self.student_id}")
    def grade(self):
        total = self.point + self.mid_term + self.final_exam
        if total >= 80:
            return "A"
        elif total >= 70:
            return "B"
        elif total >= 60:
            return "C"
        else:
            return "F"
        
    def show_info(self):
        print(f"|ชื่อ : {self.name} |รหัสนักศึกษา : {self.student_id} |เกรดที่ได้ : {self.grade()}")

student1 = Student("ชยากร","123456",10,30,50)
student1.introduce()
student1.show_info()
pass
#คะแนนจิตพิสัยpoint คะแนนสอบกลางภาคmidterm คะแนนสอบปลายภาคfinalexam