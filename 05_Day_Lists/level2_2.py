# 1. Find the middle country(ies) in the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/tree/master/data/countries.py)
# 1. Divide the countries list into two equal lists if it is even if not one more country for the first half.
# 1. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.


from countries import countries_list
#print(countries_list)
print(len(countries_list))

middle = int(len(countries_list)/2)

if len(countries_list) % 2 != 0:
    print(countries_list[middle])
else :
    print(countries_list[middle-1:middle])    
    

if len(countries_list) % 2 == 0:  
    print(f'{countries_list[0:middle]}: {len(countries_list[0:middle])}')
    print('\n')
    print(f'{countries_list[middle:]}: {len(countries_list[middle:])}')
else:
    print(f'{countries_list[0:middle+1]}: {len(countries_list[0:middle])}')
    print('\n')
    print(f'{countries_list[middle+2:]}: {len(countries_list[middle+2:])}')
    
    
countries_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first, second, third, *scandic_countries = countries_list
print("First country:", first)
print("Second country:", second)
print("Third country:", third)
print("Scandic countries:", scandic_countries)
