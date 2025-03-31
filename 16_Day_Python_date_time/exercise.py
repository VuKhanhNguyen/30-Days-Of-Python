#1.Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime as dt
now = dt.now()
print(f'Day:{now.day}, Month:{now.month}, Year:{now.year}, Hour:{now.hour}, Minute:{now.minute}, TimeStamp:{now.timestamp()}')

#2.Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
from datetime import datetime as dt
now = dt.now()
print(f'Day:{now.day}, Month:{now.month}, Year:{now.year}, Hour:{now.hour}, Minute:{now.minute}, TimeStamp:{now.timestamp()}')
formatCurrentDate = now.strftime('%m/%d/%Y, %H:%M:%S')
print(formatCurrentDate)

#3.Today is 5 December, 2019. Change this time string to time.
from datetime import datetime as dt
TodayIs = '5 December 2019'
changeToTime = dt.strptime(TodayIs,'%d %B %Y')
print(changeToTime)

#4.Calculate the time difference between now and new year.
from datetime import datetime as dt, date as d
now = dt.now()
newyear = dt(2026, 2, 1)
diff = newyear - now
print(now)
print(newyear)
print(diff)

#5.Calculate the time difference between 1 January 1970 and now.
from datetime import datetime as dt, timedelta as td
now = dt.now()
past_time = dt(1970, 1, 1) 
print(past_time)
diff = now - past_time
print(diff)


