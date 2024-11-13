def greet(name):
    # Print a greeting with the given name
    print(f"Greetings {name}!")

def main():
    # Prompt the user to enter their name
    name = input("What's your name? ")
    # Call the greet function with the user's name
    greet(name)

# Run the main function
if __name__ == "__main__":
    main()
