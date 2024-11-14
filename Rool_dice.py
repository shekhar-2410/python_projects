# roll a dice
import random


def roll_dice():
    roll_dice = input("Roll the dice (y/n): ").lower()
    if roll_dice == "y"  and roll_dice == "n":

        while True:
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            print("you rolled a", (dice1, dice2))

            roll_dice = input("Roll the dice again (y/n): ")

            if roll_dice != 'y':
                print("Goodbye!")
                break
    else:
         print("Invalid input. Please enter 'y' or 'n'.")


roll_dice()
