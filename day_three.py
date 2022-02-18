# Day three - conditional operators

# # basic if else 
# print("Welcome to the Rollercoaster!")
# height = int(input("What is your height in inches? "))
# if height >= 48:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you will have to wait to grow taller before you can ride.")

# # Odd or Even?
# number = int(input("What number do you want to check? "))
# number2 = number % 2
# if number2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

# # nested if else and if/elif/else
# print("Welcome to the Rollercoaster!")
# height = int(input("What is your height in inches? "))
# if height >= 48:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Please pay $5.")  
#     elif age <= 18:
#         print("Please pay $7.")   
#     else:
#         print("Please pay $12.") 
# else:
#     print("Sorry, you will have to wait to grow taller before you can ride.")

# #BMI index calculator with elif statement
# height = input("Enter your height in inches: ")
# weight = input("Enter your weight in lbs: ")
# h = int(height)
# w = int(weight)
# bmi = w/(h**2)*703
# #print(bmi)
# # round the number
# bmi_round = round(bmi,2)
# #print(bmi_round)
# if bmi_round < 18.5:
#     print(f"Your rounded BMI score is {bmi_round}, you are classified as underweight")
# elif bmi_round < 25:
#     print(f"Your rounded BMI score is {bmi_round}, you are classified as normal weight")
# elif bmi_round < 30:
#     print(f"Your rounded BMI score is {bmi_round}, you are classified as overweight")
# elif bmi_round < 55:
#     print(f"Your rounded BMI score is {bmi_round}, you are classified as obese")
# else:
#     print(f"Your rounded BMI score is {bmi_round}, you are classified as clinically obese")



# # Is it a leap year? Is the given year a leap year.
# # This is determined by checking to see if:
# # 1. the year is evenly divisble by 4
# # 2. EXCEPT years that are evenly divisible by 100
# # 3. UNLESS  the year is also dvivisible by 400.
# year = int(input("What year do you want to check? "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year!")
#         else:
#             print("Not a leap year")
#     else:
#         print("Leap year!")
# else:
#     print("Not a leap year")


# # Multiple if statements - Rollercoaster
# print("Welcome to the Rollercoaster!")
# # Check height to se if they can ride
# height = int(input("What is your height in inches? "))
# if height >= 48:
#     print("You can ride the rollercoaster!")
#     # checking age to detemine ticket price
#     age = int(input("What is your age? "))
#     if age < 12:
#         # Adding bill variable to this condition
#         bill = 5
#         print("Child tickets are $5.")  
#     elif age <= 18:
#         # Adding bill variable to this condition
#         bill = 7
#         print("Youth tickets are $7.")   
#     else:
#         # Adding bill variable to this condition
#         bill = 12
#         print("Adult tickets are $12.")
#     # chcking to see if they want a photo 
#     wants_pic = input("Do you want a photo taken? Y or N ")
#     if wants_pic == "Y":
#         # add 3 to the bill
#         bill += 3
#     # print out the total bill
#     print(f"Your final price is ${bill}")
# else:
#     print("Sorry, you will have to wait to grow taller before you can ride.")


# # Python Pizza with multiple if statements
# print("Welcome to Python Pizza!")
# size = input("What size pizza do you want? S, M, L. ")
# add_pepperoni = input("Would you like pepperoni? Y or N ")
# extra_cheese = input("Would you like extra cheese? Y or N ")
# # set an empty variable for the bill
# bill = 0
# # add to bill based on size
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25
# # add to bill based on pepperoni answer
# if add_pepperoni == "Y":
#     if size =="S":
#         bill += 2
#     else:
#         bill += 3
#         # add to bill based on chese answer
# if extra_cheese =="Y":
#     bill += 1
# # print out final price of pizza
# print(f"Your final price is ${bill}")

# Treasure Island






