#3. Declare a variable named company and assign it to an initial value "Coding For All".
#4. Print the variable company using _print()_.
#5. Print the length of the company string using _len()_ method and _print()_.
#6. Change all the characters to uppercase letters using _upper()_ method.
#7. Change all the characters to lowercase letters using _lower()_ method.
#8. Use capitalize(), title(), swapcase() methods to format the value of the string _Coding For All_.
#9. Cut(slice) out the first word of _Coding For All_ string.
#10. Check if _Coding For All_ string contains a word Coding using the method index, find or other methods.
company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[1:])

print(company.find("o"))
print(company.index("o"))

is_present1 = company.find('o')
print(is_present1)
is_present2 = company.index('o')
print(is_present2)
is_present3 = 'Coding' in company
print(is_present3)
# print(company[0:1])