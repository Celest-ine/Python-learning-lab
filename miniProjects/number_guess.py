# A program that generates a random number and asks the user to guess it until they get it right.

import random

number = random.randint(1, 20)
guess = 0

while guess != number:
    guess = int(input("Guess a number between 1 and 20: "))
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guesssed the number!")