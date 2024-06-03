def caesar_cipher(text, shift, mode='encrypt'):
    result = []

    # Adjust shift for decryption mode
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            # Handle case separately
            offset = 65 if char.isupper() else 97
            # Perform the shift
            new_char = chr((ord(char) - offset + shift) % 26 + offset)
            result.append(new_char)
        else:
            # Preserve non-alphabetic characters
            result.append(char)

    return ''.join(result)

def main():
    print("Caesar Cipher Program")
    print("=====================")

    while True:
        # User input for mode
        mode = input("Would you like to (e)ncrypt or (d)ecrypt? ").strip().lower()
        if mode not in ['e', 'd']:
            print("Invalid mode. Please enter 'e' for encrypt or 'd' for decrypt.")
            continue

        # User input for message
        message = input("Enter your message: ").strip()

        # User input for shift value
        try:
            shift = int(input("Enter the shift value: ").strip())
        except ValueError:
            print("Invalid shift value. Please enter an integer.")
            continue

        # Determine the mode
        operation = 'encrypt' if mode == 'e' else 'decrypt'

        # Perform encryption/decryption
        result = caesar_cipher(message, shift, operation)
        print(f"The {operation}ed message is: {result}\n")

        # Option to exit
        another = input("Would you like to (c)ontinue or (q)uit? ").strip().lower()
        if another == 'q':
            break

if __name__ == "__main__":
    main()
