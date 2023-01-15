# Day 15
# Exercise 2
# from time import time,ctime
import time
print("Time is :")
print("Time.ctime=", time.ctime())
print("Time.localtime= ", time.localtime())
print("Time.time= ", time.time())
print(time.strftime("%d,%I,%M  ,%w,", time.gmtime()))
print(time.strftime("%x,%X,%z", time.gmtime()))
print("***")
#print(time.strftime("%x,%X,%z",time.ctime()))
print("***")
#print(time.get_clock_info())