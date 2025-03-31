# dir sẽ trả về danh sách các thuộc tính, phương thức, hàm, biến của một đối tượng
# Để sử dụng dir, bạn cần import module mà bạn muốn kiểm tra
import datetime
print(dir(datetime))

#lấy thông tin về datetime
from datetime import datetime as dt
now = dt.now()
print(now)
day = now.day
month = now.month
hour = now.hour                 
minute = now.minute           
second = now.second
print(f"{day}/{month}/{hour}, {minute}:{second}")

timestamp = now.timestamp() # timestamp là số giây từ 1/1/1970 đến thời điểm hiện tại
print(f'timestamp:{timestamp}')

#định dạng date đầu ra, sử dụng strftime
from datetime import datetime as dt
new_year = dt(2025,1,1) #2025-01-01 00:00:00
print(new_year)
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(f'{day}/{month}/{year}, {hour}:{minute}')

from datetime import datetime as dt
now = dt.now()
t = now.strftime('%H:%M:%S')
print(f'Bây giờ là: {t}')

time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
print(time_one)

# chuỗi (string) dùng strptime
from datetime import datetime as dt
date_string = '31 March 2025'
print(f'Date string = {date_string}')  #Date string = 31 March 2025
date_object = dt.strptime(date_string,'%d %B %Y')
#argument thứ 2 trong strptime phải giống với chuỗi ban đầu
print(f'Date object= {date_object}') #Date object= 2025-03-31 00:00:00

#dùng date từ datetime
from datetime import date as d
d = d(2025,3,31)
print(d) #2025-03-31
print(d.today())
today = d.today()
print(today.year)
print(today.month)
print(today.day)

#đối tượng time để đại diện cho thời gian
from datetime import time as t
a = t()
print(a) #00:00:00
b = t(10,30,50)
print(b) #10:30:50
c = t(hour=10, minute=30, second=50)
print(c) #10:30:50
d = t(hour=10, minute=30, second=50, microsecond=1000)
print(d) #10:30:50.001000 giả sử microsecond=200555 thì là .200555

#chênh lệch giữa 2 thời gian
from datetime import date, datetime
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
# Time left for new year:  27 days, 0:00:00
print('Time left for new year: ', time_left_for_newyear)

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff) # Time left for new year: 26 days, 23: 01: 00

#chênh lệch giữa 2 thời gian, dùng timedelta
from datetime import timedelta as td
t1 = td(weeks=12, days=10, hours=4, seconds=20)
t2 = td(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)
'''date_string = 5 December, 2019
    date_object = 2019-12-05 00:00:00
    t3 = 86 days, 22:56:50'''