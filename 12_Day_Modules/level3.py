
#1.Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list.
from random import shuffle
def shuffle_list(lst):
    emptyList = []
    for i in lst:
        emptyList.append(i)
    shuffle(emptyList)
    return emptyList
print(shuffle_list([1,2,3,4,5,6,7,8,9,10]))

#2.Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
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
    