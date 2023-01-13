#Day 13
#String Methods
#String are imutable
a= "!!!K1amlesH!!!!"
print ("Orignal string =",a)
#Upper case
print ("Upper case =",a.upper())
print("Lower case=",a.lower())
print("Relling Strip(Ending char can remove",a.rstrip("!"))
print("all occrance of Char will replace with new",a.replace("a","@"))
print ("Split will splut change",a.split("a"))
para = "IntroductIon1 of python and 100 day of challange and 100 day will be finish in 100 day"
print ("***\n", para)
print("First letter will be capitalise=",para.capitalize())
print("length of pra=", para)
print("move in center\n", para.center(50))
print("Count occerance of char n in para", para.count("n"))
print("Check wthere string end with decide charater", para.endswith("!"))
print("Find char and retur first occorunce .find", para.find("day"))
str="ThisFo"
print("Check alfa numeric .isalnum", str.isalnum())
print("check lower or not.islower", str.islower())
print ("check whitre spces .isspace", str.isspace())
para1 = "This Is One"
print("check title or not istitle", para1.istitle())
print("swape case=",para1.swapcase())