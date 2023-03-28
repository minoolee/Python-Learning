# Python Inheritance

# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

    # Use the Person class to create an object, and then execute the printname method:


person1 = Person("Tom", "Krus")
person1.printname()
print("************1***********")
#  Create a Child Class


class Student(Person):
    pass


student1 = Student("Mike", "Jordon")
student1.printname()
print("************2***********")
# Add the __init__() Function
class Teacher(Person):
    def __init__(self, fname, lname):
     Person.__init__(self, fname, lname)
teacher =Teacher("Same", "Simpson")
teacher.printname()
print("************3***********")
# Use the super() Function
# Python also has a super() function that will make the child class inherit
# all the methods and properties from its parent:
class Baby(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

baby = Baby("Dimedime", "Paq")
baby.printname()
print("************4***********")


# Add Properties
class Charsi(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2022


charsi = Charsi("Hamzah", "Chars")
print(charsi.graduationyear)
print("************5***********")
# Add Methods

class AddMethods(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

moreInfo = AddMethods("Milisa", "Olson", 2022)
moreInfo.welcome()
