#file handling tức là thao tác với file, bao gồm đọc, ghi, xóa file
# 'r' : read - đọc file, nếu file không tồn tại thì sẽ báo lỗi
# 'w' : write - ghi file, nếu file đã tồn tại thì sẽ xóa nội dung cũ và ghi mới
# 'a' : append - ghi file, nếu file đã tồn tại thì sẽ thêm nội dung mới vào cuối file
# 'x' : exclusive creation - tạo file mới, nếu file đã tồn tại thì sẽ báo lỗi
# 't' : text - đọc ghi file dưới dạng text, mặc định là text
# 'b' : binary - đọc ghi file dưới dạng nhị phân, thường dùng cho file hình ảnh, âm thanh, video
# mặc định là 'r'

file_path = 'K:/AllOfPython/pythonLearning/30daysofPython/30-Days-Of-Python_NVK/30-Days-Of-Python/files/reading_file_example.txt'
f = open(file_path)
print(f)


#read() : đọc toàn bộ nội dung file và trả về chuỗi
file_path = 'K:/AllOfPython/pythonLearning/30daysofPython/30-Days-Of-Python_NVK/30-Days-Of-Python/files/reading_file_example.txt'
f = open(file_path)
txt = f.read()
print(type(txt))
print(txt)
txt2 = f.read(10) # đọc 10 ký tự đầu tiên
print(txt2) # không có gì vì đã đọc hết nội dung file rồi
f.close()

file_path = 'K:/AllOfPython/pythonLearning/30daysofPython/30-Days-Of-Python_NVK/30-Days-Of-Python/files/reading_file_example.txt'
f = open(file_path)
txt = f.read(10)
print(type(txt))
print(txt)
f.close()

#readline() : đọc 1 dòng trong file và trả về chuỗi
file_path = 'K:/AllOfPython/pythonLearning/30daysofPython/30-Days-Of-Python_NVK/30-Days-Of-Python/files/reading_file_example.txt'
f = open(file_path)
line = f.readline()
print(type(line))
print(line)
f.close()

#readlines() : đọc toàn bộ nội dung file và trả về list các dòng
file_path = 'K:/AllOfPython/pythonLearning/30daysofPython/30-Days-Of-Python_NVK/30-Days-Of-Python/files/reading_file_example.txt'
f = open(file_path)
lines = f.readlines()
print(type(lines))
print(lines)
f.close()

#splitlines() : tách các dòng trong file và trả về list các dòng
file_path = 'K:/AllOfPython/pythonLearning/30daysofPython/30-Days-Of-Python_NVK/30-Days-Of-Python/files/reading_file_example.txt'
f = open(file_path)
splitline = f.read().splitlines()
print(type(splitline))
print(splitline)
f.close()

#with open() : tự động đóng file sau khi đọc xong, không cần phải gọi f.close()
with open('K:/AllOfPython/pythonLearning/30daysofPython/30-Days-Of-Python_NVK/30-Days-Of-Python/files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)
    
#append : thêm nội dung vào cuối file    
with open('K:/AllOfPython/pythonLearning/30daysofPython/30-Days-Of-Python_NVK/30-Days-Of-Python/files/reading_file_example.txt','a') as f:
    f.write('This text has to be appended at the end')

#write : ghi nội dung vào file, nếu file đã tồn tại thì sẽ xóa nội dung cũ và ghi mới
with open('K:/AllOfPython/pythonLearning/30daysofPython/30-Days-Of-Python_NVK/30-Days-Of-Python/files/reading_file_example.txt','w') as f:
    f.write('This text has to be written in the file')
    
# delete : xóa file, nếu file không tồn tại thì sẽ báo lỗi
import os
os.remove('K:/AllOfPython/pythonLearning/30daysofPython/30-Days-Of-Python_NVK/30-Days-Of-Python/files/reading_file_example.txt')

import os
if os.path.exists('K:/AllOfPython/pythonLearning/30daysofPython/30-Days-Of-Python_NVK/30-Days-Of-Python/files/reading_file_example.txt'):
    os.remove('K:/AllOfPython/pythonLearning/30daysofPython/30-Days-Of-Python_NVK/30-Days-Of-Python/files/reading_file_example.txt')
else: 
    print('Đéo có file này đâu')









    