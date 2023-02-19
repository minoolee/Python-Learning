# Set
# A set is a collection which is unordered, unchangeable*, and unindexed.
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
setConstructor = set(("apple", "banana", "cherry"))
print(setConstructor)
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
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
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