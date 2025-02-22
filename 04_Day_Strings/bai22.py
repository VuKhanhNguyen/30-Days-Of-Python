#22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
strr = 'Coding For All People'
for i in range(len(strr)):
    if i == strr.rfind('l'):
        print(f'l ở vị trí thứ {i} khi dùng \"rfind()\" để tìm!')