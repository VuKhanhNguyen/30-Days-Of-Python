#1.Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a,b):
    return a+b
print(add_two_numbers(5,10))

#2.Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(2))

#3.Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*arg):
    total = 0
    for i in arg:
        if not isinstance(i,(int,float)):
            return "All items must be numbers"
        total += i
    return total
print(add_all_nums(1,'a',3,4,10))    
print(add_all_nums(1,2,3,4,10))

#4.Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(c):
    return (c*9/5)+32 
print(f'F = {convert_celsius_to_fahrenheit(20)}')

#5.Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month in ['January', 'February', 'March']:
        return 'is Spring'
    elif month in ['April', 'May', 'June']:
        return 'is Summer'
    elif month in ['July', 'August', 'September']:
        return 'is Autumn'
    else:
        return 'is Winter'
print(f'{check_season('March')} ')   

#6.Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, x2, y1, y2):
    if x2 - x1 == 0:
        return 'Slope is undefined'
    else:
        return (y2 - y1) / (x2 - x1)
print(calculate_slope(1, 2, 3, 4))

#7.Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a,b,c): #ax² + bx + c = 0
    if a == 0:
        if b == 0:
            if c == 0:
                return 'Phương trình có vô số nghiệm!'
            else:
                return 'Phương trình vô nghiệm!'
        else:
            x = -c / b
            return f'Phương trình có 1 nghiệm x = {x}'
    else:
        delta = b**2 - 4*a*c
        x1 = (-b + delta**0.5)/(2*a)
        x2 = (-b - delta**0.5)/(2*a)    
        return f'Phương trình có 2 nghiệm x1 = {x1} và x2 = {x2}'        
print(solve_quadratic_eqn(3,10,7))            

#8.Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for i in lst:
        print(i)
print_list(['a', 'b', 'c', 'd'])

#9.Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reversed_list(lst):
    empty_list = []
    for i in lst:
        empty_list.append(i)
    return empty_list[::-1]   
print(reversed_list([1, 2, 3, 4, 5,6]))

#10.Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lst):
    empty_list = []
    for i in lst:
        empty_list.append(i.capitalize())
    return empty_list
print(capitalize_list_items(['html', 'css', 'javascript']))

#11.Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_items(x,y):
    if y not in x:
        x.append(y)
        return x
    else:
        return 'Item already exists in the list'
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']    
print(add_items(food_staff,'Meat'))    
print(add_items(food_staff,'Potato'))

#12.Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_items(x,y):
    if y in x:
        x.remove(y)
        return x
    else:
        return 'Item not found in the list'
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_items(food_staff,'Potato'))
print(remove_items(food_staff,'Meat'))    


#13.Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.  
def sum_of_numbers(n):
    if not isinstance(n,(int,float)):
        return 'All items must be numbers'
    else:
        total = 0
    for i in range(1,n+1):
        total += i
    return total
        
print(sum_of_numbers(5))    
print(sum_of_numbers('a'))
print(sum_of_numbers(10))

#14.Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(n):
    if not isinstance(n,(int, float)):
        return 'All items must be numbers'
    else: 
        total = 0
        for i in range(1, n+1):
            if i%2 != 0:
                total += i
        return total
print(sum_of_odds(10))     
print(sum_of_odds('a'))           

#15.Declare a function named sum_of_evens. It takes a number parameter and it adds all the even numbers in that range.
def sum_of_evens(n):
    if not isinstance(n,(int, float)):
        return 'All items must be numbers'
    else: 
        total = 0
        for i in range(1, n+1):
            if i%2 == 0:
                total += i
        return total
print(sum_of_evens(10))     
print(sum_of_evens('a'))           
