#Self Exercies
#Fd Calculator
name = input("Enter you name :")
age = int(input("Enter you age:"))

print ("Hi ", name)

print("Please Check interest rate")
print("For 7 days to  45 Days: 3.75%")
print ("For 46 days to 90 days 4.25%")
print("For 91 days to 180 days 5%")
print("For 181 days to 365 days 6.10%")

print ("************")

priciple = int(input("please enter Principle ampunt: "))
tenur= int(input("Please select Tenure for FD: "))

print ("************")

def calculateamt(t,i):
    interest_amt = (priciple * t * i / 100)
    print ("your Interest rate is: ", i)
    print("Interest amount:", ('%.2f' % interest_amt))
    print("Total amount:", ('%.2f' % (priciple + interest_amt)))

if tenur >=7 and tenur <=45:
    t= tenur/365
    i= 3.75
    calculateamt(t,i)

elif tenur >=46 and tenur <=90:
    t= tenur/365
    i= 4.25
    calculateamt(t,i)
elif tenur >=91 and tenur <=180:
    t= tenur/365
    i= 5
    calculateamt(t,i)
elif tenur >=181 and tenur <=365:
    t= tenur/365
    i= 6.15
    calculateamt(t,i)
else:
    print("Invalid choice")