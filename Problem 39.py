import random

# The likelihood of done() returning True (set to 0.3 for this example)
DONE_LIKELIHOOD = 0.3

# Simulate the done() function
def done():
    return random.random() < DONE_LIKELIHOOD

# Chaotic counting function
def chaotic_counting():
    for i in range(1, 11):  # Loop from 1 to 10
        if done():  # Check if done() returns True
            return  # Exit the function early if done() is True
        print(i, end=" ")  # Print the current number if not done

# Main function
def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()  # Call chaotic_counting
    print("I'm done.")  # Print "I'm done." after chaotic_counting finishes

# Run the main function
if __name__ == "__main__":
    main()
