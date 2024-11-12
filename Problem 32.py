import random

# Randomly select a number between 0 and 99
a = random.randint(0, 99)

print("I am thinking of a number between 0 and 99...")

# Loop until the user guesses the correct number
while True:
    guess = int(input("Enter a guess: "))

    if guess < a:
        print("Your guess is too low")
    elif guess > a:
        print("Your guess is too high")
    else:
        print(f"Congrats! The number was: {a}")
        break

