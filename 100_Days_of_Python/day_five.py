# #For Loop with Lists
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#   print(fruit)
#   print(fruit + " Pie")
# print(fruits)

# # # 🚨 Average Student Height coding excercise 👇 
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])

# # Get the total of all heights
# total_height = 0
# for height in student_heights:
#     total_height += height
# print(f'Total height = {total_height}')
# # get the total number of students
# num_students = 0
# for student in student_heights:
#     num_students += 1
# print(f"Total number of students = {num_students}")
# # get the average (round to nearest whole number)
# avg_height = round(total_height/num_students)
# print(f' Average height is {avg_height}')

# ## or use a simplified code (without for loop)
# total_height = sum(student_heights)
# num_students = len(student_heights)
# avg_height = round(total_height/num_students)
# print(f' Average height is {avg_height}')

# # 🚨 High Score coding exercise 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)

# #using a for loop to find high score
# high_score = 0
# for score in student_scores:
#     if score > high_score:
#         high_score = score
# print(f'The highest score is {high_score}')

# ## or....
# high_score = max(student_scores)
# print(f'The highest score is {high_score}')

### For loops and the range() function
# # totaling numbers from 1 to 100
# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

# ### Sum of even numbers from 1 to 100
# total = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         total += number
# print(total)
# ## It can also be done like this...
# total2 = 0
# for number in range(2, 101, 2):
#     total2 += number
# print(total2)

### FizzBuzz

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 ==0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)
