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
print(thisDict)
print("************11***********")
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisDict.popitem()
print(thisDict)
print("************12***********")
# The del keyword removes the item with the specified key name:
del thisDict["year"]
print(thisDict)
print("************13***********")
# The clear() method empties the dictionary:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)
print("************14***********")
loopDic = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in loopDic:
    print(x)
print("************15***********")
for x in loopDic:
    print(loopDic[x])
print("************16***********")
# ou can also use the values() method to return values of a dictionary:
for x in loopDic.values():
    print(x)
print("************17***********")
# You can use the keys() method to return the keys of a dictionary:
for x in loopDic.keys():
    print(x)
print("************18***********")
# Loop through both keys and values, by using the items() method:
for x, y in loopDic.items():
    print(x, y)
print("************19***********")
# Make a copy of a dictionary with the copy() method:
copyDic = loopDic.copy()
print(copyDic)
print("************20***********")
# Make a copy of a dictionary with the dict() function:
dictDic = dict(loopDic)
print(dictDic)
print("************21***********")
# Nested Dictionaries
child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
  "name": "Linus",
  "year": 2011
}
myFamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myFamily)
print("************22***********")
print(myFamily["child2"]["name"])
# Create a dictionary with 3 keys, all with the value 0:
x = ('key1', 'key2', 'key3')
y = 0
newDic = dict.fromkeys(x, y)
print(newDic)
