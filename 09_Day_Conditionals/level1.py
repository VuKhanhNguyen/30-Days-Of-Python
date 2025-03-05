'''1. Get user input using input(“Enter your age: ”). 
If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.'''

your_age = int(input('Enter your age: '))
if your_age >= 18:
    print('You are old enough to drive.')
else:
    print(f'You need to wait {18 - your_age} years to drive.')
    

'''2. Compare the values of my_age and your_age using if … else. 
Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.'''
# your_age = int(input('Enter your age: '))
# my_age = 30
# if your_age < my_age:
#     print(f'I\'m {my_age-your_age} years older than you.')
# elif your_age > my_age:
#     print(f'You are {your_age-my_age} years older than me.')
# else:
#     print('We are the same age.')

my_age = int(input('Enter my age: '))
if your_age < my_age:
    print(f'I\'m {my_age-your_age} years older than you.')
elif your_age > my_age: 
    print(f'You are {your_age-my_age} years older than me.')
else:
    print('We are the same age.')
    
    
    
'''3. Get two numbers from the user using input prompt. 
If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.'''    
    
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
if num1 > num2:
    print(f'{num1} is greater than {num2}.')
elif num1 < num2:
    print(f'{num2} is greater than {num1}.')
else:
    print(f'{num1} and {num2} are equal.')    