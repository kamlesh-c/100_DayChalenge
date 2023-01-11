# Type Casting
#changing type of veriable

a="1"
b="2"
c=a+b
print("a=", a, "Type of a is ", type(a))
print("b=",b,"tpe of b is", type(b))
print("c=", c, "type of c is", type(c))

print("1) Explicite Type Casting (User ask to change type)")
a=int(a)
print("a=", int(a), "Type of a is ", type(a))
b=int(b)
print("b=",int(b),"tpe of b is", type(b))
c=int(a)+int(b)
print("c=", c, "type of c is", type(c))

print("Implicit Type Casting(Python self covert data type")
c=1.1
d=8
print("c=",c, "Type of c is", type(c))
print("d=",d, "Type of d is ",type(d))
e=c+d
print("e=c+d",e, "Type of e is ", type(e) )
f="a"
g=f+str(d)
print("g=",g,"tupe of g", type(g))