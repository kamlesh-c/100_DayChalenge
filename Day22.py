#Day 22
# List
a = [1,2,3,4]
print (a)
print(a[0])
print(a[1])
colors = ["Red","Yellow","black","green","white"]
print (colors)
print (colors[4])

mix = [1,2,"Kamlesh",True]
print (mix)
print (mix[3])
print (mix[1])
print(type(mix[1]))
print(type(mix[2]))
print(type(mix[-3]))

#Negativ index
mix = [1,2,"Kamlesh",True]
print(mix[-3])# Negivet index
print(mix[len(mix)-3]) # convert -ve index to  +ve index

#find value in list
print("check 7 is presnt in list : ", mix)
#same thing useful in string
if 7 in mix:
    print("yes 7 presnet ")
else:
    print("No 7 not present ")

print("check 7 is presnt in list : ", mix)
print (mix[:])
print (mix[:-1])
print (mix[1:3])
#genrate list on fly(list comprehencive
list1= []
list1= [ i for i in range(10)]
print(list1)