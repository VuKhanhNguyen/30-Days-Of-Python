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