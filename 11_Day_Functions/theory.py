#function không có parameter
def generate_full_name ():
    first_name = 'Vũ Khanh'
    last_name = 'Nguyễn'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name()

#function trả về value -part 1
def generate_full_name():
    first_name = 'Vũ Khanh'
    last_name = 'Nguyễn'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

#function có 1 parameter
def generate_full_name(name):
    message = name + ', chào các ní nhé!'
    return message
print(generate_full_name('Vũ Khanh'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(5))

def square_number(x):
    return x * x
print(square_number(5))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total += i
    return total    
print(sum_of_numbers(5))

#function có 2 parameters
def generate_full_name(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name('Vũ Khanh', 'Nguyễn'))

def sum_two_number(num_one, num_two):
    sum = num_one + num_two
    return sum
print(sum_two_number(5, 10))

def weight_of_object(mass, gravity):
    weight = str(mass * gravity) + ' N' 
    #giá trị của weight là 1 số thực, nhưng để in ra có đơn vị N thì phải chuyển thành string
    return weight
print(weight_of_object(10, 9.81))

#truyền tham số với key và value
def print_fullanme(firstname, lastname):
    space = ' '
    fullname = firstname + space + lastname
    return fullname
print(print_fullanme(firstname='Vũ Khanh', lastname='Nguyễn'))
print(print_fullanme(lastname='Nguyễn', firstname='Vũ Khanh')) # truyền lastname trước thì kết quả vẫn hiển thị firstname trước rồi mới tới lastname

#function trả về value -part 2
def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print_full_name(firstname='Asabeneh', lastname='Yetayeh')

def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))

def is_even (n):
    if n % 2 == 0:
        print('even')
        return True    # return stops further execution of the function, similar to break 
    return False
print(is_even(10)) # True
print(is_even(7)) # False

def find_even_number(n):
    even = []
    for i in range(n+1):
        if i % 2 == 0:
            even.append(i)
    return even
print(find_even_number(10)) 

#function với giá trị mặc định của parameter
def generate_full_name(firstname = 'Nguyễn', lastname = 'Vũ Khanh'):
    space = ' '
    full_name = firstname + space + lastname
    return full_name
print(generate_full_name()) # Nguyễn Vũ Khanh
print(generate_full_name('Nguyen', 'Vu Khanh'))

#truyền vào nhiều tham số khác nhau, không giới hạn số lượng tham số
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(sum_all_nums(2,3,4))

#truyền tham số mặc định và nhiều tham số khác
def generate_groups(team, *args):
    print(team)
    for i in args:
        print(i)
print(generate_groups(f'team: {'TrioForce'}','Khanh','Quý','Đức'))   

#function như là 1 parameter của function khác
def square_number(n):
    return n * n
def do_something(f,x):
    return f(x)       
print(do_something(square_number, 5)) # 25