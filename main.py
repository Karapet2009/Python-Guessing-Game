import random

print("--- Difficulty Levels ---")
print("Easy: 1-50")
print("Medium: 1-100")
print("Hard: 1-500")
option = input("Enter the difficulty level (E, M, H): ").lower()

if option == "e":
    lowest_num = 1
    highest_num = 50
elif option == "m":
    lowest_num = 1
    highest_num = 100
elif option == "h":
    lowest_num = 1
    highest_num = 500
else:
    print("Invalid difficulty.")
    exit()

guesses = 0
is_running = True
answer = random.randint(lowest_num, highest_num)

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:

    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range.")
            print(f"Please select a number between {lowest_num} and {highest_num}")

        elif guess < answer:
            print("Too low! Try again!")

            difference = abs(answer - guess)
            if difference <= 5:
                print("Very close!")
            elif difference <= 15:
                print("Warm")

        elif guess > answer:
            print("Too high! Try again!")

            difference = abs(answer - guess)
            if difference <= 5:
                print("Very close!")
            elif difference <= 15:
                print("Warm")

        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False

        if guesses == 7 and is_running:
            print(f"You lost, attempts count {guesses}")
            print(f"The correct number was {answer}")
            is_running = False

        print(f"Attempts left: {7 - guesses}")

    else:
        print("Invalid guess")
        print(f"Please select a number between {lowest_num} and {highest_num}")