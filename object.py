#OOP

def say_hello():
    print("สวัสดีวันอาทิตย์")

say_hello()
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
result_add = add(10,5)
result_sub = sub(6,3)
result_mul = mul(9,7)
result_div = div(24,6)

print(result_add)
print(result_sub)
print(result_mul)
print(result_div)

print("ผลลัพธ์ :",add(10,5))
print(f"ผลลัพธ์ของการบวก {add(10,5)}")
print(f"ผลลัพธ์ของการลบ {sub(6,3)}")
print(f"ผลลัพธ์ของการคูณ {mul(9,7)}")
print(f"ผลลัพธ์ของการหาร {div(24,6)}")

x=10 #Global variable

def show_value():
    x=5 #Local variable
    print("ค่าของ X ภายในฟังก์ชั่น", x)

show_value()
print("ค่าของ X ภายนอกฟังก์ชั่น",x)