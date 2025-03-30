
def is_frime(n):
    if n == 1:
        return f'1 không phải là số nguyên tố'
    if n == 2:
        return f'2 là số nguyên tố'
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return f'{n} không phải là số nguyên tố'
    return f'{n} là số nguyên tố'
print(is_frime(10))