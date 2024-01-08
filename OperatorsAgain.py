# Operators allow us to programmatically change variable values. There
#   are six types of operators. The six types of oeprators are 
#       -- arithmetic operators
#       -- assignment operators 
#       -- comparison operators 
#       -- logical operators
#       -- identity operators
#       -- membership operators 

# The four discussed in this script are assignment, arithmetic,
#    comparison and logical. 

# Arithmetic operators are the typical math operations: 
#       -- Addition, + 
#       -- Subtraction, - 
#       -- Multiplication, * 
#       -- Division, / 
#       -- Modulus, % (returns the remainder of a divsion)
#       -- Floor division, // (performas division and discards remainder) 
#       -- Exponentiation, **
#
# Below are use cases of arithmetic operators 

# integer variable 
xPosition = 10

# adding one 
forward = xPosition + 1

# subtracting one
backward = xPosition - 1

# printing the remainder of 5 divided by 2
print(5 % 2) # prints 1 because 5 / 2 = 2 with a remainder of 1

# printing the quotient of 5 divided by 2
print(5 // 2) # prints 2 because 5 / 2 = 2 with a remainder of 1

# printing the answer to 5^2
print(5 ** 2) # prints 25 because 5^2 = 25

# We can also combine arithmetic and assignment operators. 
xPosition = xPosition + 1

# The shortform of this is 

xPosition+=1 # prints 12
print(xPosition) 

# Below are examples of shortform of the rest of the arithemetic
#   in short form
xPosition-= 7 # prints 5
print(xPosition) 

xPosition*=20 # prints 100
print(xPosition) 

xPosition/=2 # prints 50.0
print(xPosition)

xPosition%=3 # prints 2 because 50/3 is 16 remainder 2
print(xPosition)

# a good way to confirm modulus asnwers is to satisfies the equation:
#   Quotient × Divisor + Remainder = Dividend. So, in our example 
#   16 x 3 + 2 = 50 

xPosition= 15

xPosition//=3 # prints 5
print(xPosition)

xPosition**=3 # prints 125
print(xPosition)

# The + operators can be used to append strings 
firstName = "Annika "
lastName = "Jorgensen"
print(firstName + lastName)

# We can also use the += operator to stick strings together.
myName = "Annika "
myName += "L. Jorgensen"
print(myName)

# Comparison operators compare two values and return either True of False
#   The operators are:
#       -- Returns true if two values are equal, == 
#       -- Returns true if two values are not equal, != 
#       -- Returns true if x is greater than or equal to y, >= 
#       -- Returns true if x is greatr than y, > 
#       -- Returns true if x is less than or equal to y, <= 
#       -- Returns true if x is less than y, <

# An examples of comparison operators is shown below

#integer variables 
xPosition = 10
endPosition = 10

# True if x variable is equal to y variable 
isAtEnd = xPosition == endPosition #prints true, both variables are 10
print(isAtEnd)

#Comparison and arithmetic operators can be combined 

#True if x variable greater than or equal to y/2 variable
AreHalfway = xPosition >= endPosition / 2
print(AreHalfway) #prints true because 10 is greater than 5

# Identity operators are used to compare the objects, not if they are 
# equal, but if they are actually the same object, with the same memory 
# location. This means that the value and the data type must be the same.
# There are two operators. 
#   -- "is" (the word not with quotes) returns true if both variables 
#           are the same object
#   -- "is not" (the words not with quotes) returns if both variables
#           are NOT the same object 
# Consider the following:

# creating variables 
a = 1
b = 1.0 

# will print true because both variables are 1
d= a == b 

# will print false because a is an interger and b is a float
c = a is b

# will print true because a and b are different data types
e = a is not b
print(c)

# Membership operators in Python test a sequence, such as a string, a list, 
#   or a tuple, for membership. They check whether a sequence appears in 
#   an object or not. There are two operators 
#       -- "in", (the word not with quotes) will return true if the 
#               specificied value/literal is present in the sequence
#       -- not in,(the words not with quotes) will return true if the 
#               specified value/literal is NOT present in the sequence
# Consider the following examples:

#creating string variables 
a = "abcdefg"
b = "Annika"

# checking if variable b is in a
c = b not in a 
print(c) #prints true because Annika is not in abcdefg

d = b in a 
print(d) #prints false  because Annika is not in abcdefg

# There are three logical operators in Python The operators are the word
# not with quotes 
#       -- "and" will return true if both booleans are true
#       -- "or" will return true if at least one of the booleans is true
#       -- "not" negates first boolean or turns positive into negative 
#          vice versa
# Consider the following examples 

# creating boolean variable 
isAtEnd = True

# negating boolean variable
notAtEnd = not isAtEnd #prints false

# integer variable
score = 9

# score must be greater than or equal to 10 AND isAtEnd must be true
isGameOver = score >=10 and isAtEnd #prints False because score is 9
print(isGameOver)

# score must be greater than or equal to 10 OR isAtEnd must be true
isGameOver = score >=10 or isAtEnd #prints true because isAtEnd is true
print(isGameOver)

