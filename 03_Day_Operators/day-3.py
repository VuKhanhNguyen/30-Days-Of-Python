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
        a = input(f"Nhập cạnh a: ")
        if not a.replace('.', '', 1).isdigit():
            print("Nhập sai mời nhập lại!")
            continue
        b = input(f"Nhập cạnh b: ")
        if not b.replace('.', '', 1).isdigit():
            print("Nhập sai mời nhập lại!")
            continue
        c = input(f"Nhập cạnh c: ")
        if not c.replace('.', '', 1).isdigit():
            print("Nhập sai mời nhập lại!")
            continue
        break
    except ValueError:
        print("Nhập sai mời nhập lại!")
perimeter = a + b + c
print(f'Chu vi của tam giác là: ', perimeter)        

#6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
#print ("Nhập vào chiều dài và chiều rộng của hình chữ nhật: ")
while True:
    try:
        chieudai = float(input("Chiều dài: "))
        chieurong = float(input("Chiều rộng: "))
        if(chieudai <= 0 or chieurong <= 0):
            print("Chiều dài và chiều rộng phải > 0 nha ní !")
            chieudai = float(input("Chiều dài: "))
            chieurong = float(input("Chiều rộng: "))
        else:
            dientich = chieudai * chieurong
            chuvi = 2 * (chieudai + chieurong)
        print(f"Diện tích là:  {dientich}  và chu vi là:  {chuvi}")
        break
    except Exception as e:
        print("Lỗi mọe nó rồi thần đằng ạ!!")
    

#7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
# breakpoint()
import math
while True:
    try:
        r = float(input("Nhập bán kính: "))
        area = math.pi * math.pow(r,2)
        c = 2 * math.pi * r
        print(f"Diện tích hình tròn là: {area} và chu vi hình tròn là: {c}")
        break
            
    except ValueError as e:
        print(f"Nhập sai mời nhập lại! {e}")
    except Exception as e:
        print(f"Lỗi {e} mọe nó rồi thần đằng ạ!!")           

#8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
def findSlope(e):
    p = e.replace("y=","").split("x")
    s = float(p[0])    
    # i = float(p[1])
    return s

def findIntercept(e):    
    p = e.replace("y=","").split("x")
    # s = float(p[0])    
    i = float(p[1])
    return i
      
e = "y=2x-2"

slope=findSlope(e)
print(f"Hệ số góc (slope) là: {slope}")

xi = - findIntercept(e) / findSlope(e)
print(f"X-intercept là: ({xi},0)")

yi = findIntercept(e)
print(f"Y-intercept là: (0,{yi})")

#================================================================
# breakpoint()
# e = "y = 2x-2"
# p = e.replace("y = ", "").split("x")
# s = float(p[0])
# i = float(p[1])

# print(f"Hệ số góc (slope) là: {s}")
# yi = s * 0 + i
# print(f"Y-intercept là: {yi}")
# xi = -i / s
# print(f"X-intercept là: {xi}")

#9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
import math
x1=2 
y1=2
x2=6 
y2=10
#x1, y1, x2, y2 = 1, 2, 4, 6 
def findSlope(m):
    # m = float((y2-y1)/(x2-x1))
    print(f"Hệ số góc m={m}")
    return m

def findEuclideanDistance(x1,y1,x2,y2):
    d = math.sqrt((pow(x2-x1,2))+(pow(y2-y1,2)))
    print(f"Khoảng cách là: {d}") 
    return d

m = float((y2-y1)/(x2-x1))
s9 = findSlope(m)
s9_2 = findEuclideanDistance(x1,y1,x2,y2)

#10. Compare the slopes in tasks 8 and 9.

if slope == s9:
    print("Hệ tọa độ của bài 8 và 9 bằng nhau")
elif slope > s9:
    print("Hệ tọa độ của bài 8 lớn hơn bài 9")    
else:
    print("Hệ tọa độ của bài 8 bé hơn bài 9")
    
#11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
#import math
import numpy as np
def findY(x):
    return x**2 + 6*x + 9
    
x_val = np.arange(-10,10,1)
y_val = [findY(x) for x in x_val]

roots = np.roots([1,6,9])
print(f"Giá trị x: {x_val}")
print(f"Giá trị y: {y_val}\n")
print(roots)

#================================================================
import math
def findY(x):
    return math.pow(x, 2) + 6*x + 9  # Tính y = x^2 + 6x + 9
x_val = range(-10,10,1)
y_val = [findY(x) for x in x_val]
findXmakeYbeZero = [x_val[i] for i in range(len(y_val)) if y_val[i] == 0]

print(f"Giá trị x: {list(x_val)}")
print(f"Giá trị y: {y_val}")
print(f"Giá trị x làm y = 0 là: {findXmakeYbeZero}")

#12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
lp=len("python")
dp=len("dragon")
print(lp != dp)

#13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
def FIND_ON():
    # for findON in lp and dp:
        if('on' in "python" and 'on' in "dragon"):
            return True
        return False
print(FIND_ON())

#14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = 'I hope this course is not full of jargon'
def checkWord(sentence):
    if('jargon' in sentence):
        return True
print(checkWord(sentence))    

#15. There is no 'on' in both dragon and python
str1, str2 = "python", "dragon"
def deleteON(str1,str2):
    delOn1 = str1.split("on")
    d1 = delOn1[0]
    delOn2 = str2.split("on")
    d2 = delOn2[0]
    return d1, d2
print(deleteON(str1,str2))

#16. Find the length of the text python and convert the value to float and convert it to string
def findLength(str):
    stringg = len(str)
    return stringg

strr='python'
result1 = findLength(strr)
print(result1)
result2 = str(result1)
print(result2)
print(type(result2))

#17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
def checkEvenNumber(n):
    if(n%2 == 0):
        return(f"Đây là số chẵn")
    return(f"Đây là số lẻ")
while True: 
    num=int(input("Nhập 1 số: "))
    print(checkEvenNumber(num))     
    break

#18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
import math
def convertVal():
    v=2.7
    val = int(v)
    return val

def checkCalculate():
    cal = math.floor(7/3)
    # cal = 7//3
    if(cal == convertVal()):
        return True
    return False
print(checkCalculate())

#19. Check if type of '10' is equal to type of 10
n1=type('10')
n2=type(10)
def checkTypeEqual(n1,n2):
    if(n1 == n2):
        return (f"Bằng nhau")
    return (f"Không bằng nhau")
print(checkTypeEqual(n1,n2))

#20. Check if int('9.8') is equal to 10
num = int(float('9.8'))
def checkNumEqual(n):
    try:
        if(n == 10):
            return True
        else:
            return False
    except ValueError as e:
        print(f"Lỗi {e} rồi ní ơi!")
    except Exception as e:
        print(f"Lỗi {e} rồi ní ơi!") 
print(checkNumEqual(num))

#21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
''' Enter hours: 40
    Enter rate per hour: 28
    Your weekly earning is 1120'''
def CalculatePay(h,rph):
        p = h * rph
        return p
        
while True:  
    try:
        h = int(input("Nhập giờ: "))
        break
    except ValueError as e:
        print(f"Lỗi {e}")
while True:  
    try:
        rph = int(input("Nhập lương mỗi giờ: "))
        break
    except ValueError as e:
        print(f"Lỗi {e}")            
print(f"Lương mỗi tuần của bạn là: {CalculatePay(h,rph)}$")

#22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
'''Enter number of years you have lived: 100
You have lived for 3153600000 seconds.'''
def CalculateTimeLive(y):
        result = y * 3153600
        return (f"Bạn đã sống được {result} giây rồi á!")
        
while True:  
    try:
        year = int(input("Nhập năm: "))
        break
    except ValueError as e:
        print(f"Lỗi {e}")     
             
print(CalculateTimeLive(year))

#23. Write a Python script that displays the following table
''' 1 1 1 1 1
    2 1 2 4 8
    3 1 3 9 27
    4 1 4 16 64
    5 1 5 25 125 '''

# for columnn in range(1,6):
for i in range(1,6):
    print(i, 1, i, i**2, i**3)
        
   
    

