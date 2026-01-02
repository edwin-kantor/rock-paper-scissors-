#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rock Paper Scissors CLI - Main Program

A command-line Rock-Paper-Scissors game where users play against the computer.
"""

# TODO 🇺🇸: Import utility functions from utils.py

from utils import (normalize_choice, get_computer_choice, determine_winner, get_user_choice, get_result_message)

def play_round(user_score, computer_score):

    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    winner = determine_winner(user_choice, computer_choice)

    if winner == user_choice:
        print("You won!")
        user_score += 1
    elif winner == "computer":
        print("Computer won this round!")
        computer_score += 1
    else:
        print("It's a draw")

    return user_score, computer_score


def show_score(user_score, computer_score):

    print("\nCurrent Scores:")
    print(f"User score: {user_score}")
    print(f"Computer score: {computer_score}")

def main():
    """
    Main program loop
    """

    print("Rock, Paper, Scissors Game")
    print("Rules:")
    print("- Rock beats scissors")
    print("- Paper beats rock")
    print("- Scissors beats paper")
    print("- Same choice = draw\n")

    while True:
        user_score = 0
        computer_score = 0

        for round_number in range(1, 4):
            print(f"\nRound {round_number}")

            while True:
                user_input = input("User choice (rock/paper/scissors): ").strip().lower()
                user_choice = normalize_choice(user_input)

                if user_choice is None:
                    print("Invalid choice. Try again.")
                    continue
                break

            computer_choice = get_computer_choice()

            print(f"User choice: {user_choice}")
            print(f"Computer choice: {computer_choice}")

            winner = determine_winner(user_choice, computer_choice)
            message = get_result_message(user_choice, computer_choice, winner)
            print(message)

            if winner == "user":
                user_score += 1
            elif winner == "computer":
                computer_score += 1

        print("\n--- Final Score (3 rounds) ---")
        show_score(user_score, computer_score)

        continue_game = input("\nDo you want to continue? (y/n): ").strip().lower()
        if continue_game != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()