from random import randrange, shuffle
def random_in_range():
    emptySet = set()
    while len(emptySet)<7:
        randNum = randrange(0,10)
        emptySet.add(randNum)
    lst = list(emptySet)
    shuffle(lst)
    return lst
print(random_in_range())