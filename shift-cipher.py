#!/usr/bin/python3

import sys


def shift_cipher(message, shift):
    output = ''
    encrypted_letter = ''
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                 'y', 'z']

    for letter in message:
        if letter in uppercase:
            index = uppercase.index(letter)
            encrypted_index = (index + shift) % 26
            encrypted_letter = uppercase[encrypted_index]
            output += encrypted_letter
        elif letter in lowercase:
            index = lowercase.index(letter)
            encrypted_index = (index + shift) % 26
            encrypted_letter = lowercase[encrypted_index]
            output += encrypted_letter
    return output


if __name__ == '__main__':

    print("Shift Encryption/Decryption Tool\n")
    i = 0
    while (i == 0):
        encrypt_decrypt = input("Enter 1 for encryption, 2 for decryption or" +
                                " q to quit:\n")
        if (encrypt_decrypt == '1'):
            message = input("Type your plain text message:\n")
            encrypted_message = shift_cipher(message, 3)
            print("Your encrypted message is:\n")
            print(encrypted_message)
            i == 1
        elif(encrypt_decrypt == '2'):
            message = input("Type your encrypted message:\n")
            decrypted_message = shift_cipher(message, 26-3)
            print("Your decrypted message is:\n")
            print(decrypted_message)
            i == 1
        elif(encrypt_decrypt == 'q'):
            sys.exit("Quitting...")
        else:
            print("Incorrect input. Please try again.")
