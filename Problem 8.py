# Speed of light in meters per second
c = 3 * 10**8

while True:
    # Prompt the user for mass input
    mass = input("Enter mass in kilograms (or type 'exit' to quit): ")
    
    # Check if the user wants to exit
    if mass.lower() == "exit":
        break
    
    # Convert the mass to a number and calculate energy
    mass = float(mass)
    energy = mass * c**2
    
    # Output the result
    print(f"The equivalent energy is: {energy} joules")

