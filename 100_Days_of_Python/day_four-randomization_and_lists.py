import random

# random_integer = random.randint(1, 50)
# print(random_integer)

# random_float = random.random() * 5
# print(random_float)

# # Coin flip!
# random_coin = random.randint(0, 1)
# if random_coin == 1:
#     print('Heads')
# else:
#     print('Tails')

# # Lists
# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia",
#     "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire",
#     "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
#     "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama",
#     "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
#     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska",
#     "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming",
#     "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# print(states_of_america[5])


# # Who will pay? Using a random generator
# # Split string method, to take a list of words given and create a python list of strings
# # Example list of names: Sean, Jessica, Andrew, Grace, David, Amanda, Robert, Sarah
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # # Method 1
# # #get the total number of items in list
# # num_items = len(names)
# # # Generate random numbers between 0 and the last index
# # random_choice = random.randint(0, num_items -1)
# # person_who_will_pay = names[random_choice]

# #Method 2- shorter code using .choice
# person_who_will_pay = random.choice(names)

# # Output results
# print(person_who_will_pay + ' is going to pay today.')


# # Lists inside of lists
# # List of fruits and vegetables to work with: Strawberries, Spinach, Kale, Nectarines, Apples, Grapes, Peaches, Cherries, Pears, Tomatoes, Celery, Potatoes
# veg_string = "Spinach, Kale, Tomatoes, Celery, Potatoes"
# vegetables = veg_string.split(", ")
# print(vegetables)
# fruit_string = "Strawberries, Nectarines, Apples, Grapes, Peaches, Cherries, Pears"
# fruits = fruit_string.split(", ")
# print(fruits)
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen[0][1])
# print(dirty_dozen[1][2])
# print(dirty_dozen[1][3])

# #4-3 exercise
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the X? ")#This gives a 2 digit string
# #first get hroizontal and vertical position
# horizontal = int(position[0])# first number
# vertical = int(position[1]) # second number
# # # select row and column
# # selected_row = map[vertical -1]
# # selected_row[horizontal -1]= "X"
# # simplified code
# map[vertical -1][horizontal -1]= 'X'

# print(f"{row1}\n{row2}\n{row3}")


# Rock, Paper, Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print