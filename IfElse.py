# Python If ... Else
# Python Conditions and If statements
# Python supports the usual logical conditions from mathematics:
#
#     Equals: a == b
#     Not Equals: a != b
#     Less than: a < b
#     Less than or equal to: a <= b
#     Greater than: a > b
#     Greater than or equal to: a >= b
print("************1***********")
a = 7
b = 14
if b > a:
    print("b is greater than a")
print("************2***********")
# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
c = 77
d = 77
if d > c:
    print("d is greater than a")
elif c == d:
    print("c and d are equal")
print("************3***********")
# The else keyword catches anything which isn't caught by the preceding conditions.
m = 77
h = 55
if h > m:
    print("h is greater than m")
elif m == h:
    print("m and h are equal")
else:
    print("m is greater than h")
print("************4***********")
# Short Hand If
if m > h: print("m is greater than h")
print("************5***********")
# Short Hand If ... Else
print("M") if m > h else print("H")
# This technique is known as Ternary Operators, or Conditional Expressions.
print("************6***********")
print("M") if m > h else print("=") if m == h else print("H")
print("************7***********")
# The and keyword is a logical operator, and is used to combine conditional statements:
t = 77
o = 7
n = 777
if t > o and n > t:
    print("Both conditions are True")
print("************8***********")
# The or keyword is a logical operator, and is used to combine conditional statements:
if t > o or t > n:
    print("At least one of the conditions is True")
print("************9***********")
# The not keyword is a logical operator, and is used to reverse the result of the conditional statement:
if not h > m:
    print("h is NOT greater than m")
print("************10***********")
# You can have if statements inside if statements, this is called nested if statements.
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
print("************11***********")
# if statements cannot be empty,but if you for some reason have an if statement with no content,
# put in the pass statement to avoid getting an error.
if m > h:
    pass
