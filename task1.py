def caesar_cipher(text, shift, mode):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            encrypted_text += shifted_char
        else:
            encrypted_text += char

    return encrypted_text if mode == "encrypt" else caesar_cipher(encrypted_text, -shift, "encrypt")
def main():
    mode = input("Enter 'encrypt' or 'decrypt': ").lower()
    if mode not in ["encrypt", "decrypt"]:
        print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
        return

    text = input("Enter the text: ")
    shift = int(input("Enter the shift value (a positive number): "))

    if mode == "encrypt":
        encrypted_text = caesar_cipher(text, shift, mode)
        print("Encrypted text:", encrypted_text)
    else:
        decrypted_text = caesar_cipher(text, shift, mode)
        print("Decrypted text:", decrypted_text)


if __name__ == "__main__":
    main()