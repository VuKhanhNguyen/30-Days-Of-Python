'''
34.Use a tab escape sequence to write the following lines.
Name      Age     Country   City
Asabeneh  250     Finland   Helsinki
'''

str = 'Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki'
print(str.expandtabs(10))