#Exercies 2
#IF Else statement  using Time module
import time
hour= int(time.strftime("%H", time.localtime()))
hh= print("Time hour :",time.strftime("%I,%p",time.localtime()))
#hour= int(17)
if hour < 12:
    print("Good Morning ")
elif hour >=12 and hour <=16:
    print("Good afternoon")
else:
    print("Good evening ")
print("The End ")