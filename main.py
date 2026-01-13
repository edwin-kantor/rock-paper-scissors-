#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rock Paper Scissors CLI - Main Program

A command-line Rock-Paper-Scissors game where users play against the computer.
"""

# TODO 🇺🇸: Import utility functions from utils.py

from utils import (normalize_choice, get_computer_choice, determine_winner, get_user_choice, get_result_message)

def play_round(user_score, computer_score):
    print("\nOptions: rock / paper / scissors")

    while True:
        user_input = input("User choice: ").strip().lower()
        user_choice = normalize_choice(user_input)

        if user_choice is None:
            print("Invalid choice. Please try again.")
            continue
        break

    computer_choice = get_computer_choice()

    print(f"Computer choice: {computer_choice}")

    winner = determine_winner(user_choice, computer_choice)
    message = get_result_message(user_choice, computer_choice, winner)
    print(message)

    if winner == "rock":
        user_score += 1
    elif winner == "computer":
        computer_score += 1

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
            user_score, computer_score = play_round(user_score, computer_score)

        print("\n--- Final Score (3 rounds) ---")
        show_score(user_score, computer_score)

        continue_game = input("\nDo you want to continue? (y/n): ").strip().lower()
        if continue_game == "y":
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
