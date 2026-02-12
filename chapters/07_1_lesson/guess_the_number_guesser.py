

import random


def get_number_feedback():
    while True:
        feedback = input("Is my guess too high (h), too low (l), or correct (c)? ").lower()
        if feedback in ['h', 'l', 'c']:
            return feedback
        else:
            print("Invalid input. Please enter 'h', 'l', or 'c'.")      

def get_number():
    while True:
        try:
            number = int(input("Please enter the number you thought of (1-100): "))
            if 1 <= number <= 100:
                return number
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
def play_guesser():
    MIN_NUMBER = 1
    MAX_NUMBER = 100
    print('-' * 60)
    print()
    print(f"Think of a number between {MIN_NUMBER} and {MAX_NUMBER} (inclusive).")
    input("Press Enter when you have thought of a number.")
    print()
    guess_count = 0
    # TODO: Implement the rest of this function
    pass

def main():
    print('-' * 60)
    print()
    print("Welcome to the Number Guessing Game!")
    print()
    while True:
        guess_count = play_guesser()
        answer = input("Do you want to play again? (y/n) ").lower()
        if answer == "n":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()