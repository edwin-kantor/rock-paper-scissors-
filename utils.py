#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quiz Game CLI - Utility Functions

Helper functions for Quiz Game logic.
"""


def get_questions():
    """
    Get list of quiz questions
    
    Returns:
        List of dictionaries, each containing 'question', 'options', and 'answer'
    """

    return [
        {
            "question": "If you dig a 6 foot hole, how deep is that hole ?",
            "options": [
                "A) 6 foot deep",
                "B) 8 foot deep",
                "C) 8 foot deep",
                "D) 9 foot deep",
            ],
            "answer": "A",
        }
    ]

def normalize_answer(user_input):
    """
    Normalize user input for consistent comparison
    
    Args:
        user_input: Raw user input string
    
    Returns:
        Normalized uppercase string or None if invalid
    """
    normalized = user_input.strip().upper()

    if normalized in ["A", "B", "C", "D"]:
        return normalized

    return None



def get_user_answer():
    """
    Get and validate user's answer
    
    Returns:
        Normalized valid answer (A, B, C, or D)
    """
    # TODO 🇺🇸: Create infinite loop for input validation,
    #          get user input using input(), normalize it using
    #          normalize_answer(), return valid answer or print
    #          error message on invalid input
    while True:
        user_input = input("Enter A, B, C, or D: ")
        normalized_answer = normalize_answer(user_input)

        if normalized is not None:
            return normalized

        print("Invalid input, please enter A, B, C, or D.")

