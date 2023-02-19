# Loop List
# for
thisList = ["apple", "banana", "cherry"]
for x in thisList:
    print(x)

print("*******1*********")

for x in "banana":
    print(x)

print("*******2*********")

# With the break statement we can stop the loop before it has looped through all the items:
for x in thisList:
    print(x)
    if x == "banana":
        break

print("*******3*********")

# Exit the loop when x is "banana", but this time the break comes before the print:
for x in thisList:
    if x == "banana":
        break
    print(x)

print("********4********")

# With the continue statement we can stop the current iteration of the loop, and continue with the next:
for x in thisList:
    if x == "banana":
        continue
    print(x)

print("*******5*********")

# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(7):
    print(x)

print("*********6*******")

for x in range(3, 5):
    print(x)

print("*********7*******")
for x in range(2, 30, 3):
    print(x)

print("*********8*******")

# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(7):
    print(x)
else:
    print("Finally finished!")

print("*********9*******")
# Note: The else block will NOT be executed if the loop is stopped by a break statement.
for x in range(7):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")

print("*********10******")

# Nested Loops
# A nested loop is a loop inside a loop.
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

print("*********11*******")

# The pass Statement
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

for x in [0, 1, 2]:
    pass