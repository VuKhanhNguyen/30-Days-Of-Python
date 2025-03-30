
from string import *
from random import *
#với module random thì có random, randint, choice, shuffle, sample, uniform, randrange,...
#random: trả về một số thực ngẫu nhiên trong khoảng [0.0, 1.0)
#randint: trả về một số nguyên ngẫu nhiên trong khoảng [a, b] (a, b là tham số truyền vào)
#choice: trả về một phần tử ngẫu nhiên từ một chuỗi, danh sách hoặc tuple
#shuffle: trộn các phần tử trong một danh sách
#sample: trả về một danh sách chứa các phần tử ngẫu nhiên từ một chuỗi, danh sách hoặc tuple
#uniform: trả về một số thực ngẫu nhiên trong khoảng [a, b] (a, b là tham số truyền vào)
#randrange: trả về một số nguyên ngẫu nhiên trong khoảng [a, b) (a, b là tham số truyền vào)

#1. Writ a function which generates a six digit/character random_user_id.
def random_user_id():

    stringRand = ascii_letters
    numRand = digits
    user_id = ''
    for i in range(6):
        user_id += choice(stringRand + numRand)
    return user_id
print(random_user_id())    

#2.Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
from string import *
from random import *
def user_id_gen_by_user():
    input1 = int(input('Nhập độ dài của id: '))
    input2 = int(input('Nhập số lượng id: '))
    
    stringRand = ascii_letters
    numRand = digits
    
    for i in range(input2):
        user_id = ''
        for j in range(input1):
            user_id += choice(stringRand + numRand)
        print(user_id)
user_id_gen_by_user()   

#3. Write a function named rgb_color_gen. It will generates rgb colors (3 values ranging from 0 to 255 each).
from random import*
def rbg_color_gen():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r,g,b)
print(rbg_color_gen())
