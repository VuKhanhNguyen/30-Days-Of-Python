'''
31. Which one of the following variables return True when we use the method isidentifier():
    -30DaysOfPython
    -thirty_days_of_python
'''

str1 = '30DaysOfPython'
str2 = 'thirty_days_of_python'
check1 = str1.isidentifier()
check2 = str2.isidentifier()
print(check1, check2)