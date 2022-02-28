# # Basic print and input code
# # input() will ask user input in console
# # then print() will print the string and the input from the user
# print("Hello " + input("What is your name?") + "!")

# # adding variables
# name = input("What is your name?")
# print(name)

# # switching values
# # add 3rd variable to allow switching out values
# a = input("a:")
# b = input("b:")
# c = a 
# a = b
# b = c
# print("a= " + a)
# print("b= " + b)

#"Band name generator"concatenator
#1. create greeting
print("Welcome to the new band name generator!")
#2. ask for city user grew up in (adding "\n puts cursor on new line")
city = input("what city did you grow up in?\n")
#3. ask user for pet name
pet = input("What was the name of your favorite pet?\n")
#4. combine name of city with pet name for new band name
print("Your new band name should be " + city +" " + pet +"!")