# Dictionary to store the count of each number
count_dict = {}

# Loop to get user input until the user decides to stop
while True:
    number = input("Enter a number (or type 'done' to finish): ")
    if number.lower() == 'done':  # Exit condition
        break
    number = int(number)  # Convert the input to an integer
    
    # Update the count for the entered number
    if number in count_dict:
        count_dict[number] += 1
    else:
        count_dict[number] = 1

# Print the count for each number
for number, count in count_dict.items():
    print(f"{number} appears {count} time(s).")
