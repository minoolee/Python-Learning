# Python Tuples
# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
print("******1**********")
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print("******2**********")
print(thistuple[1])
print("******3**********")
print(len(thistuple))
print("******4**********")
print(type(thistuple))
print("******5**********")
tupleNumbers = (1, 5, 7, 14)
print(tupleNumbers)
print("******6**********")
tupleBoolean = (True, False, True, False)
print(tupleBoolean)
print("******7**********")
tupleMix = ("abc", 7, True)
print(tupleMix)
print("******8**********")
# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.
constructorTuple = tuple(("red", "green", "blue")) # note the double round-brackets
print(constructorTuple)
# Access Tuple Items
print("******9**********")
print(thistuple[1])
print("******10**********")
extraTuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(extraTuple[2:5])
print("******11**********")
print(extraTuple[:4])
print("******12**********")
print(extraTuple[2:])
print("******13**********")
if "apple" in extraTuple:
    print("Yes, 'apple' is in the fruits tuple")
print("******14**********")
# Update Tuples
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# Change Tuple Values
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
print("******15**********")
# Add Items
startTuple = ("apple", "banana", "cherry")
y = list(startTuple)
y.append("orange")
startTuple = tuple(y)
print(startTuple)
print("********16******")
# Add tuple to a tuple.
firstTuple = ("apple", "banana", "cherry")
secondTuple = ("mango", "orange")
firstTuple += secondTuple
print(firstTuple)
print("********17******")
# Unpack Tuple
fruit = ("apple", "banana", "cherry")
(green, yellow, red) = fruit
print(green)
print(yellow)
print(red)
print("*********18****")
extraFruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(first, second, *rest) = extraFruits
print(first)
print(second)
print(rest)
print("*********19****")
# Loop Through a Tuple
loopsTuple = ("apple", "banana", "cherry")
for x in loopsTuple:
    print(x)
print("*********20*******")
for i in range(len(loopsTuple)):
    print(loopsTuple[i])
print("*********21****")
doubleTuple = fruit * 2
print(doubleTuple)
print("*********22****")