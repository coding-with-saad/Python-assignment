# Define the adult age threshold
ADULT_AGE = 18

def is_adult(age):
    # Check if age is greater than or equal to ADULT_AGE
    if age >= ADULT_AGE:
        return True
    else:
        return False

def main():
    # Prompt the user to enter an age
    age = int(input("How old is this person?: "))
    # Call is_adult with the given age and print the result
    print(is_adult(age))

# Run the main function
if __name__ == "__main__":
    main()
