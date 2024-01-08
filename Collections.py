# Collections offer us the ability to store multiple values within a 
#   single variable. There are three types that we will study here: lists,
#   tuples, and dictionaries.

# Lists store values based on index or position. The values can be
#   accessed all at once by name, one at a time via indexing, or several
#   several at a time via slicing. Lists can contain multiple data
#   types. Consider the following list.

# list of integers
enemyPositions = [5, 10, 15]

# reassigned list of integers
enemyPositions = [5, 10, 15, 20]

# print list
print(enemyPositions)

# Lists can contain as many elements (meaning values) as we want. Lists
#   can also be empty. 

# getting length of list
length = len(enemyPositions)
print(length) # prints 4 because there are four elements

# Indexing is a way to access elements in the list. Indexing in python
#    is 0-based meaning that the first element is at index of 0, second
#    element is at 1, and so on.

# calling last element in list enemyPositions
last = enemyPositions[3]
print(last)

# We can also change values based on indexing 

#changing first element to six
enemyPositions[0] = 6
print(enemyPositions)

# We can access multiple elements via the slicing operator, [x:y:z], where
#   where x is the lower bound and y is an upper bound, and z is the
#   step. All arguments do not have to be included. Upper bounds are not
#   included in the slice. Consider the examples

# extracting first two elements 
firstTwo = enemyPositions[0:2]
print(firstTwo)

#extracting elements 0,3
three = enemyPositions[0:6:2]
print(three)

# There are several operations we can perform on lists that help us 
#   manipulate them or retrieve properties. Examples that are covered in
#   this script are append, insert, del, and remove. 

# The append function allows you to add and element to the end of a list

# adding 25 to end 
enemyPositions.append(25)
print(enemyPositions)

# The insert function inserts an element at a specific index

# inserting 9 at index one and shifting the other values
enemyPositions.insert(1,9)
print(enemyPositions)

# The remove function removes the first occurance of an element if it
#   exists and shifts the other elements accordingly.  

# removing the first occurance of integer 6
enemyPositions.remove(6)
print(enemyPositions)

enemyPositions.append(6)
enemyPositions.insert(2,6)
print(enemyPositions)

# removing 6 at index 2, but not at index 6
enemyPositions.remove(6)
print(enemyPositions)

# The del function removes elements at a specific index

# removing element at index 2
del(enemyPositions[2])
print(enemyPositions) 

# Tuples are another type of collection that act very similiar to a list
#   however we cannot change, add, or remove elements. Tuples are used
#   for storing values only. Tuples can have elements of all the same
#   data type or multiple data types. 

# Consider the following examples

# tuple with two elements 
highScore = ("Annika", 250)

# tuples can be reassigned
highScore = ("Dovah-Kiin", 265)

# elements can be fetched by index
print(highScore[0], "is a winner!")

# we can see the length of a tuple and check if values exist

#length of tuple
length = len(highScore)
print("The length of highScore is",length)

#checking if Holly exists in variable
doesContain = "Annika" in highScore
print(" Annika exists in highScore", doesContain)

# This logic applies to strings. Consider the following examples

#creating string variable 
name = "Annika"

# calling first element
first = name[0]
print(first)

# calling first two elements 
firstTwo = name[0:2]
print(firstTwo)

# checking if Ann exists in variable 
isIn = "Ann" in name
print("Ann exists in name.", isIn)

# length of name
length = len(name)
print(length)

# Dictionaries attach their values to keys rather than storing them at 
#   specific positions or indexes. The benefit of using a dictionary is 
#   that if we need to access a specific element, we don’t need to know 
#   its position (as we would have to if we stored it in a list or tuple);
#   we only need the key under which we stored it. We can set up a 
#   dictionary like this:

actions = {"r":1, "l":-1}
print(actions)

# There are two key-value pairs where the keys are strings and the values 
#   are integers. The keys and values can be whatever types you want but 
#   string-int makes sense for us. To access a value, we need the key and 
#   do so in two ways:

# prints 1 
right = actions["r"]
print(right)

# prints 1
right = actions.get("r")
print(right)

# Both ways store 1 because the value at the key “r” is 1. The difference
#   is that “.get()” is safer and will return “None” if the key does not 
#   exist whereas [value] will just crash the program if the key does not 
#   exist.

# We can change values via their key and if the key doesn’t exist, the 
#   dictionary inserts a new key and stores the value. For example:

# changing value to 2 at key r
actions["r"] = 2

# prints 2 because value has been changed
right = actions.get("r")
print(right)

# creating key u and storing value 1 at key
actions["u"] = 1

# storing value at key u
right = actions.get("u") # prints 1
print(right)

# There are dictionary specific functions that we can access in the same 
#   way as lists and tuples. For example, we can get a list of (key, value)
#   tuples, a list of just the values, or a list of just the keys like this:

# getting list of key value tuples 
items = actions.items()
print(items)

# getting list of values 
values = actions.values()
print(values)

# getting list of keys
keys = actions.keys()
print(keys)

# We can remove a key-value pair by doing one of these two:

del(actions["u"])
actions.pop("r")

#getting list of key value tuples
items = actions.items()
print(items)

# We can also check to see if a key (and therefore some value) exists like
# this:

#checking if l is in dictionary 
isIn = "l" in actions
print(isIn)