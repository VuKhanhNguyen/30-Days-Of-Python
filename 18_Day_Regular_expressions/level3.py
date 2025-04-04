#1.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
import re
match = re.sub('%','',sentence)
print(match)
regpattern = r'[^\w\s]' # [^\w\s] là một biểu thức chính quy để tìm tất cả các ký tự không phải là chữ cái, số hoặc khoảng trắng.
match2 = re.sub(regpattern, '', match)
print(match2)

lst = list(match2.split(' '))
print(lst)
lst2 = []
for c in set(lst):
    count = lst.count(c)
    result = count,c
    lst2.append(result)
lst2.sort(reverse=True)
print(lst2[0:3])