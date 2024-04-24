# 5- Gusses game
import random

def play_guessing_game(tries):
    secret_number = random.randint(1, 5)
    guessed_numbers = set()

    while tries > 0:
        user_input = input("Guess the number (between 1 and 100): ")

        if not user_input.isdigit() or int(user_input) < 1 or int(user_input) > 100:
            print("Invalid input. Please enter a number between 1 and 100.")
            continue

        guess = int(user_input)

        if guess in guessed_numbers:
            print("You've already guessed this number. Try a different one.")
            continue

        guessed_numbers.add(guess)

        if guess == secret_number:
            print("Congratulations! You guessed the number {} correctly!".format(secret_number))
            play_guessing_game(tries)  
            return

        if guess < secret_number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")
            
        tries -= 1

    print("Sorry, you've run out of tries. The correct number was {}.".format(secret_number))

play_guessing_game(10)
