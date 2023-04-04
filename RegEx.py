# Python RegEx
# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.

# RegEx Module
# Python has a built-in package called re, which can be used to work with Regular Expressions.
# Import the re module:
print("************1***********")
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("Yes! We have a mach!")
else:
    print("No match")
print("************2***********")
# RegEx Functions

# The re module offers a set of functions that allows us to search a string for a match:
# Function 	Description
# findall 	Returns a list containing all matches
# search 	Returns a Match object if there is a match anywhere in the string
# split 	Returns a list where the string has been split at each match
# sub 	    Replaces one or many matches with a string
print("************3***********")
# Metacharacters

# Metacharacters are characters with a special meaning:

# Character  Description 	                                    Example
# [] 	     A set of characters 	                             "[a-m]"
# \ 	     Signals a special sequence
#            (can also be used to escape special characters) 	 "\d"
# . 	     Any character (except newline character) 	         "he..o"
# ^ 	     Starts with 	                                     "^hello"
# $ 	     Ends with 	                                         "planet$"
# * 	     Zero or more occurrences 	                         "he.*o"
# + 	     One or more occurrences 	                         "he.+o"
# ? 	     Zero or one occurrences 	                         "he.?o"
# {} 	     Exactly the specified number of occurrences 	     "he.{2}o"
# | 	     Either or                                        	 "falls|stays"
# () 	     Capture and group


print("************4***********")
someTest = "That will be 59 dollars"

#Find all digit characters:
find = re.findall("\d", someTest)
print(find)
print("************5***********")
# Special Sequences

# A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

# Character  Description 	                                                Example
# \A 	     Returns a match if the specified characters are at the
#            beginning of the string 	                                    "\AThe"

# \b 	     Returns a match where the specified characters are at
#            the beginning or at the end of a word(the "r" in the           r"\bain"
#            beginning is making sure that the string is being treated      r"ain\b"
#            as a "raw string")
#
# \B 	     Returns a match where the specified characters are present,
#            but NOT at the beginning (or at the end) of a word
#            (the "r" in the beginning is making sure that the string is    r"\Bain"
#            being treated as a "raw string") 	                            r"ain\B"
#
# \d 	     Returns a match where the string contains digits
#            (numbers from 0-9) 	                                        "\d"

# \D 	     Returns a match where the string DOES NOT contain digits 	    "\D"

# \s 	     Returns a match where the string contains
#            a white space character 	                                    "\s"

# \S 	     Returns a match where the string DOES NOT contain
#            a white space character 	                                     "\S"

# \w 	     Returns a match where the string contains any word
#            characters (characters from a to Z, digits from 0-9,
#            and the underscore _ character) 	                             "\w"

# \W 	    Returns a match where the string DOES NOT contain any
#           word characters 	                                             "\W"

# \Z 	    Returns a match if the specified characters are at the
#           end of the string 	                                            "Spain\Z"
print("************6***********")
# Sets

# A set is a set of characters inside a pair of square brackets [] with a special meaning:

# Set 	       Description
# [arn] 	   Returns a match where one of the specified characters (a, r, or n) is present
# [a-n] 	   Returns a match for any lower case character, alphabetically between a and n
# [^arn] 	   Returns a match for any character EXCEPT a, r, and n
# [0123] 	   Returns a match where any of the specified digits (0, 1, 2, or 3) are present
# [0-9] 	   Returns a match for any digit between 0 and 9
# [0-5][0-9]   Returns a match for any two-digit numbers from 00 and 59
# [a-zA-Z]     Returns a match for any character alphabetically between a and z, lower case OR upper case
# [+] 	       In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for
#              any + character in the string
print("************7***********")
# The findall() Function

# The findall() function returns a list containing all matches.
aiFin = re.findall("ai", txt)
print(aiFin)
print("************8***********")
# The search() Function
# The search() function searches the string for a match, and returns a Match object if there is a match.
# If there is more than one match, only the first occurrence of the match will be returned:
searchFunc = re.search("\s", txt)
print("The first white-space character is located in position:", searchFunc.start())
# If no matches are found, the value None is returned:
print("************9***********")
# The split() Function
# The split() function returns a list where the string has been split at each match:
splitFunc = re.split("\s", txt)
print(splitFunc)
print("************10***********")
#  You can control the number of occurrences by specifying the maxsplit parameter:
maxSplit = re.split("\s", txt, 1)
print(maxSplit)
print("************11***********")
# The sub() Function
# The sub() function replaces the matches with the text of your choice:
replaceFunc = re.sub("\s", "14", txt)
print(replaceFunc)
print("************12***********")
# You can control the number of replacements by specifying the count parameter:
countReplace = re.sub("\s", "7", txt, 2)
print(countReplace)
print("************13***********")
# The Match object has properties and methods used to retrieve information about the search, and the result:

# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match
print("************14***********")
groupFunc = re.search(r"\bS\w+", txt)
print(groupFunc.group())
