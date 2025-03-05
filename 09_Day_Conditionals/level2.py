'''1. Write a code which gives grade to students according to theirs scores:
        80-100, A
        70-89, B
        60-69, C
        50-59, D
        0-49, F
'''
your_score = int(input("Enter your score: "))
if your_score >= 80 and your_score <= 100:
    print('Your grade is: \"A\"')
elif your_score >= 70 and your_score <=89:
    print('Your grade is: \"B\"')
elif your_score >= 60 and your_score <=69:
    print('Your grade is: \"C\"')
elif your_score >= 50 and your_score <=59:
    print('Your grade is: \"D\"')
elif your_score >= 0 and your_score <=49:
    print('Your grade is: \"F\"')
else:
    print('Invalid score')
    
    
'''1. Check if the season is Autumn, Winter, Spring or Summer. If the user input is:
    September, October or November, the season is Autumn.
    December, January or February, the season is Winter.
    March, April or May, the season is Spring
    June, July or August, the season is Summer'''
    
# season = str(input("Enter the season: ")).lower()  # Chuyển đầu vào thành chữ thường
# if season in ['september', 'october', 'november']:
#     print('It is Autumn')
# elif season in ['december', 'january', 'february']:
#     print('It is Winter')
# elif season in ['march', 'april', 'may']:
#     print('It is Spring')
# elif season in ['june', 'july', 'august']:
#     print('It is Summer')
# else:
#     print('Invalid season entered')    
    
season = str(input("Enter the season: "))
if season == 'September' or season == 'October' or season == 'November':
    print('It is Autumn')
elif season == 'December' or season == 'January' or season == 'February':
    print('It is Winter')
elif season == 'March' or season == 'April' or season == 'May':
    print('It is Spring')
elif season == 'June' or season == 'July' or season == 'August':
    print('It is Summer')
    

 
'''If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
If the fruit exists print('That fruit already exist in the list')''' 
    
fruits = ['banana', 'orange', 'mango', 'lemon']
if 'tomato' not in fruits:
    fruits.append('tomato')
    print(fruits)
else: print('That fruit already exists in the list')    