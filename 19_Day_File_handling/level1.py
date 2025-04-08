#1.Write a function which count number of lines and number of words in a text. All the files are in the data the folder: 
# a) Read obama_speech.txt file and count number of lines and words 
# b) Read michelle_obama_speech.txt file and count number of lines and words 
# c) Read donald_speech.txt file and count number of lines and words 
# d) Read melina_trump_speech.txt file and count number of lines and words



file_path = 'K:/AllOfPython/pythonLearning/30daysofPython/30-Days-Of-Python_NVK/30-Days-Of-Python/data/obama_speech.txt'
with open(file_path) as f:
    lines = f.read().splitlines()
def count_NumberLine_and_NumberWord(lines):    
        count_line = 0
        count_word = set()  
        for i in lines:
            if i.strip() != '':
                words = i.split()
                print(words)
                count_word.update(words)
                # count_word += len(words)
                # count_line += lines.count(i) 
                count_line += 1               
        print(f'Tổng từ là : {len(count_word)}')        
        print(f'Tổng dòng là : {count_line}')    
              
    
count_NumberLine_and_NumberWord(lines)            


#2.Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
import json
file_path = 'K:/AllOfPython/pythonLearning/30daysofPython/30-Days-Of-Python_NVK/30-Days-Of-Python/data/countries_data.json'
with open(file_path, 'r', encoding='utf-8') as file:
    json_data = json.load(file)
    '''hoặc là
        content = file.read()
        json_data = json.loads(content)'''
# print(json_data)
'''json.load(): Đọc từ file-like object (file đã mở)
json.loads(): Đọc từ string (chuỗi)
Nên sử dụng thêm encoding='utf-8' khi mở file để đảm bảo xử lý đúng các ký tự Unicode.'''

def most_10 (n = 10):
    count = {}
    for country in json_data:
        for language in country.get('languages'):
            if language in count:
                count[language] += 1
            else:
                count[language] = 1 
    sorted_lang = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return sorted_lang[:n]           
print(most_10(10))    

#3.Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
import json
file_path = 'K:/AllOfPython/pythonLearning/30daysofPython/30-Days-Of-Python_NVK/30-Days-Of-Python/data/countries_data.json'
with open(file_path, 'r', encoding='utf-8') as file:
   json_data = json.load(file)  

def most_populated(n=10):
    count = {}
    for country in json_data:
        population = country.get('population')
        count[country.get('name')] = population
    sorted_pop = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return sorted_pop[:n]
print(most_populated(10))





