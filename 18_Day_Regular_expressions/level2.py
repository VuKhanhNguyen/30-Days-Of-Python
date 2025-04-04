#1.Write a pattern which identifies if a string is a valid python variable
import re
def is_valid_variable(string):
    regpattern = r'^[a-zA-Z][a-zA-Z0-9_]+$' #Dấu $ đảm bảo chuỗi kết thúc ngay sau phần hợp lệ, không có ký tự dư thừa nào khác sau đó.
    match = re.match(regpattern, string)
    if match:
        print('True')
    else:
        print('False')
is_valid_variable('first_name') # True
is_valid_variable('first-name') # False
is_valid_variable('1first_name') # False
is_valid_variable('firstname') # True    