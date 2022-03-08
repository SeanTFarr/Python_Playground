#Day 10 - Functions with outputs

# def format_name(f_name, l_name):
#     # '.title' formats a string to capitol first letter and the rest is made lower case
#     print(f_name.title())
#     print(l_name.title())
# # calling the function
# format_name("sean", 'FARR')

# # a cleaner way to do it, with print
# def format_name(f_name, l_name):
#     # '.title' formats a string to capitol first letter and the rest is made lower case
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     print(f"{formated_f_name} {formated_l_name}")
# # calling the function
# format_name("sean", 'FARR')

# # and with return
# def format_name(f_name, l_name):
#     # '.title' formats a string to capitol first letter and the rest is made lower case
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
# # calling the function
# print(format_name("sean", 'FARR'))

# # and with return
# def format_name(f_name, l_name):
#     #adding a conditional with a return
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs."
#     # '.title' formats a string to capitol first letter and the rest is made lower case
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
# # calling the function, requesting user input
# print(format_name(input("What is your first name? "), input("What is your last name? ")))

# Exercise 10.1 Days in a month
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    # check for invalid input
    if month > 12 or month < 1:
        return "Invalid month selected"
    # check if leap year and if February 
    if is_leap(year) and month == 2:
      return 29
    # if not, return selected month and subract 1 due to index numbering
    return month_days[month -1]
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(f"There are {days} days in that month")