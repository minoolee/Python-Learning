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


doubleArgFunction(firstName="Tim", lastName="Crus")
print("************6***********")
# You can also send arguments with the key = value syntax.

print("************16***********")
print("************16***********")
print("************16***********")
print("************16***********")
print("************27***********")
print("************28***********")
print("************16***********")
print("************16***********")
print("************16***********")
print("************16***********")
print("************16***********")
print("************27***********")
print("************28***********")
print("************16***********")
print("************16***********")
print("************16***********")
print("************16***********")
print("************16***********")
print("************16***********")
print("************27***********")
print("************28***********")
print("************16***********")
print("************16***********")
print("************16***********")