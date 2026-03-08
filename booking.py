import datetime
import uuid

class Student:
    def __init__(self,student_id,name,phone):
        self.student_id = student_id
        self.name = name
        self.phone = phone
        self.bookings = []
    def make_booking(self,classroom,date_str,time_str):
        if not hasattr(classroom,'schedule'):
            print(f"Error: Classroom {classroom.room_number} does not have schedule manager.")
            return None
        try:
            booking_date = datetime.datetime.strptime(date_str,"%Y-%m-%d").date()
            booking_time = datetime.datetime.strptime(time_str,"%H:%M").time()
        except ValueError:
            print("Invalid date or time format. Please use YYYY-MM-DD and HH:MM.")
            return None
        if classroom.check_availability(booking_date,booking_time):
            booking = Booking(self,classroom,booking_date,booking_time)
            self.bookings.append(booking)
            classroom.schedule.add_booking(booking)
            print(f"Booking request created for {self.name}for Room {classroom.room_number} on {date_str} at {time_str}. Status: {booking.status}")
            return booking
        else:
            print(f"room {classroom.room_number} is not available on {date_str} at {time_str}.")
            return None
    def cancle_booking(self,booking):
        if booking in self.bookings:
                if booking.status == "approved":
                    print("Approved bookings must be cancelled by an admin.")
                else:
                    booking.cancle()
                    self.bookings.remove(booking)
                    booking.classroom.schedule.remove_booking(booking)
                    print(f"Booking {booking.booking.id} ancelled by {self.name}")
        else:
            print("Booking not found in you list.")

    def view_booking(self):
        if not self.bookings:
            print(f"{self.name} has no bookings.")
            print(f"\n --- Booking for {self.name} --- ")
            return
        for booking in self.bookings:
            print(f"ID: {booking.booking_id} Room: {booking.classroom.room_number},Date: {booking.date},Time: {booking.time}, Status: {booking.status} ")

class Classroom:
    def __init__(self,room_number,capacity,equipment):
        self.room_number = room_number
        self.capacity = capacity
        self.equipment = equipment
        self.schedule = Schedule(self)

    def check_availability(self,date,time):
        return self.schedule.is_available(date,time)
    
    def get_schedule(self):
        return self.schedule.get_all_booking()
    
    def __str__(self):
        return f"Room {self.room_number} (Capacity:{self.capacity}, Equipment: {', '.join(self.equipment)})"
    
class Booking:
    booking_couter = 0

    def __init__(self,student,classroom,date,time):
        self.booking_id = f"BK-{Booking.booking_couter:04d}"
        Booking.booking_couter += 1

        self.student = student
        self.classroom = classroom
        self.date = date
        self.time = time
        self.status = "pending"
            
    def approve(self):
        self.status = "approved"
        print(f"Booking {self.booking_id} for Room {self.classroom.room_number} on {self.date} at {self.time} has been APPROVED.")

    def cancle(self):
        self.status = "cancelled"
        print(f"Booking {self.booking_id} for Room {self.classroom.room_number} on {self.date} at {self.time} has been CANCELLED.")

    def __str__(self):
        return f"Booking ID: {self.booking_id}, Student: {self.student.name}, Room: {self.classroom.room_number}, Date: {self.date}, Time: {self.time}, Status: {self.status}"
    
class Schedule:
    def __init__(self,classroom):
        self.clasroom = classroom
        self.bookings = {}

    def is_available(self,date,time):
        key = (date,time)
        return key not in self.bookings or self.bookings[key].status == "cancelled"
    
    def add_booking(self,booking):
        key = (booking.date,booking.time)
        if self.is_available(booking.date,booking.time):
            self.bookings[key] = booking
            return True
        else:
            print(f"Error: Cannot add booking for {self.classrom_number} on {booking.date} at {booking.time}")
            return False
        
    def remove_booking(self,booking):
        key = (booking.date,booking.time)
        if key in self.bookings and self.bookings[key] == booking:
            del self.bookings[key]
            return True
        return False
    
    def get_all_bookings(self):
        return list(self.bookings.values())
    
class Admin:
    def __init__(self,admin_id,name):
        self.admin_id = admin_id
        self.name = name

    def approve_booking(self,booking):
        if booking.status == "pending":
            booking.approve()
        elif booking.status == "approved":
            print(f"Booking {booking.booking_id} is already approved.")
        else:
            print(f"Boking {booking.booking_id} cannot be approved, current status is {booking.status}")

    def cancle_booking(self,booking):
        if booking.status != "cancelled":
            booking.cancle()
            booking.classroom.schedule.remove_booking(booking)
            booking.student.bookings.remove(booking)
            print(f"Admin {self.name} has cancelled Booking {booking.booking_id}.")
        else:
            print(f"Booking {booking.booking_id} is already cancelled.")

    def view_all_booking(self,all_classroom):
        print(f"\n ---All Bookings managed by Admin {self.name} ---")
        found_bookings = False
        for classroom in all_classroom:
            for booking in classroom.schedule.get_all_bookings():
                print(booking)
                found_bookings = True
            if not found_bookings:
                print("no bookings found across all classroom")

print("---เริ่มการจำลองระบบจองห้องเรียน---")
student1 =Student("S001","Fei","081-234-4567")
student2 =Student("S002","ling","061-234-4567")

room101 =Classroom("101",30,["Projector","Whiteboard"])
room102 =Classroom("102",50,["Smartboard","Microphone"])

admin1 =Admin("A001","Zhong")

print("\n---สถานะเริ่มต้น---")
print(room101)
print(room102)

#1
booking_Fei_1 = student1.make_booking(room101,"2026-03-01","11:31")
if booking_Fei_1:
    student1.view_booking()
    room101.schedule.get_all_bookings()
#2
booking_ling_1 = student2.make_booking(room101,"2026-03-01","11:31")
if booking_ling_1:
    student2.view_booking()
    room101.schedule.get_all_bookings()
#3
booking_ling_2 = student2.make_booking(room102,"2026-03-01","11:31")
if booking_ling_2:
    student2.view_booking()
    room102.schedule.get_all_bookings()
#4 admin approve
print("\n Admin อนุมัติการจองของ Fei")
if booking_Fei_1:
    admin1.approve_booking(booking_Fei_1)
    student1.view_booking()
#5 Fei cancel
if booking_Fei_1:
    student1.cancle_booking(booking_Fei_1)
    student1.view_booking()
#6
print("\n Admin ดูการจองทำ้งหมด")
admin1.view_all_booking([room101,room102])
#7
print("Admin ยกเลิกการจองของ ling")
if booking_ling_2:
    admin1.cancle_booking(booking_ling_2)
    student2.view_booking()
    admin1.view_all_booking([room101,room102])

print("\n --- Check --- \n")