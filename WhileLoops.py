# Python While Loops

# Python has two primitive loop commands:
#     while loops
#     for loops
print("************1***********")
# With the while loop we can execute a set of statements as long as a condition is true.
i = 1
while i < 7:
    print(i)
    i += 1
print("************2***********")
# With the break statement we can stop the loop even if the while condition is true:
j = 2
while j < 7:
    print(j)
    if (j == 5):
        break
    j += 1
print("************3***********")
# With the continue statement we can stop the current iteration, and continue with the next:
g = 0
while g < 7:
    g += 1
    if g == 3:
        continue
    print(g)
print("************4***********")
# With the else statement we can run a block of code once when the condition no longer is true:
s = 1
while s < 7:
    print(s)
    s += 2
else:
    print("s is no longer less than 7")
