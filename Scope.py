# Local Scope
# A variable created inside a function belongs to the local scope of that function,
# and can only be used inside that function.

print("************1***********")
def myFunc():
    x = 700
    print(x)

myFunc()
print("************2***********")
# Function Inside Function

def funcInsidefunc():
    fFunc = 500
    def insideFunc():
        print(fFunc)
    insideFunc()

funcInsidefunc()
print("************3***********")
# Global Scope
m = 700
def minooFunc():
    print(m)

minooFunc()
print(m)
print("************4***********")
# Naming Variables
# If you operate with the same variable name inside and outside of a function,
# Python will treat them as two separate variables,
# one available in the global scope (outside the function) and one available in the local scope (inside the function):
h = 500

def hamzahFunc():
    h = 420
    print(h)

hamzahFunc()
print(h)
print("************5***********")
# Global Keyword
# The global keyword makes the variable global.
def globalKeywordFunc():
    global g
    g = 700
globalKeywordFunc()
print(g)
print("************6***********")
# Also, use the global keyword if you want to make a change to a global variable inside a function.
y = 600
def changeGlobalFunc():
    global y
    y = 300
changeGlobalFunc()
print(y)
