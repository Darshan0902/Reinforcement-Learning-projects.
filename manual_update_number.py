import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Enter your guess (between 1 and 100): ")

        # Check if input is a valid integer
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} correctly!")
            print(f"It took you {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

if __name__ == "__main__":
    guess_the_number()
