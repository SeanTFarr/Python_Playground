############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):#🐞the number will not reach '20' because of the indexing
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)# 🐞range needs to go from 0 to 5(indexing)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:  #🐞needs an equal sign to capture "1994"
#   print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.") #🐞needs indenting and 'f' in the print function

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))#🐞double equals sign causes issue(acts as a True/False statement)
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)# 🐞Should be indented more
#   print(b_list)

# mutate([1,2,3,5,8,13])

# #13-1 Excercise
# number = int(input("Which number do you want to check?"))

# if number % 2 = 0:#🐞 needs a double equals sign
#   print("This is an even number.")
# else:
#   print("This is an odd number.")

# #13-2 excercise
# year = input("Which year do you want to check?")#🐞needs to be converted into 'int'

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")

# #13-3 excercise
# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:#🐞needs to have "and" instead of "or"
#     print("FizzBuzz")
#   if number % 3 == 0:#🐞should be 'elif'
#     print("Fizz")
#   if number % 5 == 0:#🐞should be 'elif'
#     print("Buzz")
#   else:
#     print([number])
  