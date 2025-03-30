#import 1 module
import mymodule
print(mymodule.generate_full_name('Nguyễn', 'Vũ Khanh'))

from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Nguyễn', 'Vũ Khanh'))
print(sum_two_nums(1, 9))
mass = 100
weight = mass * gravity
print(weight)
print(person.get('firstname'))

from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabneh','Yetayeh'))
print(total(1,9))
mass = 100
weight = mass * g
print(weight)
print(p)
print(p.get('firstname'))

#import built-in modules
'''
Sử dụng mô-đun os trong Python, có thể tự động thực hiện nhiều tác vụ hệ điều hành.
Mô-đun OS trong Python cung cấp các hàm để tạo, thay đổi thư mục làm việc hiện tại, xóa thư mục (folder),
lấy nội dung của thư mục, thay đổi và xác định thư mục hiện tại.
'''
#
import os
#tạo 1 directory
os.mkdir('directory_name')
#thay đổi directory hiện tại
os.chdir('path')
#lấy directory đang làm việc hiện tại
os.getcwd()
#xóa directory
os.rmdir()



#system module 
'''
Mô-đun sys cung cấp các hàm và biến được sử dụng để thao tác với các phần khác nhau của môi trường runtime trong Python.
Hàm sys.argv trả về một danh sách các đối số dòng lệnh được truyền cho một script Python.
Phần tử ở chỉ mục 0 trong danh sách này luôn là tên của script, còn phần tử ở chỉ mục 1 là đối số được truyền từ dòng lệnh.
'''
# nghĩa là khi chạy file này từ command line thì nó sẽ in ra tên file và các tham số truyền vào

import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))

#sys.exit() #dừng chương trình lại
#sys.maxsize #trả về kích thước lớn nhất của một biến nguyên trong Python
#sys.version #trả về phiên bản của Python đang chạy
#sys.path #trả về danh sách các thư mục mà Python tìm kiếm các mô-đun khi sử dụng câu lệnh import

#statitics module
from statistics import *
age = [22, 19, 24, 25, 26, 24, 25, 26, 27, 28]
print(mean(age))
print(median(age))
print(mode(age))
print(stdev(age))
print(variance(age))

#math module
import math
# print(dir(math))
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base

from math import pi
print(pi)

from math import *
print(pi)                  # 3.141592653589793, pi constant
print(sqrt(2))             # 1.4142135623730951, square root
print(pow(2, 3))           # 8.0, exponential
print(floor(9.81))         # 9, rounding to the lowest
print(ceil(9.81))          # 10, rounding to the highest
print(math.log10(100))     # 2

#string module
import string
print(string.ascii_letters) #abc...xyzABC...XYZ
print(string.digits) # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

#random module
from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive