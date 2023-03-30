# Python Modules
# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.
import mymodule
print("************1***********")
# Note: When using a function from a module, use the syntax: module_name.function_name.
mymodule.greeting("Jack")
print("************2***********")
a = mymodule.person1["age"]
print(a)
print("************3***********")
# Naming a Module
# You can name the module file whatever you like, but it must have the file extension .py

# Re-naming a Module
# You can create an alias when you import a module, by using the as keyword:
import neumodule as nm
c = nm.car["year"]
print(c)
print("************4***********")
# Built-in Modules
# There are several built-in modules in Python, which you can import whenever you like.
import  platform

x = platform.system()
print(x)
print("************5***********")
# Using the dir() Function
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
# import platform
y = dir(platform)
print(y)
