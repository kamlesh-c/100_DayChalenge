# Day 14
# if else statement (conditional statement )

age= int(input("Enter your age="))
print ("age is ", age )
# Conditioanl operate < > <= >= == !=
# print(age>18)
# print(age<18)
# print(age==18)
# print(age!=18)
# if (age >=18):
#     print ("Age is more than 18 can drive car/bike")
# else:
#     print("Age is less that  18 Can not  drive")

budget = int(200)
print ("Budge is =", budget)
price=  int(input("Enter apple prise:"))
cost = budget-price
if (cost>0):
    print ("apple's are cheap we can buy")
    if(cost == 1):
        print("only 1 rs save")
elif (cost==0):
    print("we can buy apple but budget is over aftet this buing ")
else:
    print("Apple are very costly ")
print("If condition ends here ")
