"""
    Cipher: Affine
"""

import string


PLAIN_TEXT = f"hi my name is Karan 123 {string.ascii_letters}{string.digits}"

KEY = 17
KEY_2 = 5


def encrypt(key, key2, plain_text):
    cipher = ""

    for character in plain_text:
        if character in string.ascii_lowercase:
            cipher += chr((((ord(character) - 97) * key) % 26) + key2 + 97)
        elif character in string.ascii_uppercase:
            cipher += chr((((ord(character) - 65) * key) % 26) + key2 + 65)
        elif character in string.digits:
            cipher += chr((((ord(character) - 48) * key) % 10) + key2 + 48)
        else:
            cipher += character

    return cipher


def decrypt(key, key2, cipher_text):
    plain = ""

    modular_multiplicative_inverse = pow(key, -1, 26)

    for character in cipher_text:
        if character in string.ascii_lowercase:
            plain += chr(
                (ord(character) - 97 - key2) * modular_multiplicative_inverse % 26 + 97
            )
        elif character in string.ascii_uppercase:
            plain += chr(
                (ord(character) - 65 - key2) * modular_multiplicative_inverse % 26 + 65
            )
        elif character in string.digits:
            plain += chr(
                (ord(character) - 48 - key2) * modular_multiplicative_inverse % 10 + 48
            )
        else:
            plain += character

    return plain


cipher_text = encrypt(KEY, KEY_2, PLAIN_TEXT)

print(f"Encrypted cipher text:\n{cipher_text}\n")

plain_text = decrypt(KEY, KEY_2, cipher_text)

print(f"Decrypted plain text:\n{plain_text}")
