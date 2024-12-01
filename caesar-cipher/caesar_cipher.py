import os

# Get user input for the word, character list, and shift amount
def get_input():
    word = input("Enter your word: ")  # Input the word to encode/decode
    word_list = list("abcdefghijklmnopqrstuvwxyz")# Alphabet list used for shifting
    while True:
        try:
            shift_amount = int(input("Enter shift amount: "))
            break# Number of positions to shift
        except ValueError:
            print("Please Enter a valid value!")
    return word, word_list, shift_amount

# Encode the word using a Caesar cipher
def encode(word, word_list, shift_amount):
    for i in range(len(word)):  # Iterate through each character in the word
        if word[i] == ' ':  # If the character is a space, keep it as is
            print(' ', end='')
        else:
            # Find the new position of the letter after shifting
            letter_index = word_list.index(word[i])
            final_index = (letter_index + shift_amount) % len(word_list)
            print(word_list[final_index], end='')  # Print the shifted letter

# Decode the word using a Caesar cipher
def decode(word, word_list, shift_amount):
    for i in range(len(word)):  # Iterate through each character in the word
        if word[i] == ' ':  # If the character is a space, keep it as is
            print(' ', end='')
        else:
            # Find the original position of the letter before shifting
            letter_index = word_list.index(word[i])
            final_index = (letter_index - shift_amount) % len(word_list)
            print(word_list[final_index], end='')  # Print the shifted-back letter

# Display the program logo
def logo():
    print("""           
     ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
    a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
    8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
    "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
     `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
                88             88                                 
               ""             88                                 
                              88                                 
     ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
    a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
    8b         88 88       d8 88       88 8PP""""""" 88          
    "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
     `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                  88                                             
                  88           
    """)

# Main function to run the program
def main():
    logo()  # Display the program logo
    print("######################## ENCODE / DECODE ########################\n")
    
    # Get input data from the user
    word, word_list, shift_amount = get_input()
    
    # Ask the user whether they want to encode or decode
    while True:
        try:
            encode_or_decode = input("Would you like to encode or decode? (e/d): ").lower()
            break
        except ValueError:
            print("Please enter a valid value!")

    # Perform the chosen operation
    if encode_or_decode == 'e':
        print("\nHere is your result:")
        encode(word, word_list, shift_amount)
    elif encode_or_decode == 'd':
        print("\nHere is your result:")
        decode(word, word_list, shift_amount)
    else:
        print("Invalid choice. Please select 'e' for encode or 'd' for decode.")

# Keep the program running in a loop for repeated use
while True:
    main()  # Call the main function
    print("\n")
    input("Press any key to continue...")  # Wait for user input before clearing the screen
    os.system("cls")  # Clear the console (works on Windows)
