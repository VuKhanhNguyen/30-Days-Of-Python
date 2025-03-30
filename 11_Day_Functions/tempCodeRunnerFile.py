from countries_data import countries_list
def most_spoken_language(n=10):
    count = {}
    for country in countries_list:
        for language in country.get('languages'):
            if language in count:
                count[language] += 1
            else:
                count[language] = 1
    sorted_lang = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return sorted_lang[:n]
print(most_spoken_language(10))
            
def most_populated_countries(n=10):
    count = {}
    for country in countries_list:
        population = country.get('population')
        count[country.get('name')] = population
    sorted_pop = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return sorted_pop[:n]
print(most_populated_countries(10))