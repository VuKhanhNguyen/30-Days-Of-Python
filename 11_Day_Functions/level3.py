#1.Write a function called is_prime, which checks if a number is prime.
def is_prime(n):
    if n == 1:
        return f'1 không phải là số nguyên tố'
    if n == 2:
        return f'2 là số nguyên tố'
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return f'{n} không phải là số nguyên tố'
    return f'{n} là số nguyên tố'
print(is_prime(10))

#2.Write a functions which checks if all items are unique in the list.
def is_unique(lst):
    for i in lst:
        if lst.count(i) > 1:
            return False
    return True
        
print(is_unique([1,2,3,4,5,6,7,8,9,9,10]))       

#3.Write a function which checks if all the items of the list are of the same data type.
def is_same_type(lst):
    for i in lst:
        if type(i) != type(lst[0]):
            return False    
    return True
print(is_same_type([1,2,'a',4,5,6,7,8,9,10]))  
print(is_same_type([1,2,3,4,5,6,7,8,9,10]))  

#4.Write a function which check if provided variable is a valid python variable
def is_provide_variable(var):
    if var.isidentifier():
        return True
    else:
        return False
print(is_provide_variable('hello_world')) #True
print(is_provide_variable('hello world')) #False

#5.