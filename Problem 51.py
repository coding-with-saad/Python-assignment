# Define the function that returns the number of fruits in stock
def num_in_stock(fruit):
    # For demonstration purposes, we define a dictionary of fruits in stock.
    stock = {
        "apple": 500,
        "banana": 300,
        "pear": 1000,
        "orange": 200,
        "mango": 0
    }
    # Return the number of fruits in stock or 0 if the fruit is not found
    return stock.get(fruit.lower(), 0)

def main():
    # Prompt the user to enter a fruit
    fruit = input("Enter a fruit: ").strip()
    
    # Get the number of fruits in stock for the entered fruit
    stock_count = num_in_stock(fruit)
    
    # Check if the fruit is in stock and print the appropriate message
    if stock_count > 0:
        print("This fruit is in stock! Here is how many:")
        print(stock_count)
    else:
        print("This fruit is not in stock.")

# Run the main function
if __name__ == "__main__":
    main()
