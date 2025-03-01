'''Check if an item exists in tuple:
Check if 'Estonia' is a nordic country

Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')'''



nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
found_1 = False
found_2 = False
for i in nordic_countries:
    if i == 'Estonia':
         print('Estonia is a nordic country') 
         found_1 = True  
    #print('Not a nordic country')
    if i == 'Iceland':         
         print('Iceland is a nordic country') 
         found_2 = True    
    #print('Not a nordic country')
if not found_1:    
    print('Not a nordic country')
if not found_2:    
    print('Not a nordic country')
    
#================================================================    
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

if 'Estonia' in nordic_countries:
    print('Estonia is a nordic country')
else:
    print('Not a nordic country')

if 'Iceland' in nordic_countries:
    print('Iceland is a nordic country')
else:
    print('Not a nordic country')
   