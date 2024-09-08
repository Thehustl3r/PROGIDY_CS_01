# Entry of our program
# Caesar cipher
from caesar_cipher import *

def main():
    result = ""
    text = ""

    while True:
        choice = int(input("What do you want to do? \n\t1. Choose 1 for encryption.\n\t2. Choose 2 for decryption.\n"))
        if choice == 1 or choice == 2:
            break
        print("Choose the correct option")

    if choice == 1:
        text = input("Write a text to be encrypted: ")
    else:
        text = input("Write a text to be decrypted: ")

    shift = int(input("Enter the shift number: "))

    # Call encryption or decryption function based on choice
    if choice == 1:
        result = caesar_encrypt(text, shift)
        print("The encrypted text is: ", result)
    else:
        result = caesar_decrypt(text, shift)
        print("The decrypted text is: ", result)

if __name__ == "__main__":
    main()
