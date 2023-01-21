# Day 21 (I deleted 1 video for learn Funtion and Function argument
#Funtion Basic (Funtion is block of code we can use multiple time

print('Creating funtion for checkking greater number ')
def isgreater (a, b):
    if (a>b):
        print ( a, "Is greater that", b)
    elif (a == b):
        print ("both number are same ")
    else:
        print (b," Is greater than ", a)

a = 10
b = 20
print ("checking in for a= 10 and b=20")
isgreater(a, b)

c= 5
d= 2
print ("checking in for c= 5 and d=2")
isgreater(c, d)

e = 7
f = 7
print ("checking in for e= 7 and f=7")
isgreater(e, f)

