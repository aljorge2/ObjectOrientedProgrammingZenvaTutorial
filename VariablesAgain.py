#import turtle
from turtle import *

# four types of variables integer float string boolean 

# integers and floats are numerical type. integers are whole numbers 
# floats are not

# integer variable 
xPosition = 10

# print variable 
print(xPosition)

# reassigning variable 
xPosition = 15
print(xPosition)

# float 
pi = 3.14 
print(pi)

# reassigning float 
pi = 3.14159
print(pi)

# representing a whole number as a float 
xPosition = 15.0
print(xPosition)

# type function gives you variable type 
xPositionType = type(xPosition)
print(xPositionType)

# boolean variables represent True or False values. These variables 
#   can only be in one state. Consider the following example.

isGameOver = False
isGameOver = True

# if "isGameOver" is true and we wanted the variable to be of integer type
#    we could do the following 

isGameOver = 1

# Strings are any text data. The text can be housed between "" or '' the
#   quotes must be the same on both sides. The following example shows two
#   equivalent variables 

name = "Annika"
name = 'Annika'

# numbers and boolean values can also become strings inside quotations
isGameOverText = "False"
ageStringType = "27"

# Since strings can house other data as I can insert variables into
#   strings as shown below

age = 22
namePlusAge = "Annika is {}".format(age)

# the open brackets tell the compiler to expect a variable value so we 
#   must give a value (in this example variable "age"). When printing
#   the variable the open brackets are filled with the variable's value

#print variable
print(namePlusAge)

# the following examples show what the other variable types look like in 
#   string format

#showing boolean as string
isGameOver = False
Question = "Is the game over? {}".format(isGameOver)
print(Question)

#showing float as string
pi= 3.1415
Question = "What is Pi? {}".format(pi)
print(pi)