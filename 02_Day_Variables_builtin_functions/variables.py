
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


print(abs(age))

print(all(skills))
#ví dụ all() # trả về false khi có ít nhất một phần tử là "falsy" (False, 0, None, "", [], {}, set(), ...).
number_list = [1, 2, 3, 4, 5]
print(all(n%2==0 for n in number_list)) # False

print(any(number_list))

#các kí tự không thuộc ascii sẽ được chuyển thành mã escape unicode
test = 'khanh khiêm tốn'
print(ascii(test))

print(bin(age))
print(bin(age)[3:])
print(format(age, 'b'))

print(bool(is_married))

# #ví dụ breakpoint()
# breakpoint() 
a = 10
b = int(10.1)
def tinhtong(a, b):
    tong = a + b 
    return tong
ket_qua = tinhtong(a, b)
print("Tổng là:", ket_qua)

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

#ví dụ bytes([nguồn], [encoding], [error]), không thể sửa
# file_path = r"C:/Users/ADMIN/Pictures/Screenshots/Screenshot 2025-02-10 114003.png"
# with open(file_path, "rb") as file:
#     data = bytes(file.read())
#     print(data)