#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rock Paper Scissors CLI - Utility Functions

Helper functions for Rock-Paper-Scissors game logic.
"""

import random

def normalize_choice(user_input):

    choice = user_input.strip().lower()
    if choice in ["rock", "r"]:
        return "rock"
    elif choice in ["paper", "p"]:
        return "paper"
    elif choice in ["scissors", "s"]:
        return "scissors"
    else:
        return None

def get_computer_choice():

    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):

    if user_choice == computer_choice:
        return "tie"

    if (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "user"
    else:
        return "computer"

def get_user_choice():

    while True:
        user_input = input("Please enter your choice: ")
        normalized = normalize_choice(user_input)

        if normalized is not None:
            return normalized

        print("Invalid choice. Please enter rock, paper, or scissors (r,p,s).")

def get_result_message(user_choice, computer_choice, winner):
    if winner == "tie":
        return f"{user_choice.capitalize()} cannot beat {computer_choice} → Draw"
    if winner == "user":
        return f"{user_choice.capitalize()} beats {computer_choice} → You win this round!"
    return f"{computer_choice.capitalize()} beats {user_choice} → Computer wins this round!"




