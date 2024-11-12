# Constant for the maximum value in the sequence
MAX_VALUE = 10000

# Initialize the first two terms of the Fibonacci sequence
a, b = 0, 1

# Print Fibonacci terms as long as they are less than MAX_VALUE
while a < MAX_VALUE:
    print(a, end=" ")
    # Update terms for the next step in the sequence
    a, b = b, a + b
