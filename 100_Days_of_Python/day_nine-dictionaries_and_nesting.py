# Day 9 - Dictionarues, nesting, and the secret auction
# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
    
# }

# # #retrieving items from a dictionary
# # print(programming_dictionary["Bug"])

# # Addubg new items to a dicationary
# programming_dictionary["Loop"] = "The action of doing something over and over again."

# #print(programming_dictionary)

# #loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])


# #Exercise 9.1
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}

# #TODO-2: Write your code below to add the grades to student_grades.👇
# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[student] = 'Acceptable'
#     else:
#         student_grades[student] = "Fail"
    

# # 🚨 Don't change the code below 👇
# print(student_grades)

# # Nesting...
# capitals = {
#   "France": "Paris",
#   "Germany": "Berlin",
# }
# # Nesting a list in a dictionary
# travel_log = {
#   "France": ["Paris", "Lille", "Dijon"],
#   "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }
# #Nesting Dictionary in a Dictionary(acceessed by key)

# travel_log = {
#   "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#   "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
# }

# #Nesting Dictionaries in Lists(accessed by index)

# travel_log = [
# {
#   "country": "France", 
#   "cities_visited": ["Paris", "Lille", "Dijon"], 
#   "total_visits": 12,
# },
# {
#   "country": "Germany",
#   "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#   "total_visits": 5,
# },
# ]

# # Exercise 9.2
# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
# def add_new_country(name, visit_count, cities_visited):
#     new_country = {}
#     new_country["country"] = name
#     new_country["visits"] = visit_count
#     new_country["cities"] = cities_visited
#     travel_log.append(new_country)


# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

# Blind Auction
import os
from auction_art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Angela": 123, "James": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid: 
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    #key  
    name = input("What is your name?: ")
    #value
    price = int(input("What is your bid?: $"))
    #add key and value to empty dictionary
    bids[name] = price
    #input for additional bids
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    #conditional for yes or no 
    if should_continue == "no":  
        bidding_finished = True
        #calling function for highest bid
        find_highest_bidder(bids)
    elif should_continue == "yes":
        #clearing screen
        os.system("cls")