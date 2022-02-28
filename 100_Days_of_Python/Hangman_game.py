#Hangman game
import random
import os


#use the 'word_list' from hangman_words.py

from hangman_words import word_list

# randomly choose a word from word_list and add it to the chosen_word variable
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#Import the logo from hangman_art.py 
from hangman_art import logo
print(logo)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    os.system("cls")

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"you have already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"{guess} is not in the word")
        lives -= 1
        #Import the stages from hangman_art.py
        from hangman_art import stages
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word was {chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

