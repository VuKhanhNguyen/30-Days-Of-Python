'''1.  Use for loop to iterate from 0 to 100 and print the sum of all numbers.

   ```sh
   The sum of all numbers is 5050.
   ```'''
sum = 0
for num in range(0,101):
    sum = sum + num
print(f'Tổng là: {sum}')   
  
#================================================================
   
'''1. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

    ```sh
    The sum of all evens is 2550. And the sum of all odds is 2500.
    ```
   '''   
   
OddSum = 0
EvenSum = 0
for num in range(0,101):
    if num % 2 == 0:
        EvenSum = EvenSum + num
    elif num % 2 != 0:
        OddSum = OddSum + num   
print(f'Tổng chẵn là : {EvenSum} và tổng lẻ là: {OddSum}')