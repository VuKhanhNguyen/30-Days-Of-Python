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
print(calculate_std([1,2,3,4,5,6,7,8])) #2.0
