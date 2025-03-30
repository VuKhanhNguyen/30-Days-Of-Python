#1.Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
ood_and_zero = [i for i in numbers if i <= 0]
print(ood_and_zero)

#2.Flatten the following list of lists of lists to a one dimensional list
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten = [a for sub in list_of_lists for item in sub for a in item]
print(flatten)

#3.Using list comprehension create the following list of tuples:
'''[(0, 1, 0, 0, 0, 0, 0),
    (1, 1, 1, 1, 1, 1, 1),
    (2, 1, 2, 4, 8, 16, 32),
    (3, 1, 3, 9, 27, 81, 243),
    (4, 1, 4, 16, 64, 256, 1024),
    (5, 1, 5, 25, 125, 625, 3125),
    (6, 1, 6, 36, 216, 1296, 7776),
    (7, 1, 7, 49, 343, 2401, 16807),
    (8, 1, 8, 64, 512, 4096, 32768),
    (9, 1, 9, 81, 729, 6561, 59049),
    (10, 1, 10, 100, 1000, 10000, 100000)]'''
LOT = [(i,1,i,i**2,i**3,i**4,i**5) for i in range(11)]
print(LOT)

#4.Flatten the following list to a new list
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flatten = [list(item) for sub in countries for item in sub]
print(flatten)

#5.Change the following list to a list of dictionaries
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
keyy = ['country', 'city']
dicti = [{keyy[0]: country, keyy[1]: city} for sublist in countries for country, city in sublist]
print(dicti)

#6.
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concat = [firstname +' '+ lastname for sublist in names for firstname, lastname in sublist]
print(concat)

#7.
SlopeCal = lambda x1,x2,y1,y2: (y2-y1)/(x2-x1)
print(SlopeCal(2,4,4,7))

def slopecal(x1, x2, y1, y2):
    return (y2 - y1) / (x2 - x1)
print(slopecal(2, 4, 4, 7))