#Day 24
# Tuple  Tuple are imutable
tup = (1,4,7,3,4,2,1)
print(type(tup),tup)
print(tup[0])
print(tup[3])
print("lentget of tuple", len(tup))
if 4 in tup:
    print("4 is in tuple")
else:
    print("not present")
t1= tup[1:4]
print (t1,"type of t1 :",type(t1))
