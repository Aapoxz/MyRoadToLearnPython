import random

def guess_number():
   # Coded by aapoxz lol
    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0

    print("Welcome to the number guessing game!")
    print("I have selected a number between 1 and 100. Try to guess it!")

   
    while guess != number_to_guess:

        guess = int(input("Enter your guess: "))
        attempts += 1

   
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")

# Run the guess number game
guess_number()
