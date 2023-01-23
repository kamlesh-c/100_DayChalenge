#day 23
#list method
a = [1,6,21,13,14,50,6]
print (a)
a.append(7)
print (a)
a.reverse()
print(a)
a.sort()
print (a)
a.sort(reverse=True)
print (a)
print (a)
co= a.count(6)
print (co)
newl = a.copy()
print (newl)
newl[0]=0
print (newl)
print ("-------------")
print ("List a = ", a)
l1 = [100,200,300]
print ("List a = ", l1)
print ("extening a with l1")
a.extend(l1)
print (a)
print ("-------------")
print ("List a = ", a)
l1 = [100,200,300]
print ("List a = ", l1)
m1 = [777,333,444]
print("adding or concating two list")
k = l1 + m1 + a
print (k)
print (k.count(100))
