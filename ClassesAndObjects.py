# Python Classes and Objects
# A Class is like an object constructor, or a "blueprint" for creating objects.

print("************1***********")
# Create a Class
class MyClass:
    m = 7
m1 = MyClass()
print(m1.m)
print("************2***********")
# The __init__() Function
# All classes have a function called __init__(), which is always executed when the class is being initiated.
#
# Use the __init__() function to assign values to object properties,
# or other operations that are necessary to do when the object is being created:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("Jack", 7)
print(person1.name)
print(person1.age)
print("************3***********")
# The __str__() Function
# The __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned:

class Charsi:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"


charsi1 = Charsi('hamzah', 35)
print(charsi1)
print("************4***********")
# Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the object.
class Playear:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def callPlayearFun(self):
      print("You are the next " + self.name)


playear1 = Playear("Ronaldo", 30)
playear1.callPlayearFun()
print("************5***********")
# The self Parameter
# The self parameter is a reference to the current instance of the class,
# and is used to access variables that belongs to the class.
# It does not have to be named self ,you can call it whatever you like,
# but it has to be the first parameter of any function in the class:
class Selfmade:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myFunc(famouse):
            print("Hello my name is " + famouse.name)

self1 = Selfmade("Jack", 32)
self1.myFunc()
print("************6***********")
self1.project = "charsi"
print(self1.project)
print("************6***********")
# The pass Statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content,
# put in the pass statement to avoid getting an error.
class Empty:
    pass


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