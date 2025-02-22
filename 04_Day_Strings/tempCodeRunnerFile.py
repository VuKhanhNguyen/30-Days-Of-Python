strr = 'You cannot end a sentence with because because because is a conjunction'
findString = strr.find('because') #23
print(findString)

findString2 = strr.rindex('because') #24
print(findString2)

sliceString = strr.split()
sliceString2 = ' '.join([i for i in sliceString if i != 'because'])
print(sliceString2)     