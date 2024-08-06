"""
    Cipher: Multiplicative
"""

import string


PLAIN_TEXT = f"hi my name is Karan 123 {string.ascii_letters}{string.digits}"

KEY = 2


def encrypt(key, plain_text):
    cipher = ""

    for character in plain_text:
        if character in string.ascii_lowercase:
            cipher += chr((ord(character) - 97 + key) % 26 + 97)
            # print(character, ord(character) - 97, ord(cipher[-1]) - 97)
        elif character in string.ascii_uppercase:
            cipher += chr((ord(character) - 65 + key) % 26 + 65)
            # print(character, ord(character) - 65, ord(cipher[-1]) - 65)
        elif character in string.digits:
            cipher += chr((ord(character) - 48 + key) % 10 + 48)
            # print(character, ord(character) - 48, ord(cipher[-1]) - 48)
        else:
            cipher += character
            # print(character, ord(character), ord(cipher[-1]))

    return cipher


def decrypt(key, cipher_text):
    plain = ""

    for character in cipher_text:
        if character in string.ascii_lowercase:
            plain += chr((ord(character) - 97 - key) % 26 + 97)
            # print(character, ord(character) - 97, ord(plain[-1]) - 97)
        elif character in string.ascii_uppercase:
            plain += chr((ord(character) - 65 - key) % 26 + 65)
            # print(character, ord(character) - 65, ord(plain[-1]) - 65)
        elif character in string.digits:
            plain += chr((ord(character) - 48 - key) % 10 + 48)
            # print(character, ord(character) - 48, ord(plain[-1]) - 48)
        else:
            plain += character
            # print(character, ord(character), ord(plain[-1]))

    return plain


cipher_text = encrypt(KEY, PLAIN_TEXT)

print(f"Encrypted cipher text:\n{cipher_text}\n")

plain_text = decrypt(KEY, cipher_text)

print(f"Decrypted plain text:\n{plain_text}")
