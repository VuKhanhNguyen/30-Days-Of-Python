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