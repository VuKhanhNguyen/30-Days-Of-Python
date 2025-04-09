#2. Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
# the min, max, mean, median, standard deviation of cats' weight in metric units.
# the min, max, mean, median, standard deviation of cats' lifespan in years.
# Create a frequency table of country and breed of cats

import requests
response = requests.get('https://api.thecatapi.com/v1/breeds')
print(response)
cats = response.json()

weights = []
lifespans = []
country_breed = {}

for cat in cats:
    weight = cat.get('weight', {}).get('metric', '')
    if weight and ' - ' in weight:
        min_w, max_w = map(float, weight.split(' - '))
        weights.append((min_w + max_w)/2)
    lifespan = cat.get('life_span', '')
    
    if lifespan and ' - ' in lifespan:
        min_l, max_l = map(float, lifespan.split(' - '))
        lifespans.append((min_l + max_l) / 2)

    # Bảng tần suất quốc gia và giống mèo
    country = cat.get('origin', 'Unknown')
    country_breed[country] = country_breed.get(country, 0) + 1    
def calc_stats(values):
    n = len(values)
    sorted_vals = sorted(values)
    mean = sum(values) / n
    median = sorted_vals[n // 2] if n % 2 == 1 else (sorted_vals[n // 2 - 1] + sorted_vals[n // 2]) / 2
    variance = sum((x - mean) ** 2 for x in values) / (n - 1)
    std_dev = variance ** 0.5
    return min(values), max(values), mean, median, std_dev    

w_min, w_max, w_mean, w_median, w_std = calc_stats(weights)
print("🐱 Weight (kg):")
print(f"Min: {w_min}, Max: {w_max}, Mean: {round(w_mean, 2)}, Median: {w_median}, Std Dev: {round(w_std, 2)}")

l_min, l_max, l_mean, l_median, l_std = calc_stats(lifespans)
print("\n🐾 Lifespan (years):")
print(f"Min: {l_min}, Max: {l_max}, Mean: {round(l_mean, 2)}, Median: {l_median}, Std Dev: {round(l_std, 2)}")

print("\n🌍 Frequency Table (Country: Number of Breeds):")
for country, count in sorted(country_breed.items(), key=lambda x: -x[1]):
    print(f"{country}: {count}")