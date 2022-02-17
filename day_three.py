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

#BMI index calculator with elif statement
height = input("Enter your height in inches: ")
weight = input("Enter your weight in lbs: ")
h = int(height)
w = int(weight)
bmi = w/(h**2)*703
#print(bmi)
# round the number
bmi_round = round(bmi,2)
#print(bmi_round)
if bmi_round < 18.5:
    print(f"Your rounded BMI score is {bmi_round}, you are classified as underweight")
elif bmi_round < 25:
    print(f"Your rounded BMI score is {bmi_round}, you are classified as normal weight")
elif bmi_round < 30:
    print(f"Your rounded BMI score is {bmi_round}, you are classified as overweight")
elif bmi_round < 55:
    print(f"Your rounded BMI score is {bmi_round}, you are classified as obese")
else:
    print(f"Your rounded BMI score is {bmi_round}, you are classified as clinically obese")