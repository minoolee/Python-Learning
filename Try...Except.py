# Python Try Except

# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.
print("************1***********")
# Exception Handling
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
# These exceptions can be handled using the try statement:
try:
    print(x)
except:
    print("An exception occurred")
    # #The try block will generate an error, because x is not defined:
print("************2***********")
# Print one message if the try block raises a NameError and another for other errors:
# #The try block will generate a NameError, because x is not defined:
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
print("************3***********")
# Else
# You can use the else keyword to define a block of code to be executed if no errors were raised:
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
print("************4***********")
# Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")
print("************5***********")
# This can be useful to close objects and clean up resources:
try:
    f = open("demofile.txt")
    try:
        f.write("Lorem Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")
print("************28***********")
print("************16***********")
print("************16***********")
print("************16***********")
print("************16***********")
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