#Day 16
#Match case
#this new update from 3.10
# x= int(input("Enter a number: "))
x = 3
match x:
    case 0:
        print("Case is zero")
    case 5:
        print("Case is 5")
    case 4:
        print("Case is 4")
    case _:
        print("this is default x")
        #this is default case define by _
