# Day 15
# Exercise 2
# from time import time,ctime
import time
print("Time is :")
print("Time.ctime=", time.ctime())
print("Time.localtime= ", time.localtime())
print("Geting time in sec. from Epoch Time.time= ", time.time())
print(time.strftime("%d,%I,%M  ,%w,", time.gmtime()))
print(time.strftime("%x,%X,%z", time.gmtime()))
print("***")
day = time.strftime("Day is :  %A", time.localtime())
month = time.strftime("Month is :  %B", time.localtime())
date= time.strftime("date is :  %d", time.localtime())
year= time.strftime("year is :  %Y", time.localtime())
hours= time.strftime("Hour is :  %H", time.localtime())
minute = time.strftime("Minute is :  %M", time.localtime())
second= time.strftime("Second is :  %S", time.localtime())
print("********")
print(day)
print(date)
print(month)
print(year)
print(hours)
print(minute)
print(second)
print("********")

