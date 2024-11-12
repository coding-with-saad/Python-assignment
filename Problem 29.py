# Initialize an empty phonebook dictionary
phonebook = {}

# Function to add a contact
def add_contact(name, number):
    phonebook[name] = number
    print(f"Contact '{name}' added with number {number}.")

# Function to retrieve a contact
def get_contact(name):
    if name in phonebook:
        print(f"{name}'s number is {phonebook[name]}.")
    else:
        print(f"Contact '{name}' not found.")

# Function to display all contacts
def display_contacts():
    if phonebook:
        print("\nPhonebook Contacts:")
        for name, number in phonebook.items():
            print(f"{name}: {number}")
    else:
        print("The phonebook is empty.")

# Main loop to interact with the user
while True:
    print("\nOptions:")
    print("1 - Add a new contact")
    print("2 - Look up a contact")
    print("3 - Display all contacts")
    print("4 - Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        name = input("Enter the contact's name: ")
        number = input("Enter the contact's phone number: ")
        add_contact(name, number)
        
    elif choice == "2":
        name = input("Enter the name to look up: ")
        get_contact(name)
        
    elif choice == "3":
        display_contacts()
        
    elif choice == "4":
        print("Exiting the phonebook.")
        break
        
    else:
        print("Invalid option. Please try again.")
