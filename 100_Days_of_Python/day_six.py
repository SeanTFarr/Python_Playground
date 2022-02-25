# Day 6 - Functions

##framework for defining functions
# def my_function():
#     #Do this
#     #Then do this
#     #Finally do this
## to operate it, call the function
# my_function()

# ## Functions created for "Reeborg's World"
# def turn_around():
#     turn_left()
#     turn_left()
    
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

#for step in range(6:)
#   jump()

##using the while loop, instead of for loop
#number_of_hurdles = 6
#while number_of_hurdles > 0:
#   jump()
#   number_of_hurdles -= 1

## Hurdle 4 challenge
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()

# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()
    
##Reeborg"s Maze Challenge
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# while front_is_clear():
#     move()
# turn_left()

# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
        