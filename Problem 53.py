# Helper function to subtract 7 from num
def subtract_seven(num):
    return num - 7

# Main function
def main():
    # Ask the user for a number
    num = int(input("Enter a number: "))
    
    # Call the subtract_seven function and store the result
    result = subtract_seven(num)
    
    # Print the result
    print(f"The result of subtracting 7 is: {result}")

# Run the main function
main()
