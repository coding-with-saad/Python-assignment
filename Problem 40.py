def count_even(lst):
    # Populate the list by prompting the user for input
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":  # Stop if the input is empty
            break
        try:
            num = int(user_input)  # Convert the input to an integer
            lst.append(num)  # Add the number to the list
        except ValueError:
            print("That's not an integer. Please try again.")

    # Count and print the number of even numbers in the list
    even_count = sum(1 for num in lst if num % 2 == 0)
    print(f"Number of even numbers: {even_count}")

# Example usage
lst = []
count_even(lst)
