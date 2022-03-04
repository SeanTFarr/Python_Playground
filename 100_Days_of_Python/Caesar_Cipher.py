# Caesar Cipher 
from pydoc import plain


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is '{end_text}'")

from caesar_art import logo
print(logo)

#code to restart if user wants
should_end = False
while not should_end:
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # using the % we get a remander, to keep the number within the 26 letters
    shift = shift % 26

    #Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
    caesar(start_text = text, shift_amount = shift, cipher_direction = direction)

    # ask if restart desired
    restart = input("Want to restart? Type 'yes' if you want to or type 'no' if you do not.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")