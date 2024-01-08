# if statements is a way execute code only if some tests returns true.
#   the test is boolean and compares some variable to another. Consider
#   the following 

#representing a keystroke with a string
key = "r"

# if key equals r print move right
if key == "r": #notice colon
  print("move right") # notice indentation

# outside of indentation print done
print("done") 

# if we want to compare multiple variables we can use elif

# if key equals r print move right
key = "l"
if key == "r":
  print("move right")

# if key equals l print move left
elif key == "l":
  print("move left")

# print done
print("done")

# elif statement is only run if the previous tests return False. If we 
#   want some default code to execute if all previous tests return False,
#   we can use else

# if key equals r print move right
key = "u"
if key == "r":
  print("move right")

# if key equals l print move left
elif key == "l":
  print("move left")

# if key is not r or l print invalid key
else:
  print ("invalid key")

# print done
print("done")

# loops provide a way to execute code multiple times without having to 
#   type the same code again and again. 
#
# the simpleset form is the while loop. It is similiar to an if statement 
#   being ran multiple times. It performs a test and executes code if the 
#   test returns True but instead of executing the code once, it 
#   continuously executes the code until the test eventually returns False.
#   Consider the following example

# creating integer variables 
position = 0
end_position = 10

# while loop that will run until position >= endPosition
while position < end_position: # note the colon
  position += 1 #note the indentation
  print(position)
  if position == end_position:
    print("You have reached the end")

# the loop increases the position variable by 1 for each loop iteration and
#   prints the new position out, so it runs 10 times. Once the position 
#   evaluates to 10 (as it is updated with each iteration), the condition 
#   position < end_position evaluates to False and so the loop breaks or 
#   stops running and any proceeding code is executed.

# we can control the loop iterations with "continue" and "break" 
#   statements. The continue command forces the loop to go to the next
#   iteration, whereas break will exit the loop immediately. Consider the
#   following

# creating integer variables
position = 0
end_position = 10
enemy_position = 5

# while loop that will run until position >= endPosition unless the
#   position is equal to enemyPosition
while position < end_position:
  position += 1
  print(position)
  if position == enemy_position:
    print("Game over!")
    break

# the above loop only runs 5 times when  position = 5, 
#   position == enemy_position = True and the break statement is reached,
#   causing the loop to stop running.

# a for loop acts similiar to a while loop but it runs a preset number
#   of times. We build right into the loop when to start and when to 
#   stop. Consider the where we pair the loop with a collection type to 
#   visit every element of a list. When we pair it with a list, for 
#   example, we iterate through the list with each iteration of the loop 
#   visiting the next element of the list. We can visit every member of 
#   a list and print it out. 

enemy_positions = [5, 10, 15]
for enemy_position in enemy_positions:
  print(enemy_position)

# the for in loop starts at the beginning of enemy_positions (index 0). 
#   It assigns the value of enemyPositions[0] into enemyPosition and 
#   runs the loop body (print(enemyPosition)). Then it moves to the next
#    iteration and visits the next member of the list (index 1). This 
#   process continues, each time updating the enemy_position to contain 
#   the value of the current index of enemyPositions until it has run 
#   every element in the list. If the list is empty, the loop will run 0 
#   times.

# for loops can also be paired with ranges if we want to set the number
#   of times a for loop should run. For example we could print "Hello" 5
#   times like this

for i in range(0,5):
  print("Hello")

# The for loop runs as many times as there are elements in the range
#   [0,1,2,3,4,5](note that the upper bound 5 is not included). A final 
#   thing to note is that every for loop can be turned into a while loop 
#   but not every while loop can be turned into a for loop. This is
#   because we sometimes do not know how many times a while loop will
#   run.