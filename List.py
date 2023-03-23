thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thisList)
print("********1********")
print(thisList[1])
print("*********2*******")
print(thisList[2:5])
print("*********3*******")
print(thisList[:4])
print("*********4*******")
print(thisList[2:])
print("*********5*******")
if "apple" in thisList:
    print("Yes, 'apple' is in the fruits list")
print("********6********")
# Change List Items
thisList[5] = "blackcurrant"
print(thisList)
print("*********7*******")
thisList[1:4] = ["sinaasappel", "watermelon"]
print(thisList)
print("*********8*******")
thisList[1:2] = ["fig", "grapes"]
print(thisList)
print("*********9*******")
thisList.insert(2, "apricot")
print(thisList)
print("********10********")
# Add List Items
thisList.append("lemon")
print(thisList)
print("********11********")
tropical = ["pineapple", "papaya"]
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thisList.extend(tropical)
print(thisList)
print("*******12*********")
# Remove Specified Item
thisList.remove("kiwi")
print(thisList)
print("********13********")
thisList.pop(1)
print(thisList)
print("********14********")
# If you do not specify the index, the pop() method removes the last item.
thisList.pop()
print(thisList)
print("********15********")
# The del keyword also removes the specified index:
del thisList[3]
print(thisList)
print("********16********")
# The del keyword can also delete the list completely.
# del thisList
# print(thisList)
# Clear the List
# The clear() method empties the list.
thisList.clear()
print(thisList)