alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

is_out = "no"
shift_number = int(input("Firstly, give encryption rate (except 0): "))
array_size_controller = []

def encrypt():
    secret_message = input("\nType your secret message: ").lower()
    encrypted_message = ""

    for letter in secret_message:
        current_index = alphabet.index(letter)
        shifted_index = current_index + shift_number
        if shifted_index > 25:
            shifted_index = shifted_index - 25
        encrypted_message += alphabet[shifted_index]

    return encrypted_message

def decrypt(shift_number):
    encrypted_input = input("\nEnter your encrypted message: ").lower()
    decrypted_message = ""
    
    for letter in encrypted_input:
        current_index = alphabet.index(letter)
        shifted_index = current_index - shift_number
        if shifted_index < 0:
            shifted_index = current_index - shift_number - 1
        decrypted_message += alphabet[shifted_index]

    return decrypted_message

while is_out == "no":
    user_choice = input("\n\nType 'encode' to encrypt or Type 'decode' to decrypt: ").lower()

    if user_choice == "encode":
        encrypted_message = encrypt()
        print(f"Your secret message is encrypted into: {encrypted_message}")
    elif user_choice == "decode":
        decrypted_message = decrypt(shift_number)
        print(f"The real message is: {decrypted_message}")
    else:
        print("You typed wrong! Try again...")

    is_out = input("Do you want to exit from the program (yes/no): ")


print("\n\n**You exited from the program!**\nBye bye...")


