# Function to convert feet to inches
def feet_to_inches(feet):
    return feet * 12

# Prompt the user for input in feet
feet = float(input("Enter the number of feet: "))

# Calculate the equivalent inches
inches = feet_to_inches(feet)

# Determine singular or plural for feet
unit = "foot" if feet == 1 else "feet"

# Output the result
print(f"{feet} {unit} is equal to {inches} inches.")













feet = float(input("Enter length in feet: "))
inches = feet * 12
print(f"{feet} feet is equal to {inches} inches.")