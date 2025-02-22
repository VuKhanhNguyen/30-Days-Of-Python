company = 'Coding For All'
   
findCharCompany = company[0]
findIndexCompany =  company.find(findCharCompany)
print(f'Chữ {findCharCompany} ở vị trí thứ {findIndexCompany}')

for index, char in enumerate(company):
    # findIndexCompany2 = company.find(char)
    print(f'Chữ {char} ở vị trí thứ {index}')