#1.Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number  
def odds_and_evens(n):
    countE = 0
    countO = 0
    for i in range(0, n+1):
        if i % 2 == 0:
            countE += 1 
        else:
            countO += 1
    return f'Số chẵn có: {countE}\nSố lẻ có: {countO}'        
print(odds_and_evens(100))    

#2.Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(n):
    if n <= 1:
        return 1
    else :
        return n * factorial(n-1)
print(factorial(10))    

#3.Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(n):
    if len(n) == 0:
        return True
    else:
        return False
print(is_empty([]))

#4.
def calculate_mean(lst):
    sum = 0
    if len(lst) == 0:
        return 0
    else:
        for i in lst:
            sum += i
        return sum / len(lst)
print(calculate_mean([1,2,3,4,5]))
    
def calculate_median(lst):
    if len(lst) == 0:
        return 0
    else:
        lst.sort()
        #for i in lst:
        if len(lst) % 2 !=0:
            return lst[int(len(lst)/2)]
        else:
            return ( lst[int(len(lst)/2)] + lst[int((len(lst)/2))-1] )/2
print(calculate_median([1,2,3,4,5,6,7])) #4
print(calculate_median([1,2,3,4,5,6,7,8])) #4.5

def calculate_mode(lst):
    if len(lst) == 0:
        return 0
    else:
        count = 0
        #empty_lst = []
        for i in lst:
            if lst.count(i) > count:
                count = lst.count(i)
                mode = i
        return mode
print(calculate_mode([1,2,3,3,3,4,5,6,7,8,8])) #3

def calculate_range(lst):
    if len(lst) == 0:
        return 0
    else:
        return max(lst) - min(lst)
print(calculate_range([1,2,3,4,5,6,7]))

def calculate_variance(lst):
    if len(lst) == 0:
        return 0
    elif len(lst) < 2:
        return f'Variance is not defined for a single value'
    else: 
        summ = 0
        for i in lst:
            summ += i
        mean = summ/len(lst)
        square_diff = 0
        for i2 in lst:
            square_diff += (i2 - mean) ** 2
        total = square_diff
    return total / len(lst)
print(calculate_variance([1,2,3,4,5,6,7]))

def calculate_std (lst):
    if len(lst) == 0:
        return 0
    elif len(lst) < 2:
        return f'Variance is not defined for a single value'
    else:
         total_sum = 0
         for i in lst:
             total_sum += i     
         mean = total_sum / len(lst)
         square_diff = 0
         for i2 in lst:
             square_diff += (i2 - mean) ** 2
         total = square_diff
    standard = (total / len(lst)) ** 0.5        
    return standard
print(calculate_std([1,2,3,4,5,6,7])) #2.0
