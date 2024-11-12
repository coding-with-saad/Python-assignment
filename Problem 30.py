# Fruit prices in a dictionary
fruit_prices = {
    "apple": 3.0,
    "durian": 25.0,
    "jackfruit": 15.0,
    "kiwi": 2.5,
    "rambutan": 4.0,
    "mango": 8.0
}

total_cost = 0.0

# Loop through each fruit in the dictionary
for fruit, price in fruit_prices.items():
    # Ask the user how many of each fruit they want
    quantity = int(input(f"How many ({fruit}) do you want?: "))
    
    # Calculate cost for the current fruit and add to the total cost
    total_cost += quantity * price

# Print the total combined cost
print(f"Your total is ${total_cost}")
