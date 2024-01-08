# functions are contained blocks of code that run only when we choose.
#   They remain dormant until we call upon them. This allows us to hide
#   aways code so that it is run only when we wat it to run. This also 
#   allows us to execute the same functionality at potentially many 
#   different points in the program without having to rewrite. Consider
#   the following. 

# creating integer variable 
position = 0

# def starts function definition. movePlayer is function name
def move_player(): # empty parantheses means function takes no inputs
  
  # getting access to position variable
  global position

  # increasing position by 1
  position += 1
  print(position)

# calling movePlayer function
move_player()

# note that we can only access the variable within that function as 
#   variables only exist within the function/control flow/class in which 
#   they’re declared.

# functions can take values in via parameters which we place within the 
#   ( ) and can then use like regular variables. Consider the following

# creating integer variable 
position = 0

# defining function with 1 parameter
def move_player(byAmount):
  
  # calling global variable
  global position

  # increasing global variable by parameter
  position += byAmount

  # printing global variable
  print(position)

# now when we call the function, it needs an input value for byAmount 

# calling function
move_player(5)

# we can pass in as many parameters we want and they can be of whatever 
#   type we want. However, we have to pass in at least one value for each 
#   parameter when calling a function.

# global variables should be avoided if possible.

# creating integer variable
position = 0

# defining function with 2 parameters
def move_player(position, byAmount):
  
  # increasing parameter 1 by parameter 2
  position += byAmount

  # printing parameter 1
  print(position)

# calling function
move_player(position, 5)

# printing position
print(position)

# Notice that the variable position's value is still 0. That is because 
#   the value is just copied when passed in as a parameter (and we are 
#   not using the global variable position). To fix this, we can use 
#   return values. Return values act as output from a function and can be 
#   captured when calling a function like this:

# creating integer variable
position = 0

# defining function with 2 parameters
def move_player(position, by_amount):
  
  # increasing parameter 1 by parameter 2
  position += by_amount

  #returning parameter 1
  return position

# setting variable equal to function
position = move_player(position, 5)

# printing position
print(position)

# We can also use return statements to break out of functions prematurely 
#   just like with break statements. If a function does not need to output
#   a value but we want to break out of it prematurely, simply use a 
#   “return” with no value beside it.
