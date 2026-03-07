import random

print("===============================================================")
print("                       NUMBER GUESSING GAME                    ")
print("===============================================================")
print("Welcome to the game!")
print("Easy level is 1-10 with 3 tries.")
print("Medium level is 1-50 with 4 tries.")
print("Hard level is 1-100 with 5 tries.")
print()

preferred_name = input("Enter your preferred name: ")
print(f"Welcome to the game {preferred_name}!")
print()

games_played = 0
games_won = 0
playing = "y"

while playing == "y":
    answer = input("Are you ready to play? y/n: ").lower()

    if answer == "y":

        print("Great! Good luck!")

        # Difficulty Selection
        while True:

            difficulty = input("Enter a difficulty level: easy, medium, hard: ").lower()

            if difficulty == "easy":
                max_number = 10
                max_tries = 3
                break

            elif difficulty == "medium":
                max_number = 50
                max_tries = 4
                break

            elif difficulty == "hard":
                max_number = 100
                max_tries = 5
                break

            else:
                print("Please enter only Easy, Medium, or Hard.")

        secret_number = random.randint(1, max_number)

        tries = 0
        games_played += 1

        print(f"You selected {difficulty.capitalize()} mode!")
        print(f"Guess a number between 1 and {max_number}: ")
        print(f"You have {max_tries} tries left!")
        print()

        # Guessing Loop
        while tries < max_tries:

            while True:

                try:
                    guess = int(input(f"Enter a guess between 1 and {max_number}: "))

                    if 1 <= guess <= max_number:
                        break
                    else:
                        print(f"That number is not between 1 and {max_number}! Try again.")

                except ValueError:
                    print("Please enter a valid number.")

            tries += 1

            if guess == secret_number:

                games_won += 1
                print(f"You must be a genius! You guessed the number in {tries} tries!")
                break

            elif guess > secret_number:

                print("Sorry, your guess is too high!")
                print(f"You have {max_tries - tries} tries left!")
            else:

                print("Sorry, your guess is too low!")
                print(f"You have {max_tries - tries} tries left!")

        # Game Over Condition
        if tries == max_tries and guess != secret_number:
            print(f"Game over! The number was {secret_number}.")

        print()
        print(f"Score: {games_won} win(s) out of {games_played} game(s) played.")

    else:

        print("Okay, maybe next time!")

    print()
    playing = input("Would you like to play again? y/n: ").lower()
    print()

print("Thank you for playing!")
