# Function to double the input number
def double(num):
    return num * 2

# Main function to interact with the user
def main():
    # Ask the user for a number
    num = int(input("Enter a number: "))
    # Call the double function and print the result
    result = double(num)
    print("Double that is", result)

# Run the main function
if __name__ == "__main__":
    main()
