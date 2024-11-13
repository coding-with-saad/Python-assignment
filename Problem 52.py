def get_user_data():
    # Ask for the first name and store it in a variable
    first_name = input("What is your first name?: ")
    
    # Ask for the last name and store it in a variable
    last_name = input("What is your last name?: ")
    
    # Ask for the email address and store it in a variable
    email = input("What is your email address?: ")
    
    # Return all three pieces of data as a tuple
    return first_name, last_name, email

# Calling the function and printing the result
user_data = get_user_data()

# Print the result as requested
print("Received the following user data:", user_data)
