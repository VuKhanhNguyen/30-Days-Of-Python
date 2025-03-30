from random import*
def rbg_color_gen():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r,g,b)
print(rbg_color_gen())