#Day 20.2
#checking inbuild function of python
a = 10
b = "abc"
d= 3.14
e = 15
ans = max(a,e)
print ("max",ans)
ans = min(a,e)
print ("min",ans)
ans= type(a)
print(ans)
ans= pow(a,2)
print(ans)
print("printing range function: ")
for ans in range(a,e):
    print(ans,end="\t")
print ("End for",end="\n")
a = 10
b = "abc"
d= 3.14
e = 15
f= ["a","b","c","d"]
slicefn = slice(2)
print(f[slicefn])