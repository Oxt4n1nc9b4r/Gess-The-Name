import random

def choose_name():
    names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hannah', 'Ian', 'Julia','Jui','Lami']
    return random.choice(names)

def guess_name():
    name_to_guess = choose_name()
    attempts = 3

    print("Welcome to the Name Guessing Game!")
    print("You have 3 attempts to guess the name.")
    print("The name consists of a single word with the first letter capitalized.")

    while attempts > 0:
        guess = input("\nEnter your guess: ").strip().capitalize()
        
        if guess == name_to_guess:
            print("Congratulations! You guessed the name correctly!")
            return
        
        print("Incorrect guess. Try again.")
        attempts -= 1

    print(f"Sorry, you've run out of attempts. The correct name was {name_to_guess}.")

guess_name()
