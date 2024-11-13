def print_ones_digit(num):
    ones_digit = num % 10  # Get the ones digit
    print(f"The ones digit is {ones_digit}")

def main():
    # Prompt the user to enter a number
    num = int(input("Enter a number: "))
    # Call print_ones_digit with the user's number
    print_ones_digit(num)

# Run the main function
if __name__ == "__main__":
    main()
