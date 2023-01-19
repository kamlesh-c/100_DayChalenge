# day 19
# Break and continue statement
for i in range(5):
    print ("If i = 8  Break ")
    print ("Print is =", i*2)
    if (i == 8):
        break

print("out of loop")

for i in range (10):
    print("This is i", i)
    if (i == 5 ):
        print("in if statement  ")
        continue
    print("after if statement")
print("after for loop")