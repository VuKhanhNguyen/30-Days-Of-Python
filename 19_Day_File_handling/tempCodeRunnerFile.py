with open('K:/AllOfPython/pythonLearning/30daysofPython/30-Days-Of-Python_NVK/30-Days-Of-Python/files/reading_file_example.txt','a') as f:
    f.write('This text has to be appended at the end')
    txt = f.read()    
    print(txt)