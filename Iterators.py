# Python Iterators
# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object which
# implements the iterator protocol, which consist of the methods __iter__() and __next__().


# Iterator vs Iterable

# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which
# you can get an iterator from.
# All these objects have an iter() method which is used to get an iterator:

print("************1***********")
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
# print(next(myit)) StopIteration
print("************2***********")
myStr = "banana"
myIt = iter(myStr)
print(next(myIt))
print(next(myIt))
print(next(myIt))
print(next(myIt))
print(next(myIt))
print(next(myIt))
print("************3***********")
# Create an Iterator

# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
# As you have learned in the Python Classes/Objects chapter,
# all classes have a function called __init__(),
# which allows you to do some initializing when the object is being created.
# The __iter__() method acts similar, you can do operations (initializing etc.),
# but must always return the iterator object itself.
# The __next__() method also allows you to do operations, and must return the next item in the sequence.


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        y = self.a
        self.a += 1
        return y


myClass = MyNumbers()
myIter = iter(myClass)
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print("************4***********")
# for item in c
# 1) Let c_item = c.__iter__(), which defines iteration over a Cafe object
# 2) Call c_item.__next__() to get the next value in the iteration process
# 3) Repeat Ste 2 until we get StopIteration


class Cafe:
    def __init__(self, menu):
        self._menu = menu

    def __iter__(self):
        self.i = -1
        return self

    def __next__(self):
        self.i += 1
        if self.i < len(self._menu):
            return self._menu[self.i]
        raise StopIteration


c = Cafe(['Mocha Latte', 'Iced Coffee', 'Tee'])
for item in c:
    print(item)
print("************5***********")
# So usually, we prefer generators instead


class Restaurant:
    def __init__(self, menu):
        self._menu = menu

    def __iter__(self):
        for itemR in self._menu:
            yield itemR


r = Restaurant(['Pizza', 'Burger', 'Ice'])
for item in r:
    print(item)
print("************6***********")
# Ranger


class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step

    # Start
    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration


fr = FRange(0, 2, 0.5)
for x in fr:
    print(x)
print("************7***********")
# loop in loop


class FRange2D:
    def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):
        self.rows = rows
        self.fr = FRange(start, stop, step)

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < self.rows:
            self.value += 1
            return iter(self.fr)
        else:
            raise StopIteration


fr = FRange2D(0, 2, 0.5, 4)
for row in fr:
    for x in row:
        print(x, end=" ")
    print()
