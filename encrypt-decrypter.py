alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

is_out = "no"
shift_number = 0

def encrypt():
    secret_message = input("Type your secret message: ").lower()
    shift_number = int(input("Give encryption rate (except 0): "))
    encrypted_message = ""

    for letter in secret_message:
        current_index = alphabet.index(letter)
        shifted_index = current_index + shift_number
        encrypted_message += alphabet[shifted_index]

    return encrypted_message

def decrypt():
    encrypted_input = input("Enter your encrypted message: ").lower()
    decrypted_message = ""
    print(f"The shift number is {shift_number}")
    for letter in encrypted_input:
        current_index = alphabet.index(letter)
        shifted_index = current_index - shift_number
        decrypted_message += alphabet[shifted_index]

    return decrypted_message

while is_out == "no":
    user_choice = input("Type 'encode' to encrypt or Type 'decode' to decrypt: ").lower()

    if user_choice == "encode":
        encrypted_message = encrypt()
        print(f"Your secret message is encrypted into: {encrypted_message}")
    elif user_choice == "decode":
        decrypted_message = decrypt()
        print(f"The real message is: {decrypted_message}")
    else:
        print("You typed wrong! Try again...")

    is_out = input("Do you want to exit from the program (yes/no): ")


print("\nYou exited from the program!\nBye bye...")


