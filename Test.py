# ลองออกแบบ class Car พร้อม attributes และ methods ของคุณเอง
class Car:
    def __init__(self,model,colors,wheel,brand):
        self.colors = colors
        self.wheel = int(wheel)
        self.brand = brand
        self.model = model

    def show_more(self):
        print(f"Car : {self.model} Colors {self.colors} Wheel {self.wheel} Brand {self.brand}")
car1 = Car("Model A " , "Red " ,4,"Tesla")
car1.show_more()
pass