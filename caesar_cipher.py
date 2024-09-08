# Function to encrypt the plaintext
def caesar_encrypt(plaintext, shift):
    result = ""
    
    # Traverse through each character in the plaintext
    for char in plaintext:
        # Encrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # If it's not a letter, leave it unchanged
            result += char
    
    return result

# Function to decrypt the ciphertext
def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)
