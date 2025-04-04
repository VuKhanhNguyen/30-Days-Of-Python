#1.What is the most frequent word in the following paragraph?
import re
paragraph = '''I love teaching. If you do not love teaching what else can you love. 
I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'''

regex_pattern = r'\w+'
match = re.findall(regex_pattern, paragraph, re.I)
print(match)
emptylst = []
#print(set(match))
for c in set(match):
    count = match.count(c)
    result = count,c
    emptylst.append(result)
emptylst.sort(reverse=True)    
print(emptylst)    

    
#2.The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
import re    
txt = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction'
regex_pattern = r'-?\d+'
match = re.findall(regex_pattern, txt)        
print(match)
intpoint = [int(n) for n in match]
print(intpoint)
distance = max(intpoint) - min(intpoint)
print(f'{max(intpoint)} - {min(intpoint)} = {distance}')


