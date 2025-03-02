# 1. Find the length of the set it_companies
# 2. Add 'Twitter' to it_companies
# 3. Insert multiple IT companies at once to the set it_companies
# 4. Remove one of the companies from the set it_companies
# 5. What is the difference between remove and discard

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}


print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)

it_companies.update(['TikTok', 'Instagram','LinkedIn'])
print(it_companies)

it_companies.remove('TikTok')
print(it_companies)

#discard() sẽ không gây lỗi khi không có item tương ứng để xóa, ngược lại thì remove() sẽ báo lỗi
it_companies.discard('Messenger')
print(it_companies)
it_companies.remove('Messenger')
print(it_companies)
