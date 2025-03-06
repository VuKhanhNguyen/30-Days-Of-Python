# 1. Iterate 0 to 10 using for loop, do the same using while loop.
# 2. Iterate 10 to 0 using for loop, do the same using while loop.

for i in range(0,11):
    print(i)
print('\n')
#----------------------------------------------------------------1
i1 = 0    
while i1 <= 10:
    print(i1)
    i1 += 1
print('\n') 
#----------------------------------------------------------------1   
for i in range(10,-1,-1):
    print(i)
print('\n')
#----------------------------------------------------------------2
i1 = 10    
while i1 >= 0:
    print(i1)
    i1 -= 1 
#----------------------------------------------------------------2      


#================================================================
'''3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:

   ```py
     #
     ##
     ###
     ####
     #####
     ######
     #######
   ```

'''

for hang in range(0,7):
    for cot in range(0,7+1):
        print('#', end='') 
    print()
#----------------------------------------------------------------    
for hang in range(1, 8):
    for cot in range(1, hang+1):
        print('#', end='') #(end='' giúp in trên cùng một dòng)
    print() # xuống dòng
#----------------------------------------------------------------    
for hang in range(1, 8):
    print('#' * hang)    


#================================================================
''' Use nested loops to create the following:

   ```sh
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   ```
   '''
   
for hangg in range(1,9):   
    for cott in range(1, 9):
            print('#' , end=' ')
    print()           


#================================================================  
num = 0 
while num in range(0,11):
    print(f'{num} x {num} = {num*num}')
    num += 1
print('\n')
#----------------------------------------------------------------
for numm in range(0,11):
    print(f'{numm} x {numm} = {numm*numm}')
    
#================================================================    

#6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.    
list = ['Python', 'Numpy','Pandas','Django', 'Flask']

for i in range(len(list)):
    print(list[i])
print('\n')
#----------------------------------------------------------------
for i in list:
    print(i)    
print('\n')    
#----------------------------------------------------------------
for index, i  in enumerate(list):
    print(f'{index}. {i}')
print('\n')
#----------------------------------------------------------------
i = 0
while i < len(list):
    print(list[i])
    i += 1
print('\n')


#================================================================
# 7. Use for loop to iterate from 0 to 100 and print only even numbers
# 8. Use for loop to iterate from 0 to 100 and print only odd numbers

print(f'Số chẵn từ 0-100 là: ')
for num in range(0, 101): 
    if num % 2 == 0:
        print(num)
print('\n')

print(f'Số lẻ từ 0-100 là: ')
for num in range(0, 101): 
    if num % 2 != 0:
        print(num)
print('\n')