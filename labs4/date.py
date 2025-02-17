#2program to print yesterday, today, tomorrow
import datetime

current_time = datetime.datetime.now()
tomorrow = current_time + datetime.timedelta(days=1)
yesterday = current_time - datetime.timedelta(days=1)

print("Yesterday's date:", yesterday)
print("Today's date: ", current_time)
print("Tomorrow's date: ", tomorrow)


#1  program to subtract five days from current date.
import datetime
time_now = datetime.datetime.now()
time_5days = time_now - datetime.timedelta(days=5)

print("5 days ago date:", time_5days)

#3microsecond
import datetime

current_time = datetime.datetime.now()

print(current_time.replace(microsecond=0))

#4calculate two date difference in seconds.
import datetime

year_1 = int(input("Input ur year: "))
month_1 = int(input("input ur month: "))
day_1 = int(input("Input ur day: "))
hour_1 = int(input("Input ur hour: "))
min_1 = int(input("Input ur minute: "))
sec_1 = int(input("Input ur second: "))
msec_1 = int(input("Input ur microsecond: "))

year_2 = int(input("Input ur year: "))
month_2 = int(input("input ur month: "))
day_2 = int(input("Input ur day: "))
hour_2 = int(input("Input ur hour: "))
min_2 = int(input("Input ur minute: "))
sec_2 = int(input("Input ur second: "))
msec_2 = int(input("Input ur microsecond: "))

time1 = datetime.datetime(year_1, month_1, day_1, hour_1, min_1, sec_1, msec_1)
time2 = datetime.datetime(year_2, month_2, day_2, hour_2, min_2, sec_2, msec_2)

time_diff = abs(time1 - time2)
print(time_diff.total_seconds())
