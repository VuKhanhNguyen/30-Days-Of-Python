
# Variables in Python

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = -250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Asabeneh', 
    'lastname':'Yetayeh', 
    'country':'Finland',
    'city':'Helsinki'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

# first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

# print(first_name, last_name, country, age, is_married)
# print('First name:', first_name)
# print('Last name: ', last_name)
# print('Country: ', country)
# print('Age: ', age)
# print('Married: ', is_married)

#================================================================================================
print(abs(age))

#================================================================================================
print(all(skills))
#ví dụ all() # trả về false khi có ít nhất một phần tử là "falsy" (False, 0, None, "", [], {}, set(), ...).
number_list = [1, 2, 3, 4, 5]
print(all(n%2==0 for n in number_list)) # False

#================================================================================================
print(any(number_list))

#================================================================================================
#các kí tự không thuộc ascii sẽ được chuyển thành mã escape unicode
test = 'khanh khiêm tốn'
print(ascii(test))

#================================================================================================
print(bin(age))
print(bin(age)[3:])
print(format(age, 'b'))

#================================================================================================
print(bool(is_married))

#================================================================================================
# #ví dụ breakpoint()
# breakpoint() 
a = 10
b = int(10.1)
def tinhtong(a, b):
    tong = a + b 
    return tong
ket_qua = tinhtong(a, b)
print("Tổng là:", ket_qua)

#================================================================================================
#ví dụ bytearray([nguồn], [encoding], [error]) có thể sửa
# file_path = r"C:/Users/ADMIN/Pictures/Screenshots/Screenshot 2025-02-10 114003.png"
# with open(file_path, "rb") as file:
#     data = bytearray(file.read())
#     print(data)

    # data[0] = 0xFF  
    # # Ghi lại file đã chỉnh sửa
    # with open(file_path, "wb") as file:
    #     file.write(data)
    # print("File đã được chỉnh sửa thành công!")

#================================================================================================
#ví dụ bytes([nguồn], [encoding], [error]), không thể sửa
# file_path = r"C:/Users/ADMIN/Pictures/Screenshots/Screenshot 2025-02-10 114003.png"
# with open(file_path, "rb") as file:
#     data = bytes(file.read())
#     print(data)

#================================================================================================
print(callable(age)) #false
print(callable(tinhtong))

#================================================================================================
#chuyển mã ascii, unicode thành kí tự
print(chr(107))

#================================================================================================
class Example:
    class_var = "Class Variable"

    @classmethod
    def class_method(cls):
        return cls.class_var
    @classmethod
    def class_method_changename(cls, newname):
        cls.class_var = newname
Example.class_method_changename("New variable")
print(Example.class_var)
    # @staticmethod
    # def static_method(a):
    #     return "Static Method Called"

print(Example.class_method())
# print(Example.static_method()) 

#================================================================================================
source_code = """
x = 10
y = 20
result = x + y
print("Tổng:", result)
"""
compiled_code = compile(source_code, filename="<string>", mode="exec")
# Thực thi mã bytecode
exec(compiled_code)

#================================================================================================
complexTest1, complexTest2 = 3, -4
result = complex(complexTest1, complexTest2)
print(result) 
print("phần thực: ", result.real)
print("phần ảo: ", result.imag)
#================================================================================================
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Tạo một đối tượng Person
person = Person("Alice", 30)

# Trước khi xóa thuộc tính
print("Tên:", person.name)
print("Tuổi:", person.age)

# Xóa thuộc tính 'age' của đối tượng person
delattr(person, "age")

# Kiểm tra lại sau khi xóa
print("Tên:", person.name)
try:
    print("Tuổi:", person.age)  # Sẽ gây lỗi vì 'age' đã bị xóa
except AttributeError as e:
    print("Lỗi:", e)

#================================================================================================
my_dict = dict(name="Alice", age=25, city="New York")
print(my_dict.get("name"))
print(my_dict)

# Tạo từ điển từ danh sách các cặp (key, value)
pairs = [("name", "Bob"), ("age", 30), ("city", "London")]
my_dict = dict(pairs)
print(my_dict)

original_dict = {"a": 1, "b": 2}
copied_dict = dict(original_dict)
print(copied_dict)

# Từ điển gốc
original_dict = {"x": 10, "y": 20}
# Kết hợp từ điển gốc với các đối số từ khóa
new_dict = dict(original_dict, z=30, y=50)  # `y` được ghi đè
print(new_dict)
#================================================================================================
import math
print(dir(math))
print(dir())
print(dir(Example()))
methods = [m for m in dir(math) if not m.startswith("_")]
print(methods)

#================================================================================================
print(divmod(10, 3)) # bằng 3 dư 1 (3,1)

#================================================================================================
for i, nameSkill in enumerate(skills,start=1):
    print(f"Thứ tự {i}: {nameSkill}")
    
for n in enumerate(skills):
    print(n)
    
for index, char in enumerate("Python"):
    print(f"Ký tự {char} ở vị trí {index}")
        
#================================================================================================
x=1
print(eval('x+1'))

expr = "3 + 5 * 2"
result = eval(expr)
print(result)

x1 = 100
y1 = 20
context = {"x": 10, "y": 20}  # Chỉ cho phép dùng x = 10, y = 20
print(eval("x + y", context))
print(eval("x1 + y1", globals()))

# user_input = input("Nhập biểu thức toán học: ")  # Ví dụ nhập: 10 / 2 + 3
# print("Kết quả:", eval(user_input))

#================================================================================================
class Book:
    def __init__ (self, title, author,yearPublish):
        self.title=title
        self.author=author
        self.yearPublish=yearPublish
book= Book("Doraemon","Fujiko.F.Fujio","2004")
print(getattr(book, 'title','không tìm thấy'))


class MathOperations:
    def add(self, a, b):
        return a + b
    
    def multiply(self, a, b):
        return a * b

math_obj = MathOperations()

# Chọn phương thức cần gọi
operation = "add"
func = getattr(math_obj, operation, None)  # Lấy phương thức add
if func:
    print(func(3, 5))  # Output: 8        

#================================================================================================


#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================
#================================================================================================


import math
#exercises
#1.Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(skills))
print(type(age))

#2.Using the len() built-in function, find the length of your first name
print(len(first_name))

#3.Compare the length of your first name and your last name
print(len(first_name) > len(last_name))

#4.Declare 5 as num_one and 4 as num_two
num_one = 20
num_two = 8

#5.Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print(total)

#6.Subtract num_one from num_two and assign the value to a variable total
total1 = num_one - num_two
print(total1)

#7.Multiply num_two and num_one and assign the value to a variable total
total2 = num_one * num_two
print(total2)

#8.Divide num_one by num_two and assign the value to a variable total
try :
    total3 = num_one / num_two
    print(total3)
except ZeroDivisionError:
    print("Không thể chia cho 0")
    
#9.Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
print(remainder)

remainder1,remainder2 = divmod(num_two, num_one)
print(remainder2)

#10.Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one * math.pow(num_two,2)
print(exp)

#11.Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print(floor_division)

'''12.The radius of a circle is 30 meters.
-Calculate the area of a circle and assign the value to a variable name of area_of_circle
-Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
-Take radius as user input and calculate the area.'''
import math
area_of_circle = math.pi * math.pow(30,2)
print(f'Diện tích hình tròn là',area_of_circle)

circum_of_circle = 2 * math.pi * 30
print(f'Chu vi hình tròn là',circum_of_circle)

import math
userInput = input("Nhập vào bán kính hình tròn: ")
while not userInput.isnumeric():
    print("Nhập sai")
    userInput = input("Nhập vào bán kính hình tròn: ")
    
area_of_circle2 = math.pi * math.pow(int(userInput),2)
print(f'Diện tích hình tròn là',area_of_circle2)    

#13.Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
class information:
    def __init__(self, firstname, lastname, country, age):
        self.firstname = firstname
        self.lastname = lastname
        self.country = country
        self.age = age
    def __str__(self):
        # return f"{self.firstname} {self.lastname} {self.country} {self.age}"
        return f"Tên: {self.firstname}, Họ: {self.lastname}, Quốc gia: {self.country}, Tuổi: {self.age}"

info_input = input("Nhập tên: ")
info_input2 = input("Nhập họ: ")
info_input3 = input("Nhập quốc gia: ")
info_input4 = input("Nhập tuổi:")
info = information(info_input, info_input2, info_input3, info_input4)
print(info)

#14.Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
print(help('keywords'))