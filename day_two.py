# Day 2 - Data types

# # Can't concatenate strings and integers together to print
# num_char = len(input("What is your name?")) # Is an integer
# # Change the int to a string
# new_num_char = str(num_char)
# # now they will print together
# print("Your name has "+ new_num_char + " characters in it.")

# # request a two digit number then add them together
# two_digit_number = input("type a two digit number: ")
# a = two_digit_number[0]
# b = two_digit_number[1]
# result = int(a) + int(b)
# print(a)
# print(b)
# print(result)

# # BMI index calculator
# height = input("Enter your height in inches: ")
# weight = input("Enter your weight in lbs: ")
# h = int(height)
# w = int(weight)
# bmi = w/(h**2)*703
# print(bmi)
# # round the number
# bmi_round = round(bmi,2)
# #print(bmi_round)
# # the f-string
# print(f"Your rounded BMI score is {bmi_round}")

# # Time left until 90 years old
# age = input("What is your current age?")
# age_int = int(age)
# yrs_remain = 90 - age_int
# days_left = yrs_remain * 365
# week_left = yrs_remain * 52
# mos_left = yrs_remain * 12
# print(f"You have {days_left} days, {week_left} weeks, and {mos_left} months remaining!")

# Tip calculator
print("Welcome to the tip calculator")
bill = float(input("What is the total bill? $"))
tip = int(input("What percentage tip would you like to leave? 15, 18, 20: "))
tip_percent = tip/100 
tip_calc = bill * tip_percent
tip_amount = round(tip_calc, 2)
total_pay = bill + tip_amount
print(f"Your tip will be ${tip_amount} and the total paid will be ${total_pay}")