def print_multiple(message, repeats):
    for _ in range(repeats):
        print(message, end=" ")

def main():
    # Prompt the user for a message
    message = input("Please type a message: ")
    # Prompt the user for the number of repeats, converting input to integer
    repeats = int(input("Enter a number of times to repeat your message: "))
    # Call print_multiple with the message and repeats count
    print_multiple(message, repeats)

# Run the main function
if __name__ == "__main__":
    main()
