def print_divisors(num):
    print(f"Here are the divisors of {num}:")
    for i in range(1, num + 1):  # Loop from 1 to num (inclusive)
        if num % i == 0:         # Check if i is a divisor of num
            print(i, end=" ")

def main():
    # Prompt the user for a number
    num = int(input("Enter a number: "))
    # Call print_divisors with the user's number
    print_divisors(num)

# Run the main function
if __name__ == "__main__":
    main()
