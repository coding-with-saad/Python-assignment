# Define the add_three_copies function
def add_three_copies(data_list, data):
    # Add three copies of 'data' to 'data_list'
    data_list.append(data)
    data_list.append(data)
    data_list.append(data)

# Main program
# Get user input
message = input("Enter a message to copy: ")

# Initialize an empty list
my_list = []

# Print the list before calling the function
print("List before:", my_list)

# Call the function
add_three_copies(my_list, message)

# Print the list after calling the function
print("List after:", my_list)
