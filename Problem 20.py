# Function to get and print the last element of the list
def get_last_element(lst):
    # Print the last element in the list
    print("Last element:", lst[-1])

# Main program to prompt the user for list input
user_list = []
num_elements = int(input("How many elements do you want to add to the list? "))

# Collect elements from the user
for i in range(num_elements):
    element = input(f"Enter element {i + 1}: ")
    user_list.append(element)

# Call the function with the user's list
get_last_element(user_list)
