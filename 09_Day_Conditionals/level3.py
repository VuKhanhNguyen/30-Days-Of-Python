'''* Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
     * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
     * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
     * If the person is married and if he lives in Finland, print the information in the following format:
     
    Asabeneh Yetayeh lives in Finland. He is married.     '''
    
    
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
middleSkill = int(len(person['skills'])/2)
print (middleSkill)
if person.get('skills'):
    print(person['skills'][middleSkill])
    if 'Python' in person.get('skills'):
        print('Python is in skills')
if set(person.get('skills')) == {'JavaScript', 'React'}:
    print('He is front-end developer')
elif set(person.get('skills')) == {' Node', 'MongoDB', 'Python'}:
    print('He is backend developer')
else:
    print('He is fullstack developer')            
        

if person.get('is_married') and person.get('country') == 'Finland':
    print(f'{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.')
