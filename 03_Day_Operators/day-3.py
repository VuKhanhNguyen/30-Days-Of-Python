# Arithmetic Operations in Python
# Integers

print('Addition: ', 1 + 2)
print('Subtraction: ', 2 - 1)
print('Multiplication: ', 2 * 3)
print ('Division: ', 4 / 2)                         # Division in python gives floating number
print('Division: ', 6 / 2)
print('Division: ', 7 / 2)
print('Division without the remainder: ', 7 // 2)   # gives without the floating number or without the remaining
print('Modulus: ', 3 % 2)                           # Gives the remainder
print ('Division without the remainder: ', 7 // 3)
print('Exponential: ', 3 ** 2)                     # it means 3 * 3

# Floating numbers
print('Floating Number,PI', 3.14)
print('Floating Number, gravity', 9.81)

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex number: ',(1 + 1j) * (1-1j))

# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function try to avoid overriding builtin functions
print(total) # if you don't label your print with some string, you never know from where is  the result is coming
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_two
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)


# Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')

print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# Boolean comparison
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)

# Another way comparison 
print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False -there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statement is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False

# x=10 và x>>=2 tức là x = 10 với binary 1010, sau đó dịch phải 2 bit, kết quả là 0010, tức là 2
x=10
x>>=2
print(x)

# x=100 và x<<=2 tức là x = 100 với binary 1100100, sau đó dịch trái 2 bit, kết quả là 1100100"00", tức là 400
x=100
x<<=2
print(x)

print(x:=3) #=3 nhưng print(x=3) sẽ bị lỗi
#================================================================================================
# Exercises
#1.Declare your age as a integer variable
age = int(21)
print(f'Tuổi của ní là: ', age)

#2.Declare your height as a float variable
height = float(1.75)
print(f'Chiều cao của ní là: ', height, 'm')

#3.Declare a variable that store a complex number
cnumberReal = 4
cnumberImg = 2
complexNumber = complex(cnumberReal, cnumberImg)
print(complexNumber)
print(f"Phần thực là: ", complexNumber.real)
print(f"Phần ảo là: ", complexNumber.imag)

#4.Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
import math
print("Nhập vào chiều dài cạnh đáy và chiều cao của tam giác: ")
while True:
    try:
        base = float(input("Chiều dài cạnh đáy: "))
        if base <= 0:
            print("Nhập sai, mời nhập lại")
            continue
        height = float(input("Chiều cao: "))
        if height <= 0:
            print("Nhập sai, mời nhập lại")
            continue
        break
    except ValueError:
        print("Nhập sai, mời nhập lại")
area = 0.5 * base * height
print(f'Diện tích của tam giác là: ', area)

#6.Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
import math
print("Nhập vào 3 cạnh của tam giác: ")
while True:
    try:
        a = float(input(f"Nhập cạnh a: "))
        if a<=0 or not a.replace('.', '', 1).isdigit():
            print("Nhập sai mời nhập lại!")
            continue
        b = float(input(f"Nhập cạnh b: "))
        if b<=0 or not b.replace('.', '', 1).isdigit():
            print("Nhập sai mời nhập lại!")
            continue
        c = float(input(f"Nhập cạnh c: "))
        if c<=0 or not c.replace('.', '', 1).isdigit():
            print("Nhập sai mời nhập lại!")
            continue
        break
    except ValueError:
        print("Nhập sai mời nhập lại!")
perimeter = a + b + c
print(f'Chu vi của tam giác là: ', perimeter)        