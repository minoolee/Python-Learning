# Set A set is a collection which is unordered, unchangeable*, and un indexed.
print("************1***********")
thisSet = {"apple", "banana", "cherry"}
print(thisSet)
print("************2***********")
# Sets cannot have two items with the same value.
dontRepeatSet = {"apple", "banana", "cherry", "apple"}
print(dontRepeatSet)
print("************3***********")
# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
mixSet = {"apple", "banana", "cherry", True, 1, 2}
print(mixSet)
print("************4***********")
abcSet = {"apple", "banana", "cherry"}
numberSet = {1, 6, 9, 3, 5}
booleansSet = {True, False, True}
print(abcSet)
print(numberSet)
print(booleansSet)
print("************5***********")
# A set can contain different data types:
containMixSet = {"abc", 7, True, 14, "male", False}
print(containMixSet)
print("************6***********")
# Using the set constructor to make a set
# setConstructor = set(("apple", "banana", "cherry"))
# print(setConstructor)
print("************7***********")
# Loops
loopsSet = ("apple", "banana", "cherry")
for x in loopsSet:
    print(x)
print("************8***********")
# Check if "banana" is present in the set:
print("banana" in loopsSet)
print("************9***********")
#  Items
# Once a set is created, you cannot change its items, but you can add new items.
thisSet.add("orange")
print(thisSet)
print("************10***********")
# To add items from another set into the current set, use the update() method.
tropical = {"pineapple", "mango", "papaya"}
thisSet.update(tropical)
print(thisSet)
print("************11***********")
# Any Iterable
# The object in the update() method does not have to be a set,
# it can be any iterable object (tuples, lists, dictionaries etc.).
thisList = ["kiwi", "mango"]
thisTuple = ("lemon", "cherry")
tropical.update(thisList, thisTuple)
print(tropical)
print("************12***********")
# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.
tropical.remove("mango")
print(tropical)
print("************13***********")
# Note: If the item to remove does not exist, discard() will NOT raise an error.
tropical.discard("kiwi")
print(tropical)
print("************14***********")
# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
x = thisSet.pop()
print(x)
print(thisSet)
print("************15***********")
# The clear() method empties the set:
thisSet.clear()
print(thisSet)
print("************16***********")
# del tropical
# print(tropical)
# You can use the union() method that returns a new set containing all items from both sets,
# or the update() method that inserts all the items from one set into another:
setUni1 = {"a", "b", "c"}
setUni2 = {1, 2, 3}
# setUni3 = setUni1.union(setUni2)
# print(setUni3)
print("************17***********")
# The intersection_update() method will keep only the items that are present in both sets.
kart1 = {"apple", "banana", "cherry"}
kart2 = {"google", "microsoft", "apple"}
kart1.intersection_update(kart2)
print(kart1)
print("************18***********")
# The intersection() method will return a new set, that only contains the items that are present in both sets.
sameKart = kart1.intersection(kart2)
print(sameKart)
print("************19***********")
# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
box1 = {"apple", "banana", "cherry"}
box2 = {"google", "microsoft", "apple"}
box1.symmetric_difference_update(box2)
print(box1)
print("************20***********")
# The symmetric_difference() method will return a new set,
# that contains only the elements that are NOT present in both sets.
box3 = {"apple", "banana", "cherry"}
box4 = {"google", "microsoft", "apple"}
box5 = box3.symmetric_difference(box4)
print(box5)
print("************21***********")
# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
boxSet1 = {"apple", "banana", "cherry", True}
boxSet2 = {"google", 1, "microsoft", "apple", 2}
boxSet3 = boxSet1.symmetric_difference(boxSet2)
print(boxSet3)
print("************22***********")
# Set issubset() Method
# Return True if all items in set x are present in set y:
setBox1 = {"a", "b", "c"}
setBox2 = {"f", "e", "d", "c", "b", "a"}
setBox3 = setBox1.issubset(setBox2)
print(setBox3)
print("************23***********")
# Set difference()
# Return a set that contains the items that only exist in set x, and not in set y:
sB1 = {"apple", "banana", "cherry"}
sB2 = {"google", "microsoft", "apple"}
sB3 = sB1.difference(sB2)
print(sB3)
print("************24***********")
#  Set discard()
# Remove "banana" from the set:
sB3.discard("banana")
print(sB3)
print("************25***********")
# Set isdisjoint()
# Return True if no items in set x is present in set y:
bS1 = {"apple", "banana", "cherry"}
print("************26***********")
print("************27***********")
print("************28***********")
print("************16***********")
print("************16***********")
print("************16***********")
