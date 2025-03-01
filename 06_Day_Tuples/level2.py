# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
# Change the about food_stuff_tp tuple to a food_stuff_lt list
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
# Slice out the first three items and the last three items from food_staff_lt list
# Delete the food_staff_tp tuple completely

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products = ('milk', 'meat', 'butter')
food_stuff_tp  = fruits + vegetables + animal_products
print(food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

middle_item = int(len(food_stuff_lt)/2)
print(food_stuff_lt[middle_item-1:middle_item+1])
middle_item2 = int(len(food_stuff_tp)/2)
print(food_stuff_tp[middle_item-1:middle_item+1])

first_item = food_stuff_lt[0:3]
print(first_item)
last_item = food_stuff_lt[-3:]
print(last_item)

try: 
    del food_stuff_tp
    print(food_stuff_tp)
except NameError as n:
    print('Tuple does not exist anymore')
    print(f'Lỗi {n}') 