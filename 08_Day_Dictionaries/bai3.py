# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
# 4. Get the length of the student dictionary
# 5. Get the value of skills and check the data type, it should be a list
# 6. Modify the skills values by adding one or two skills
# 7. Get the dictionary keys as a list
# 8. Get the dictionary values as a list
# 9. Change the dictionary to a list of tuples using _items()_ method
# 10. Delete one of the items in the dictionary
# 11. Delete one of the dictionaries

student = {'first_name': 'khanh', 
           'last_name' : 'nguyen',
           'gender': 'male', 
           'marial status': 'single',
           'skills': ['PYTHON', 'HTML', 'CSS', 'Javascript', 'JAVA', 'C#'],
           'country': 'Vietnam',
           'city': 'Da Nang',
           'address': {'Ward':'Hoa Phat', 'District':'Cam Le'}
           }
print(len(student))

print(student['skills'])
print(type(student['skills']))

student['skills'].append('SQL')
print(student)

print('\n')
print(student.keys())
print('\n')
print(student.values())
print('\n')
print(student.items())

print('\n')
del student['address']
print(student)
print('\n')

student.pop('city')
print(student)
print('\n')
popdict = student.pop('class','Not found')
print(popdict)

print('\n')
try:
    del student
    print(student) # NameError: name 'student' is not defined
except NameError as e: 
    print(f'Lỗi: "{e}"')

