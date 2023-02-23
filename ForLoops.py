# Python For Loops
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages,
# and works more like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
print("************1***********")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
# The for loop does not require an indexing variable to set beforehand.
print("************2***********")
for x in "banana":
    print(x)
print("************3***********")
# With the break statement we can stop the loop before it has looped through all the items:
for x in fruits:
    print(x)
    if x == "banana":
        break
print("************4***********")
for x in fruits:
    if x == "banana":
        break
    print(x)
print("************5***********")
# With the continue statement we can stop the current iteration of the loop, and continue with the next:
for x in fruits:
    if x == "banana":
        continue
    print(x)
print("************6***********")
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers,
# starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(7):
    print(x)
print("************7***********")
for x in range(3, 7):
    print(x)
print("************8***********")
for x in range(3, 30, 7):
    print(x)
print("************8***********")
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(7):
    print(x)
else:
    print("Finally finished!")
print("************9***********")
# Note: The else block will NOT be executed if the loop is stopped by a break statement.
for x in range(7):
    if x == 5:
        break
    print(x)
else:
    print("Finally finished!")
print("************10***********")
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":
adj = ["red", "big", "tasty"]
for x in adj:
    for y in fruits:
        print(x, y)
