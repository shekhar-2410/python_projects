# rock,paper and scissors game

import random

def play_game():
    choices = {"r": "Rock", "p": "Paper", "s": "Scissors"}
    while True:
        user_choice = input("Enter your choice (r for Rock, p for Paper, s for Scissors): ").lower()
        if user_choice not in choices:
            print("Invalid input. Please enter 'r', 'p', or 's'.")
            continue

        computer_choice = random.choice(["r", "p", "s"])

        print("Your choice:", choices[user_choice])
        print("Computer's choice:", choices[computer_choice])

        if user_choice == computer_choice:
            print("It's a Tie!")
        elif (user_choice == "r" and computer_choice == "s") or \
             (user_choice == "p" and computer_choice == "r") or \
             (user_choice == "s" and computer_choice == "p"):
            print("You win!")
        else:
            print("You lose!")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing!")
            break

play_game()
