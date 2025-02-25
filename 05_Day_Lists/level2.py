# - Sort the list and find the min and max age
# - Add the min age and the max age again to the list
# - Find the median age (one middle item or two middle items divided by two)
# - Find the average age (sum of all items divided by their number )
# - Find the range of the ages (max minus min)
# - Compare the value of (min - average) and (max - average), use _abs()_ method
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)

maxAges = max(ages)
print(f'Tuổi cao nhất: {maxAges}')

minAges = min(ages)
print(f'Tuổi thấp nhất: {minAges}')

#Tìm trung vị
# Khi số lượng phần tử là lẻ, trung vị là phần tử ở giữa.
# Khi số lượng phần tử là chẵn, trung vị là trung bình cộng của hai phần tử giữa.
if len(ages) % 2 != 0:
    temp = int(len(ages)/2)
    medianAges = ages[temp]
    print(f'Tuổi trung vị {medianAges}')
else:
    temp = int(len(ages)/2)
    temp2 = int(((temp-1)+temp)/2)
    medianAges = ages[temp2]
    print(f'Tuổi trung vị {medianAges}')
    
averageAges = int(sum(ages)/len(ages))
print(f'Tuổi trung bình: {averageAges}')

rangeAges = maxAges - minAges
print(f'Khoảng biến thiên tuổi: {rangeAges}')

a=abs(minAges-rangeAges)
b=abs(maxAges-rangeAges)
print(f'a={a}, b={b}')
if a>b:
   print('minAges-rangeAges lớn hơn maxAges-rangeAges')
elif a < b:
    print('minAges-rangeAges nhỏ hơn maxAges-rangeAges')
else: 
    print('minAges-rangeAges bằng maxAges-rangeAges')    