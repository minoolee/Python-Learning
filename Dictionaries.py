# Python Dictionaries
print("************1***********")
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1994
}
print(thisDict)
print("************2***********")
#  key:value
print(thisDict["brand"])
print("************3***********")
# There is also a method called get() that will give you the same result:
g = thisDict.get("model")
print(g)
print("************4***********")
# The keys() method will return a list of all the keys in the dictionary.
k = thisDict.keys()
print(k)
print("************5***********")
# Add a new itthe original
thisDict["color"] = "White"
print(thisDict)
print("************6***********")
# The values() method will return a list of all the values in the dictionary.
v = thisDict.values()
print(v)
print("************7***********")
# The items() method will return each item in a dictionary, as tuples in a list.
itm = thisDict.items()
print(itm)
print("************8***********")
# Loops
if "model" in thisDict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
print("************9***********")
# The update() method will update the dictionary with the items from the given argument.
thisDict.update({"year": 2020})
print(thisDict)
print("************10***********")
# Removing Items
thisDict.pop("model")
print("************27***********")
print("************28***********")
print("************16***********")
print("************16***********")
print("************16***********")
print("************27***********")
print("************28***********")
print("************16***********")
print("************16***********")
print("************16***********")
print("************27***********")
print("************28***********")
print("************16***********")
print("************16***********")
print("************16***********")
print("************27***********")
print("************28***********")
print("************16***********")
print("************16***********")
print("************16***********")