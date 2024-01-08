# objects are code entities with state and behavior. The state is 
#   represented by variables that make up various properties or 
#   attributes. This allows us to create complex data types with many 
#   values attached to them. The behavior is managed by functions that 
#   the object can run; typically, these functions modify the state in 
#   some way.

# classes act as blueprints for objects, specifying what variables an 
#   object should use to make up its state and also defining any functions
#   the object might want to run. Classes also use special initializer 
#   functions to create instances and set up the initial state of the 
#   object. Consider the following class: 

# This of objects Proper nouns and classes as nouns. Everything is an 
#   objects but you make classes to contains objects 

# creating class with three properties 
class GameObject:
  
  # defining function that takes in parameters for the initial values 
  def __init__(self, name, x_pos, y_pos): # two underscores b4 & after init
    
    # self accesses variable/function that belongs to GameObject object
    self.name = name 
    self.x_pos = x_pos
    self.y_pos = y_pos

    # creating new function that changes position 
  def move(self, by_x_amount, by_y_amount):
    
    # adding numbers to xPos
    self.x_pos += by_x_amount

    # adding numbers to xPos 
    self.y_pos += by_y_amount

# when calling this function nothing seems to happen because we are 
#   setting the initial state behavior
game_object = GameObject("Enemy", 1, 2)
print(game_object)
# Now the gameObject variable is of type GAMEOBJECT and contains the three
#   variables name, x_pos, and y_pos. We can access them with . syntax and
#   even set them like this:

#setting variable equal to first property from class
name = game_object.name
print(name)

#changing first property from class
game_object.name = "Enemy 1"
name = game_object.name
print(name)

# changing intial states from class
other_game_object = GameObject("Player", 2, 0)
print(other_game_object.name)

# changing inital states from class 
game_object = GameObject("Enemy", 1, 2)

#vchanging x and y position of class 
game_object.move(5, 10)

# printing x position 
print(game_object.x_pos) #should print 6 because intial 1 + 5 move
print(game_object.y_pos) #should print 12 because initial 2 + 10 move 

# objects are reference types which means that upon assignment, we 
#   maintain a reference to a specific object rather than just copying 
#   some values. So far, all of the variables (Integers, Floats, Booleans,
#   Strings, Lists, Dictionaries, etc.) are all value types meaning their 
#   values are copied during assignment. Take this example: 

# creating variable 
one_int = 5

# creating variable 
another_int = one_int

# Above both variables equal 5 and if I change one variable the other is
#   unaffected 

another_int = 10
print(another_int)
print(one_int)

# This is because these are both value types and assigning one equal to
#   the other is just copying the current value. However, with objects, we
#   create a reference when assigning one to the other. Take this example:

#changing intial state of GameObject
game_object = GameObject("Enemy", 1, 2)

#creating variable equal to initial states of GameObject
other_game_object = game_object

# Here, other_game_object is a reference to game_object so they are
#   actually both referring to the same object rather than copying values,
#   therefore the values are shared between them both. This means that
#   whenever we change a value within one of them, we also change the other:

# changing name property
other_game_object.name = "new name"

# Changing the name property in other_game_object also changes the name
#   in game_object. This can lead to unexpected problems if not properly
#   managed.



# printing variables
print(other_game_object.name)
print(game_object.name)

# inheritance allows one class to “inherit” or essentially copy over all
#    of the variables and functions of another class as well as implement
#    its own. This is very useful when we want a set of variables and
#    functions that many different classes will share. Consider the
#    following example

# creating superclass titled GameObject
class GameObject:
  
  # setting 3 intial conditions 
  def __init__(self, name, x_pos, y_pos):
    self.name = name
    self.x_pos = x_pos
    self.y_pos = y_pos

  # creating function with 2 parameters   
  def move(self, by_x_amount, by_y_amount):

    # adding numbers to x_pos
    self.x_pos += by_x_amount

    # addining number to y_pos
    self.y_pos += by_y_amount

# creating a subclass that inherits properties from class GameObject 
class Enemy(GameObject):
  
  # setting 4 initial conditions 
  def __init__(self, name, x_pos, y_pos, health):

    # inheriting GameObject intializer
    super().__init__(name, x_pos, y_pos)

    # defining the new condition
    self.health = health

    # new function with one parameter 
  def take_damage(self, amount):

    # subtracting numbers from health
    self.health -= amount

enemy = Enemy("Enemy", 5, 10, 100)
print(enemy.health)

game_object = GameObject("Game object", 1, 2)
print(game_object.x_pos)