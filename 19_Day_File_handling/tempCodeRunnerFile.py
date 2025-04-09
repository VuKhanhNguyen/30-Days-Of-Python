import csv
file_path = 'K:/AllOfPython/pythonLearning/30daysofPython/30-Days-Of-Python_NVK/30-Days-Of-Python/data/hacker_news.csv'
with open(file_path) as f:
    lines = csv.reader(f, delimiter=',') # delimiter dùng để tách các trường trong file csv
    line_count_py = 0
    line_count_js = 0
    line_count_java = 0
    for row in lines:
        row_text = ', '.join(row) # chuyển đổi các trường trong dòng thành một chuỗi
        print(row_text)  
        if 'python' in row_text or 'Python' in row_text:
            line_count_py += 1
        if 'javascript' in row_text or 'Javascript' in row_text or 'JavaScript' in row_text:
            line_count_js += 1
        if 'Java' in row_text and 'Javascript' not in row_text:
            line_count_java += 1
          
print(line_count_py)
print(line_count_js)
print(line_count_java)     