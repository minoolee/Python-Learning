b = "Hello , World"
print(b[2:5])
print("********1********")
print(b[:5])
print("********2********")
print(b[-3:-1])
print("********3********")
print(b.upper())
print("********4********")
print(b.lower())
print("*******5*********")
# The strip() method removes any whitespace from the beginning or the end:
print(b.strip())
print("********6********")
print(b.replace("H", "K"))
print("*******7*********")
print(b.split(","))
print("*******8*********")
quantity = 3
itemno = 567
price = 48.87
myorders = "I want {} pieces of item {} for {} dollars."
print(myorders.format(quantity, itemno, price))
print("********9********")
myorders1 = "I want {2} pieces of item {0} for {1} dollars."
print(myorders1.format(quantity, itemno, price))
print("********10********")
txt = "hello, and welcome to 7 my world?"
print(txt.capitalize())
print("*******11*********")
txt1 = "Hello, and welcome to my world."
print(txt1.casefold())
print("*******12*********")
cen = "banana"
print(cen.center(56))
print("*******13*********")
print(cen.center(20, "a"))
print("********14********")
p = txt.count("welcome")
print(p)
print("*******15*********")
print(txt.endswith("?"))
print("*******16*********")
print(txt1.endswith("my world."))
print("********17********")
print(txt.endswith("world.", 4, 8))
print("********18********")
expand = "H\te\tl\tl\to"
print(expand.expandtabs(3))
print("********19********")
print(txt.find("my"))
print("*******20*********")
ptxt = "For only {pop:.2f} dollars!"
print(ptxt.format(pop=49))
print("********21********")
print(txt.index("welcome"))
print("*******22*********")
# string.index(value, start, end)
print(txt.index("n", 8, 10))
print("******23**********")
# Check if all the characters in the text is alphanumeric:
alnum = "Company7"
print(alnum.isalnum())
print("*******24*********")
print(txt.isalnum())
print("*******25*********")
print(cen.isalpha())
print("*******26*********")
age = "54"
print(age.isdigit())
print("*******27*********")
indentif = "C_R7"
print(indentif.isidentifier())
print("********28********")
lo = "hello"
print(lo.islower())
print("*******29*********")
space = "   "
print(space.isspace())
print("*******30*********")
# Check if each word start with an upper case letter:
title = "Hello, And Welcome To My World!"
print(title.istitle())
print("*******31*********")
# Check if all the characters in the text are in upper case:
checkUpper = "HELLO WORLD!"
print(checkUpper.isupper())
print("********32********")
myTeam = ("Hamzah", "DimDim", "Minoo")
print("#".join(myTeam))
print("********33********")
myObj = {"name": "Tom", "country": "Germany"}
mySeparator = "Love"
res = mySeparator.join(myObj.values())
print(res)
print("*******34*********")
print(checkUpper.ljust(30), "is my fierst")
print("********35********")
trans = lo.maketrans("h", "K")
print(lo.translate(trans))
print("*******36*********")
port = "I could eat bananas all day"
print(port.partition("apples"))