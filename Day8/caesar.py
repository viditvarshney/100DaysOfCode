import string
import logo

print(logo.logo)
alphabets = string.ascii_lowercase


def caesar(initial_text, key, cipher_direction):
    result = ""
    if direction.casefold() == 'decode':
        key = key * -1
    for i in text:
        ind = alphabets.index(i)
        temp_ind = ind + key
        if temp_ind < 0:
            new_ind = 26+temp_ind
        else:
            new_ind = temp_ind % 26
        result += alphabets[new_ind]
    print(f"The {direction}d tesxt is: {result}")


while True:
    while True:

        text = input("Type your message:\n").lower()
        key = int(input("Type the key number (this should be private): \n"))
        direction = input(
            "Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if direction.casefold() == 'encode' or direction.casefold() == 'decode':
            break
        else:
            print("Invalid option selected.")
    caesar(initial_text=text, key=key, cipher_direction=direction)
    if(input("Want to do more Encryption or Decryption: yes OR no: ").casefold() == 'no'):
        print("Happy Encryption.")
        break
