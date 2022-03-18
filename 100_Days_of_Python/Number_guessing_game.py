#Number Guessing Game 
from random import randint
from number_guess_art import logo

#Global constants
EASY_LEVEL = 15
MID_LEVEL = 10
HARD_LEVEL = 5

#Create function to check user's guess against actual answer
def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"Thats it! The number was {answer}.")

#Create function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty level. Type 'easy', 'medium', or 'hard': ")
    if level == "easy":
        return EASY_LEVEL
    elif level == "medium":
        return MID_LEVEL
    else:
        return HARD_LEVEL

def game():
    print(logo)
    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1 and 100")


    #Choosing a random number between 1 and 100
    answer = randint(1, 100)
    #code for testing
    print(f"The answer is {answer}")

    #ask user to choose a difficulty
    turns = set_difficulty()

    #set variable for guess
    guess = 0
    #Repeat the guessing if they are wrong
    while guess != answer:
        print(f"You have {turns} attempts to guess the number")
        #Let the user guess a number:
        guess = int(input("Make a guess: "))

        #Track the number of turns and reduce it by 1 if they give wrong answer
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("Sorry, but you have ran out of turns, you lose!")
            return
        elif guess != answer:
            print("Guess again")

game()

