# Number Guessing Game - Picker
# The program thinks of a number between 1 and 100 and the user tries to guess it.
# The program should tell the user if the guess is too high or too low.
# The program should also tell the user how many guesses it took to guess the number.

import random

MIN_NUMBER = 1
MAX_NUMBER = 100

def get_valid_guess():
   guess = input("Enter your guess (1-100): ")
   while True:
         try:
              guess = int(guess)
              if MIN_NUMBER <= guess <= MAX_NUMBER:
                return guess
              else:
                print(f"Please enter a number between {MIN_NUMBER} and {MAX_NUMBER}.")
         except ValueError:
              print("Invalid input. Please enter a valid integer.")
         guess = input("Enter your guess (1-100): ")        
def play_picker():
    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    guess_count = 0
    while True:
        guess = get_valid_guess()
        guess_count += 1
        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {guess_count} guesses.")
            return guess_count
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

def main():
    print('=' * 60)
    print()
    print("Welcome to the Number Guessing Game!")
    print()
    while True:
        guess_count = play_picker()
        answer = input("Do you want to play again? (y/n) ").lower()
        if answer != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()