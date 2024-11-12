# The affirmation to be typed by the user
affirmation = "I am capable of doing anything I put my mind to."

# Prompt the user until they type the affirmation correctly
while True:
    print("Please type the following affirmation:")
    user_input = input()  # Get user input without an inline prompt

    if user_input == affirmation:
        print("That's right! :)")
        break  # Exit the loop if the affirmation is correct
    else:
        print("Hmmm, that was not the affirmation.")

