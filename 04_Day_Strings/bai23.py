'''
#23. Use index or find to find the position of the first occurrence of the word 'because' 
in the following sentence: 'You cannot end a sentence with because because because is a conjunction' 
'''

'''
#24. Use rindex to find the position of the last occurrence of the word because 
in the following sentence: 'You cannot end a sentence with because because because is a conjunction' 
'''

'''
#25. Slice out the phrase 'because because because' in the following sentence: 
'You cannot end a sentence with because because because is a conjunction'
'''

'''
#26. Find the position of the first occurrence of the word 'because' in the following sentence:
'You cannot end a sentence with because because because is a conjunction'
'''

'''
#27. Slice out the phrase 'because because because' in the following sentence: 
'You cannot end a sentence with because because because is a conjunction'
'''

strr = 'You cannot end a sentence with because because because is a conjunction'
findString = strr.find('because') #23
print(findString)

findString2 = strr.rindex('because') #24
print(findString2)

sliceString = strr.split()
sliceString2 = ' '.join([i for i in sliceString if i != 'because']) #25
print(sliceString2)     



findString = strr.find('because') #26
print(findString) 


sliceString3 = strr.split()
sliceString4 = ' '.join([i for i in sliceString3 if i!='because']) #27
print(sliceString4)     