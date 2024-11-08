# Initialize an empty list to store the values
values = []

while True:
    # Prompt the user for input
    value = input("Enter a value: ")
    
    # Check if the input is empty (user pressed Enter without typing anything)
    # if value == "":
        # break  # Exit the loop if the input is empty
    
    # Add the value to the list
    values.append(value)

# Print the final list
print("Here's the list:", values)

