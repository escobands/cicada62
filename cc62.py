# Cicada62 - Encoder / Decoder

# Import os for clearing the screen
import os

# The main character set (including space)
cicada62_set = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 '

# Manually define a predictable, fixed mapping for testing
# For example: each character maps to a unique number from 1 to 62
# Fun fact, original mapping was just 1-62
fixed_mapping = {
    'A': 37,  'B': 22,  'C': 42,  'D': 34,  'E': 20,  'F': 63,  'G': 58,  'H': 52,
    'I': 40,  'J': 31,  'K': 62,  'L': 32,  'M': 19,  'N': 24,  'O': 10,  'P': 17,
    'Q': 12,  'R': 21,  'S': 49,  'T': 47,  'U':  4,  'V': 30,  'W': 54,  'X':  5,
    'Y': 56,  'Z': 11,  'a': 53,  'b': 23,  'c': 45,  'd': 26,  'e': 25,  'f': 41,
    'g': 59,  'h': 29,  'i': 43,  'j': 27,  'k': 51,  'l': 13,  'm': 36,  'n': 46,
    'o': 39,  'p': 33,  'q': 57,  'r': 14,  's': 50,  't': 61,  'u':  3,  'v': 28,
    'w': 38,  'x':  6,  'y': 35,  'z': 55,  '0': 44,  '1':  7,  '2': 60,  '3':  9,
    '4': 15,  '5': 16,  '6': 18,  '7': 48,  '8':  2,  '9':  8,  ' ': 1
}


# Invert the mapping to make decoding easier
reverse_mapping = {v: k for k, v in fixed_mapping.items()}

# Clearing the screen
def clean_screen():
    # Check the OS
    if os.name == 'nt': # Windows
        os.system('cls')
    else: # For Linux or Mac
        os.system('clear')

# ASCII Function
def cicada62_menu_ascii():
    print("""
  .oooooo.    o8o                            .o8                .ooo     .oooo.   
 d8P'  `Y8b   `"'                           "888              .88'     .dP""Y88b  
888          oooo   .ooooo.   .oooo.    .oooo888   .oooo.    d88'            ]8P' 
888          `888  d88' `"Y8 `P  )88b  d88' `888  `P  )88b  d888P"Ybo.     .d8P'  
888           888  888        .oP"888  888   888   .oP"888  Y88[   ]88   .dP'     
`88b    ooo   888  888   .o8 d8(  888  888   888  d8(  888  `Y88   88P .oP     .o 
 `Y8bood8P'  o888o `Y8bod8P' `Y888""8o `Y8bod88P" `Y888""8o  `88bod8'  8888888888 """)

# The main menu
def cicada62_menu():
    clean_screen()
    print("================================")
    print("Cicada62tools")
    print("================================")
    print("[1] Encoder")
    print("[2] Decoder")
    print("[3] About Cicada62tools")
    print("[4] Break the program")

# Credits and thingies
def cicada62_credits():
    clean_screen()
    print("""
  .oooooo.    o8o                            .o8                .ooo     .oooo.   
 d8P'  `Y8b   `"'                           "888              .88'     .dP""Y88b  
888          oooo   .ooooo.   .oooo.    .oooo888   .oooo.    d88'            ]8P' 
888          `888  d88' `"Y8 `P  )88b  d88' `888  `P  )88b  d888P"Ybo.     .d8P'  
888           888  888        .oP"888  888   888   .oP"888  Y88[   ]88   .dP'     
`88b    ooo   888  888   .o8 d8(  888  888   888  d8(  888  `Y88   88P .oP     .o 
 `Y8bood8P'  o888o `Y8bod8P' `Y888""8o `Y8bod88P" `Y888""8o  `88bod8'  8888888888 """)
    print("Cicada62tools - Tool for encoding / decoding Cicada62 scheme")
    print("Made by Francisco Escobar")
    print("ASCII made with Patorjk's TAAG")
    # Pause for user input
    input("Press ENTER|RETURN to return to the menu")
    

# Encoding function
def cicada62_encoder(input_string, fixed_mapping):
    # Replace the spaces with '00' for encoding
    encoded_numbers = [str(fixed_mapping[char]) if char != ' ' else '1' for char in input_string]
    # Join the numbers into a single string which are separated by a dot
    encoded_str = '.'.join(encoded_numbers)
    return encoded_str

# Decoder function
def cicada62_decoder(encoded_str, reverse_mapping):
    # Split the encoded string into a list of numbers (assuming they are separated by '.')
    encoded_numbers = encoded_str.split('.')
    # Map the number back to its corresponding character using the reverse mapping
    decoded_str = ''.join([reverse_mapping[int(num)] if num != '1' else ' ' for num in encoded_numbers])
    return decoded_str
 
# Main function
def main():
    cicada62_menu_ascii()

    while True:
        cicada62_menu()
        choice = input("[?]")

        if choice == '1':
            message = input("Please type in the specified phrase. ")
            encoded = cicada62_encoder(message, fixed_mapping) # So it doesn't bug out
            print(f"Cicada62/encoder > {encoded}")
            input("Press ENTER|RETURN to return to the menu")

        elif choice == '2':
            encoded_message = input("Please type in the correct message. ")
            decoded = cicada62_decoder(encoded_message, reverse_mapping) # Passing reverse_mapping
            print(f"Cicada62/decoder > {decoded}")
            input("Press ENTER|RETURN to return to the menu")

        elif choice == '3':
            cicada62_credits()

        elif choice == '4':
            print("See you next time!")
            break

        else:
            print("Not a real option.")

# Run it up
if __name__ == "__main__":
    main()