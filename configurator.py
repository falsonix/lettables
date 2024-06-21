# Written by Falsonix on 6/21/2024

# List of allowed characters, make sure that the requested string does not contain any of these
allowed_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-+=[]{}/\\|,.<>;:'\""

def count_individual_characters(phrase):
    # Convert the phrase to uppercase to match the allowed characters
    phrase = phrase.upper()
    
    # Initialize a dictionary to count each character
    char_count = {char: 0 for char in allowed_chars}
    
    # Iterate through each character in the phrase
    for char in phrase:
        if char in char_count:
            char_count[char] += 1
        else:
            print(f"(ruh roh) Ignoring character: {char}")  # Debugging statement to show ignored characters
    
    return char_count

def count_characters(phrase):
    # Initialize a dictionary to count each character in the provided string
    char_count = {char: 0 for char in allowed_chars}
    
    # Convert the phrase to uppercase to match the allowed characters, Python doesn't like counting lowercase letters for some reason
    phrase = phrase.upper()

    # Initialize a variable to store the total number of characters in the phrase, excluding spaces
    total_chars = 0

    # Iterate through each character in the phrase
    for char in phrase:
        if char in char_count:
            total_chars += 1  # Increment total character count for later :)
    return total_chars

# Ask the user for their desired phrase
user_input = input("Please input the phrase that you wish to print: ")

# Print the user's input for debugging purposes (and maybe quality of life but idk lol)
print(f"You entered: {user_input}.")

# Count the individual characters
character_count = count_individual_characters(user_input)

# Count the total characters
total_characters = count_characters(user_input)

# Print the results
print("You'll need to print out this amount of letters in order to assemble your phrase:")
for char, count in character_count.items():
    if count > 0:
        print(f"{char}: {count}")

# Print the total number of letters in the phrase, ignoring spaces
print(f"Total characters (excluding spaces): {total_characters}")

# Wait for the user to hit the enter key before closing the Python window
input("Press enter to continue.....")