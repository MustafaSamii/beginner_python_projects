"""

This is a simple number guessing game where the user has to guess a randomly generated number between 0 and 50. 
It was good review for simple Python concepts like loops, conditionals, and user input.
It works well and i didnt just copy it from somewhere, I wrote it myself.
good work! Time for the next project!

"""



import random

def Game():
    number = random.randint(0, 50)
    tries = 0
    print("Welcome to the Number Guessing Game!")
    print("You have 3 tries to guess the number between 0 and 50.")
    while tries < 3:
        user_data = int(input("Enter a number to guess:"))
        tries +=1
        print({number})
        if user_data == number:
            print(f"You got it! It took you {tries} tries")
            break
        elif user_data<number:
            print(f"Wrong, try a bit higher -- you're on # {tries}")
        else:
            print(f"Wrong, try a bit lower -- you're on # {tries}")
    if tries == 3:
        print(f"Sorry, you've used all your tries. The correct number was {number}.")

Game()