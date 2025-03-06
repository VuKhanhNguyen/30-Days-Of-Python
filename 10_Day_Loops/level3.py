# 1. Go to the data folder and use the [countries.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) file. 
# Loop through the countries and extract all the countries containing the word _land_.

import countries
#print(countries.countries_list)

for i in countries.countries_list:
    if 'land' in i:
        print(i)
print()

# 1. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruit_list = ['banana', 'orange', 'mango', 'lemon']
empty_list = []
for r in fruit_list:
    if r not in empty_list:
        empty_list.append(r)
    print(empty_list)
empty_list.reverse()
print(empty_list)    
# reverseList = list(reversed(empty_list))
# print(reverseList)

# 2. Go to the data folder and use the [countries_data.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file. 
#    1. What are the total number of languages in the data
#    2. Find the ten most spoken languages from the data
#    3. Find the 10 most populated countries in the world
import countries_data
totalLanguages = set()
for i in countries_data.country_list:
    totalLanguages.update(i['languages'])

total_languages = len(totalLanguages)
print(f"Total number of languages: {total_languages}")
#----------------------------------------------------------------
from collections import Counter
languages = []
for i in countries_data.country_list:
    languages.extend(i['languages'])
totalLanguages = Counter(languages)
print(totalLanguages.most_common(10))
#----------------------------------------------------------------
k = sorted(countries_data.country_list, key=lambda x: x['population'], reverse=True)
for i in k[:10]:
    print(i['name'], i['population'])

#================================================================
# import importlib.util
# import os
# file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/countries.py'))
# spec = importlib.util.spec_from_file_location("countries", file_path)
# countries_module = importlib.util.module_from_spec(spec)
# spec.loader.exec_module(countries_module)

# print(countries_module.countries_list)  # Truy cập danh sách quốc gia