def make_sentence(word, part_of_speech):
    if part_of_speech == 0:  # Noun
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:  # Verb
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:  # Adjective
        print(f"Looking out my window, the sky is big and {word}!")

def main():
    # Ask the user for a word
    word = input("Please type a noun, verb, or adjective: ")
    # Ask the user to specify the part of speech
    part_of_speech = int(input("Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: "))
    # Call make_sentence with the word and part_of_speech
    make_sentence(word, part_of_speech)

# Run the main function
if __name__ == "__main__":
    main()
