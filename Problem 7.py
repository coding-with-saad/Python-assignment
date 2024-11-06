import random

# Global variable
total_rolls = 3  # Number of times to roll two dice

def roll_dice():
    # Local variables inside the function
    die1 = random.randint(1, 6)  # Roll the first die (1 to 6)
    die2 = random.randint(1, 6)  # Roll the second die (1 to 6)
    return die1, die2

def main():
    # Using the global variable
    for roll_num in range(1, total_rolls + 1):
        # Each call to roll_dice() generates a new set of local die1 and die2 values
        die1, die2 = roll_dice()
        print(f"Roll {roll_num}: Die 1 = {die1}, Die 2 = {die2}")
        add=die1+die2
        print(add)

# Execute the main function
main()
