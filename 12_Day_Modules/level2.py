#1.Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array 
# (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 
# 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
from string import *
from random import *
def list_of_hexa_colors(n):
    hex_char = '0123456789abcdef'
    lst = []
    
    for i in range(n):
        hex = '#'
        for j in range(6):
            hex += choice(hex_char)
        lst.append(hex)
    return lst        
print(list_of_hexa_colors(5))

#2.Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
from random import randint
def list_of_rgb_colors(n):
    lst = []
    
    for i in range(n):
        # for j in range(3):
        rgb = randint(0,255), randint(0,255), randint(0,255)
        lst.append(rgb)
    return lst
print(list_of_rgb_colors(5))    

#3.Write a function generate_colors which can generate any number of hexa or rgb colors.
from string import *
from random import *
def generate_color(c, n):
    lst = []
    if c == 'hexa': 
        hex_char = '0123456789abcdef'
        for i in range(n):
            hex = '#'
            for j in range(6):
                hex += choice(hex_char)
            lst.append(hex)
        return lst
    if c == 'rgb':
        
        for i in range(n):
            rgb = f'rgb({randint(0,255)}, {randint(0,255)}, {randint(0,255)})'
            lst.append(rgb)
        return lst
print(generate_color('hexa', 3))
print(generate_color('hexa', 1))
print(generate_color('rgb', 3))  
print(generate_color('rgb', 1))  # ['rgb(33,79, 176)']       