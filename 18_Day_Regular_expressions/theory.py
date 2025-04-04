#regular expressions: Biểu thức chính quy hoặc RegEx là chuỗi văn bản đặc biệt giúp tìm các mẫu trong dữ liệu. 
# RegEx có thể được sử dụng để kiểm tra xem một số mẫu có tồn tại trong một kiểu dữ liệu khác hay không. 
# Để sử dụng RegEx trong python, trước tiên chúng ta phải nhập mô-đun RegEx có tên là re.

#các phương thức của re:
import re
re.match() # chỉ tìm kiếm ở đầu dòng đầu tiên của chuỗi và trả về các đối tượng khớp nếu tìm thấy, nếu không thì trả về None.
re.search() #Trả về một đối tượng khớp nếu có đối tượng đó ở bất kỳ đâu trong chuỗi, bao gồm cả chuỗi nhiều dòng.
re.findall() #Trả về một danh sách tất cả các đối tượng khớp trong chuỗi.
re.split() # Lấy một chuỗi, chia nó tại các điểm khớp, trả về một danh sách
re.sub() #Thay thế một hoặc nhiều kết quả khớp trong một chuỗi Kết quả khớp

#match()
import re
txt = 'i hate python very much'
match = re.match('i hate',txt,re.I) # re.I là một cờ cho phép tìm kiếm không phân biệt chữ hoa chữ thường
print(match) #<re.Match object; span=(0, 6), match='i hate'>
span = match.span() # span() trả về vị trí bắt đầu và kết thúc của chuỗi khớp
print(span) #(0, 6)
start, end = span
print(start , end)
substring = txt[start:end]
print(substring)

#search()
import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>

span = match.span()
print(span)     # (100, 105)

start, end = span
print(start, end)  # 100 105
substring = txt[start:end]
print(substring)       # first


#findall() 
import re
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It return a list
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']


#sub()
import re
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.
# OR
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.

#================================================================
txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)


#split()
import re

txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt))

#regex pattern
import re
regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']

# To make case insensitive adding flag '
matches = re.findall(regex_pattern, txt, re.I)
print(matches)  # ['Apple', 'apple']
# or we can use a set of characters method
regex_pattern = r'[Aa]pple'  # this mean the first letter could be Apple or apple
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']