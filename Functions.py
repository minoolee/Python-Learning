# Python Functions
# In Python a function is defined using the def keyword:
print("************1***********")


def my_function():
    print("Hello from a function")


my_function()
print("************2***********")


# Arguments
def myFunction(name):
    print(name + " Refsnes")


myFunction("Emil")
myFunction("Jack")
print("************3***********")


def moreArgs(firstName, lastName):
    print(firstName + " " + lastName)


moreArgs("Samy", "Smite")
moreArgs("Jacky", "Chan")
print("************4***********")
# If you do not know how many arguments that will be passed into your function,
# add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
def tupleFunction(*kinds):
    print("The youngest child is " + kinds[2])


tupleFunction("Tom", "Tobias", "Linus")

print("************5***********")
# If you do not know how many keyword arguments that will be passed into your function,
# add two asterisk: ** before the parameter name in the function definition.


def doubleArgFunction(**kid):
    print("His last name is " + kid["lastName"])
    print("his age is " + kid["state"])


doubleArgFunction(firstName="Tim", lastName="Crus", state="56")
print("************6***********")
# You can also send arguments with the key = value syntax.

print("************6***********")
# Default Parameter Value


def defaultFunction(country = "Norway"):
    print("I am from " + country)


defaultFunction("Sweden")
defaultFunction()
print("************7***********")
# Passing a List as an Argument

def listArgument(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

listArgument(fruits)
print("************8***********")
# Return Values

def returnFunction(x):
    return 5 * x


print(returnFunction(3))
print("************9***********")
# The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content,
# put in the pass statement to avoid getting an error.

def passFunction():
    pass


