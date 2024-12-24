letters = "abcdefghijklmnopqrstuvwxyz"
num_letters = len(letters)

def encrypt_decrypt(text, mode, key):
    result = ""
    if mode == "d":
        key = -key

    for letter in text:
        lower_letter = letter.lower()
        if lower_letter in letters:
            index = letters.find(lower_letter)
            new_index = index + key
            if new_index >= num_letters:
                new_index -= num_letters
            elif new_index < 0:
                new_index += num_letters
            result += letters[new_index]
        else:
            result += letter
    return result

print("Caesar Cipher Program")
print()

user_input = input("Do you want to encrypt or decrypt? (e/d): ").lower()
print()

if user_input == "e":
    print("Encryption mode selected.")
    key = int(input("Enter the key (1 through 26): "))
    plaintext = input("Enter the text to encrypt: ")
    ciphertext = encrypt_decrypt(plaintext, "e", key)
    print(f"Ciphertext: {ciphertext}")

elif user_input == "d":
    print("Decryption mode selected.")
    key = int(input("Enter the key (1 through 26): "))
    ciphertext = input("Enter the text to decrypt: ")
    plaintext = encrypt_decrypt(ciphertext, "d", key)
    print(f"Plaintext: {plaintext}")

else:
    print("Invalid option. Please select 'e' to encrypt or 'd' to decrypt.")
