# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
# 1. Explain the difference between the following data types: string, list, tuple and set
# 2. _I am a teacher and I love to inspire and teach people.
#    _ How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

age = [22, 19, 24, 25, 26, 24, 25, 24]
ageSet = set(age)
print(ageSet)


strr = 'I am a teacher and I love to inspire and teach people'
strr = strr.lower()
setEmpty = set()    
splitStr = strr.split()
print(splitStr)
JoinStr = ''.join(splitStr)
print(JoinStr)
for char in JoinStr:
    # print(char)
    setEmpty.add(char)
print(setEmpty) 
print(len(setEmpty))   

#================================================================
#cách khác
strr = 'I am a teacher and I love to inspire and teach people'

# Chuyển về chữ thường
strr_lower = strr.lower()

# Lấy các từ duy nhất
unique_words = set(strr_lower.split())

# Lấy các ký tự duy nhất từ các từ duy nhất
unique_chars = set(''.join(unique_words))

print(unique_chars)
