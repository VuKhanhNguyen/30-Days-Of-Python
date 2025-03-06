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