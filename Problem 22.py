MAX_LENGTH = 3

def shorten(lst):
    # Remove elements from the end until lst is MAX_LENGTH items long
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()  # Remove the last item
        print("Removed:", removed_item)  # Print the removed item

# Main function to get the list from the user and call shorten
def main():
    user_list = []
    num_elements = int(input("How many elements do you want to add to the list? "))

    for i in range(num_elements):
        element = input(f"Enter element {i + 1}: ")
        user_list.append(element)

    print("Original list:", user_list)
    shorten(user_list)
    print("Shortened list:", user_list)

# Run the main function
main()
