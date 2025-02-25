# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
# 7. Print the list using _print()_
# 8. Print the number of companies in the list
# 9. Print the first, middle and last company
# 10. Print the list after modifying one of the companies
# 11. Add an IT company to it_companies
# 12. Insert an IT company in the middle of the companies list
# 13. Change one of the it_companies names to uppercase (IBM excluded!)
# 14. Join the it_companies with a string '#;&nbsp; '
# 15. Check if a certain company exists in the it_companies list.
# 16. Sort the list using sort() method
# 17. Reverse the list in descending order using reverse() method
# 18. Slice out the first 3 companies from the list
# 19. Slice out the last 3 companies from the list
# 20. Slice out the middle IT company or companies from the list
# 21. Remove the first IT company from the list
# 22. Remove the middle IT company or companies from the list
# 23. Remove the last IT company from the list
# 24. Remove all IT companies from the list
# 25. Destroy the IT companies list


it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'] #6
print(it_companies)
print(len(it_companies)) #8


findMiddle=int(len(it_companies)/2) #9

print(f'{it_companies[0]}, {it_companies[findMiddle]}, {it_companies[-1]}') #9

it_companies.append('IT') #11
print(it_companies)

it_companies.insert(findMiddle, 'TikTok') #12
print(it_companies)

print(it_companies[1].upper()) #13

print('#;'.join(it_companies)) #14

checkExist = 'Google' in it_companies #15
print(checkExist) 


it_companies.sort(reverse=True)
print(it_companies) #16

it_companies.reverse() #17
print(it_companies)

sliceCompany = it_companies[0:3] #18
print(sliceCompany)


sliceCompany2 = it_companies[-3:] #19
print(sliceCompany2)

sliceCompany3 = int(len(it_companies)/2) #20
print(it_companies[sliceCompany3-1:sliceCompany3+2])


#================================================================

it_companies = ['Amazon', 'Apple', 'Facebook', 'Google', 'IBM', 'IT', 'Microsoft', 'Oracle', 'TikTok']
print(it_companies)

it_companies.pop(0) #21
print(it_companies)

removeMiddle = int(len(it_companies)/2)
it_companies.pop(removeMiddle) #22
print(it_companies)

it_companies.pop(-1) #23
print(it_companies)

it_companies.clear() #24
print(it_companies)


it_companies = ['Amazon', 'Apple', 'Facebook', 'Google', 'IBM', 'IT', 'Microsoft', 'Oracle', 'TikTok']
it_companies.remove('IT') #25
print(it_companies)