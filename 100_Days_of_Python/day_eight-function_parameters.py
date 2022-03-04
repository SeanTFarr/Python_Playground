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

# # Area calculator
# import math
# #👇
# def paint_calc(height, width, cover):
#     # added math.ceil to round number up
#     need = int(math.ceil((height * width) / cover))
#     print(f"You will need {need} cans of paint")

# #👆
# # Define a function called paint_calc() so that the code below works.   

# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

# #prime number checker
# #👇
# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("it's a prime number.")
#     else:
#         print("it's not a prime number.")
# #👆
    
# #👇
# n = int(input("Check this number: "))
# prime_checker(number=n)

# Caesar Cipher encryption🐛
from pydoc import plain


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Combine the encrypt() and decrypt() functions into a single function called caesar()

#Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
    #Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

#Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text, shift_amount):
    #Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        plain_text += new_letter
    print(f"The decoded text is {plain_text}")
    #print output: "The decoded text is hello"


#Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. 
# You should be able to test the code to encrypt *AND* decrypt a message.
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
else:
    decrypt(cipher_text=text, shift_amount=shift)

#Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.