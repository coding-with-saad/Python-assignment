def print_even_odd(start, end):
    for num in range(start, end + 1):  # Loop from start to end (inclusive)
        if num % 2 == 0:
            print(f"{num} even", end=" ")
        else:
            print(f"{num} odd", end=" ")

# Call the function with the desired range
print_even_odd(1, 19)
