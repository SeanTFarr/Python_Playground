# Day 8 - Function Parameters & Caesar Cipher
# # Review: simple function
# # Create a function called greet(). 
# def greet():
#     print(" This is")
#     print("  good")
#     print("practice!")
# # Write 3 print statements inside the function.
# # Call the greet() function and run your code.
# greet()

# # Function that allows for input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"how are you, {name}?")
# greet_with_name('Sean')

# # Functions with more than 1 input
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"what is it like in {location}?")

# greet_with("Jessica", "Korea")

# Area calculator
import math
#Write your code below this line 👇
def paint_calc(height, width, cover):
    # added math.ceil to round number up
    need = int(math.ceil((height * width) / cover))
    print(f"You will need {need} cans of paint")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


