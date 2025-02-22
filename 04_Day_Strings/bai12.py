#12. Change Python for Everyone to Python for All using the replace method or other methods.
#18. Create an acronym or an abbreviation for the name 'Python For Everyone'.


strr = 'Python for Everyone' #12
newStrr = strr.replace("Everyone", "All") #cach 1
print(newStrr)

newStrr2 = strr.split(" ")
#print(newStrr2)
newStrr2[-1] = 'All'
newStrr3 = " ".join(newStrr2) #cach 2
print(newStrr3)

strr2 = 'Python For Everyone' #18
# newStrr = strr2[0]
# newStrr2 = strr2[7]
# newStrr3 = strr2[11]
# concatenateStr = ''.join([newStrr, newStrr2, newStrr3])
# print(concatenateStr)
newStrr = ''.join([i[0] for i in strr2.split()]) #18
# newStrr = "".join([i for i in strr2 if i.isupper()])
print(newStrr)