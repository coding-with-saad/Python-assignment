# Ask the user to enter a number
curr_value = int(input("Enter a number: "))

# Double the number and print each result until it reaches or exceeds 100
while curr_value < 1000:
    curr_value = curr_value * 2
    print(curr_value, end=" ")
