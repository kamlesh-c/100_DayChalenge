#Tupple menthod
a = (1,2,3,5)
print (a)
b = list(a)
print (b)
b.pop(3)
print(b)
b.append(4)
print("***********")
print (b)
a = tuple (b)
print("***********")
print (a)
c = ("a","b","c","d",1)
print (c)
d = a + c
print (d)
print(d.count(1))
print (d.index("a"))