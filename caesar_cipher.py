def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                shifted = (ord(char) - base + shift) % 26 + base
            elif mode == 'decrypt':
                shifted = (ord(char) - base - shift) % 26 + base
            result += chr(shifted)
        else:
            result += char  # keep spaces, punctuation, etc.
    
    return result


def main():
    print("=== Caesar Cipher ===")
    message = input("Enter your message: ")
    
    while True:
        try:
            shift = int(input("Enter shift value (0-25): "))
            if 0 <= shift <= 25:
                break
            else:
                print("Shift must be between 0 and 25.")
        except ValueError:
            print("Please enter a valid integer.")
    
    mode = ""
    while mode not in ["encrypt", "decrypt"]:
        mode = input("Do you want to 'encrypt' or 'decrypt' the message? ").lower()

    result = caesar_cipher(message, shift, mode)
    print(f"\nResult ({mode}ed message): {result}")


if __name__ == "__main__":
    main()
