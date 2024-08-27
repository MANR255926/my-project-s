import random

def number_guessing_game():
    """
    A number guessing game where the computer generates a random number
    and the player tries to guess it.
    """

    min_value = int(input("Enter the minimum value: "))
    max_value = int(input("Enter the maximum value: "))

    random_number = random.randint(min_value, max_value)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between {} and {}: ".format(min_value, max_value)))

            if guess < random_number:
                print("Your guess is too low.")
            elif guess > random_number:
                print("Your guess is too high.")
            else:
                print("Congratulations! You guessed the number in {} attempts.".format(attempts + 1))
                break

            attempts += 1
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    number_guessing_game()