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