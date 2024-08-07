"""
    Cipher: Affine
"""

import string
PLAIN_TEXT = "AB"

CIPHER_TEXT = "GL"

CIPHER_TEXT_2 = "XPALASXYFGFUKPXUSOGEUTKCDGEXANMGNVS"


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
                (ord(character) - 97 - key2) *
                modular_multiplicative_inverse % 26 + 97
            )
        elif character in string.ascii_uppercase:
            plain += chr(
                (ord(character) - 65 - key2) *
                modular_multiplicative_inverse % 26 + 65
            )
        elif character in string.digits:
            plain += chr(
                (ord(character) - 48 - key2) *
                modular_multiplicative_inverse % 10 + 48
            )
        else:
            plain += character

    return plain


def bruteforce_affine_cipher(plain_text, cipher_text):
    for key1 in range(1, 26, 2):
        for key2 in range(0, 26, 1):
            if encrypt(key1, key2, plain_text) == cipher_text:
                return key1, key2

    return False, False


key_bruteforced_1, key_bruteforced_2 = bruteforce_affine_cipher(
    PLAIN_TEXT, CIPHER_TEXT)

if not key_bruteforced_1:
    print("Bruteforce attack failed")
else:
    print(f"Key 1: {key_bruteforced_1} | Key 2: {key_bruteforced_2}")

    plain_text = decrypt(key_bruteforced_1, key_bruteforced_2, CIPHER_TEXT_2)

    print(f"Decrypted plain text:\n{plain_text}")
