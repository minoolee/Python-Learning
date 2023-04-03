# Python JSON
# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.
# Python has a built-in package called json, which can be used to work with JSON data.
print("************1***********")
# If you have a JSON string, you can parse it by using the json.loads() method.
import json

# some JSON:
x = '{"name": "Jack", "age": 30, "city": "New York"}'

# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])
print("************2***********")
# Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
# a Python object (dict):
objctDict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
# convert into JSON:
convertJson = json.dumps(objctDict)
print(convertJson)
print("************3***********")
# You can convert Python objects of the following types, into JSON strings:
#
#     dict
#     list
#     tuple
#     string
#     int
#     float
#     True
#     False
#     None
print("************4***********")
print(json.dumps(["apple", "bananas"]))
print(json.dumps(14.7))
print(json.dumps(True))
print("************5***********")
# When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:
# Python 	JSON
# dict 	    Object
# list 	    Array
# tuple 	Array
# str 	    String
# int 	    Number
# float 	Number
# True 	    true
# False 	false
# None   	null
print("************6***********")
# Format the Result
# The json.dumps() method has parameters to make it easier to read the result:
# Use the indent parameter to define the numbers of indents:
# Use the separators parameter to change the default separator:
# Order the Result
# Use the sort_keys parameter to specify if the result should be sorted or not:
person = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann", "Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
# use four indents to make it easier to read the result:
# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
# sort the result alphabetically by keys:
print(json.dumps(person, indent=4, separators=(". ", " = "), sort_keys=True))
