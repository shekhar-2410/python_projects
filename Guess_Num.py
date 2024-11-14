# Guess number 1-100
import random


def guess_number():
    gussed_number = int(input("Guess a number between 1 and 100: "))
    secret_number = random.randint(1, 100)
    print(secret_number)

    while True:

        if gussed_number > secret_number:
            print("Too high! try again")
            gussed_number = int(input("Guess a number between 1 and 100: "))

        elif gussed_number < secret_number:
            print("Too low! try again")
            gussed_number = int(input("Guess a number between 1 and 100: "))
            

        else:
            print("Bingo! You guessed the correct number🎉")
            break


guess_number()
