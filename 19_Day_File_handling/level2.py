#4.Extract all incoming email addresses as a list from the email_exchange_big.txt file.
file_path = 'K:/AllOfPython/pythonLearning/30daysofPython/30-Days-Of-Python_NVK/30-Days-Of-Python/data/email_exchanges_big.txt'
with open(file_path) as f:
    lines = f.read().splitlines()
    # print(lines)


def extract_email(lines):

    email = []
    for i in lines:
        if i.startswith('From '):
            word = i.split()
            if '@' in word[1]:
                email.append(word[1])
    return email            
print(extract_email(lines))       



#5.Find the most common words in the English language. 
# Call the name of your function find_most_common_words, 
# it will take two parameters - a string or a file and a positive integer, 
# indicating the number of words. Your function will return an array of tuples in descending order.            

def find_most_common_words(file_path, n):
    with open(file_path, 'r') as f:
        text = f.read().splitlines()
        print(text)
        dct = {}
        for i in text:
            word = i.split()
            print(word)
            for j in word:
                if j in dct:
                    dct[j] += 1
                else: 
                    dct[j] = 1
            
            
        sortedWord = sorted(dct.items(), key = lambda x: x[1], reverse=True)
        return [(count,word)for word, count in sortedWord[:n]]
    
result = find_most_common_words('K:/AllOfPython/pythonLearning/30daysofPython/30-Days-Of-Python_NVK/30-Days-Of-Python/files/reading_file_example.txt',10)
print(result)


#6.Use the function, find_most_frequent_words to find: 
# a) The ten most frequent words used in Obama's speech 
# b) The ten most frequent words used in Michelle's speech 
# c) The ten most frequent words used in Trump's speech 
# d) The ten most frequent words used in Melina's speech


file_path = 'K:/AllOfPython/pythonLearning/30daysofPython/30-Days-Of-Python_NVK/30-Days-Of-Python/data/obama_speech.txt'
with open(file_path) as f:
    lines = f.read().splitlines()
def find_most_frequent_words(lines):
    dct = {}
    count_word = set()  
    for i in lines:
        if i.strip() != '':
            words = i.split()            
            count_word.update(words)
        for j in words:
            if j in dct:
                dct[j] += 1
            else:
                dct[j] = 1
    sortedWord = sorted(dct.items(), key = lambda x: x[1], reverse=True)
    return [(count, word) for word, count in sortedWord[:]]                                     
print(find_most_frequent_words(lines))  


#7.Write a python application that checks similarity between two texts. 
# It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. 
# For instance check the similarity between the transcripts of Michelle's and Melina's speech. 
# You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity).
# List of stop words are in the data directory

def clean_text(file_path):
    with open(file_path) as f:
        text = f.read().splitlines()
        # print(text)
        cleanText = []
        for i in text:
            if i.strip() != '':
                cleanText.append(i.strip().lower())
        return cleanText     
def remove_support_words(file_path):
    ct = clean_text(file_path) 
    # print(ct)
    
    with open('K:/AllOfPython/pythonLearning/30daysofPython/30-Days-Of-Python_NVK/30-Days-Of-Python/data/stop_words.py') as f:
        stop_words = f.read()
        print(stop_words)
        # stop_words = stop_words.split()
        # print(stop_words)
        for i in stop_words:
            if i in ct:
                ct.remove(i)
        return ct
def check_text_similarity(file_path1, file_path2):
    ct1 = remove_support_words(file_path1)
    ct2 = remove_support_words(file_path2)
    # print(ct1)
    # print(ct2)
    set1 = set(ct1)
    set2 = set(ct2)
    # print(set1)
    # print(set2)
    similarity = len(set1.intersection(set2)) / len(set1.union(set2)) 
    print(similarity)                 
check_text_similarity('K:/AllOfPython/pythonLearning/30daysofPython/30-Days-Of-Python_NVK/30-Days-Of-Python/data/michelle_obama_speech.txt', 'K:/AllOfPython/pythonLearning/30daysofPython/30-Days-Of-Python_NVK/30-Days-Of-Python/data/melina_trump_speech.txt')    


#8.Find the 10 most repeated words in the romeo_and_juliet.txt
def  most_repeated_words ():
    file_path = 'K:/AllOfPython/pythonLearning/30daysofPython/30-Days-Of-Python_NVK/30-Days-Of-Python/data/romeo_and_juliet.txt'
    with open(file_path) as f:
        lines = f.read().splitlines()
        dct = {}
        for i in lines:
            if i.strip() != '':
                words = i.split()
                for j in words:
                    if j in dct:
                        dct[j] += 1
                    else:
                        dct[j] = 1
        sorted_word = sorted(dct.items(), key= lambda x: x[1], reverse = True)
        result = [(count,word) for word, count in sorted_word[:10]]     
        return result   
print(most_repeated_words())                    


#9. Read the hacker news csv file and find out: 
# a) Count the number lines containing python or Python 
# b) Count the number lines containing JavaScript, javascript or Javascript 
# c) Count the number lines containing Java and not JavaScript
import csv
file_path = 'K:/AllOfPython/pythonLearning/30daysofPython/30-Days-Of-Python_NVK/30-Days-Of-Python/data/hacker_news.csv'
with open(file_path) as f:
    lines = csv.reader(f, delimiter=',') # delimiter dùng để tách các trường trong file csv
    line_count_py = 0
    line_count_js = 0
    line_count_java = 0
    for row in lines:
        row_text = ', '.join(row) # chuyển đổi các trường trong dòng thành một chuỗi
         
        if 'python' in row_text or 'Python' in row_text:
            line_count_py += 1
        if 'javascript' in row_text or 'Javascript' in row_text or 'JavaScript' in row_text:
            line_count_js += 1
        if 'Java' in row_text and 'Javascript' not in row_text:
            line_count_java += 1
print(row_text)           
print(line_count_py)
print(line_count_js)
print(line_count_java)                  