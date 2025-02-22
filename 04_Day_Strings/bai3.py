#3. Declare a variable named company and assign it to an initial value "Coding For All".
#4. Print the variable company using _print()_.
#5. Print the length of the company string using _len()_ method and _print()_.
#6. Change all the characters to uppercase letters using _upper()_ method.
#7. Change all the characters to lowercase letters using _lower()_ method.
#8. Use capitalize(), title(), swapcase() methods to format the value of the string _Coding For All_.
#9. Cut(slice) out the first word of _Coding For All_ string.
#10. Check if _Coding For All_ string contains a word Coding using the method index, find or other methods.
#11. Replace the word coding in the string 'Coding For All' to Python.
#13. Split the string 'Coding For All' using space as the separator (split()) .
#16. What is the last index of the string _Coding For All_.
#17. What character is at index 10 in "Coding For All" string.
#19. Create an acronym or an abbreviation for the name 'Coding For All'.
#20. Use index to determine the position of the first occurrence of C in Coding For All.

company = 'Coding For All' #3
print(company) #4

print(len(company)) #5

print(company.upper()) #6

print(company.lower()) #7

print(company.capitalize()) #8
print(company.title()) #8
print(company.swapcase()) #8

print(company[1:]) #9

print(company.find("o")) #0
print(company.index("o")) #10

is_present1 = company.find('o') #10
print(is_present1)
is_present1_1 = company.find('o', is_present1+1)
print(is_present1_1)
is_present2 = company.index('o') #10
print(is_present2)
is_present3 = 'Coding' in company #10
print(is_present3)

newCompany = company.replace("Coding", "Python") #11
print(newCompany)

splitCompany = company.split(' ') #13
print(splitCompany)

findIndexCompany = company[-1] #16
print(findIndexCompany)

findIndexCompany2 = company[10] #17
print(findIndexCompany2)

abbreCompany = ''.join(i for i in company if i.isupper()) #19
print(abbreCompany)
abbreCompany2 = ''.join([i[0] for i in company.split()]) #19
print(abbreCompany2)


company = 'Coding For All'
   
findCharCompany = company[0]
findIndexCompany =  company.find(findCharCompany)
print(f'Chữ {findCharCompany} ở vị trí thứ {findIndexCompany}')

for index, char in enumerate(company):
    # findIndexCompany2 = company.find(char)
    print(f'Chữ {char} ở vị trí thứ {index}')