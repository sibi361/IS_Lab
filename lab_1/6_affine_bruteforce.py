"""
    Cipher: Affine
"""

PLAIN_TEXT = "AB"

CIPHER_TEXT = "GL"

import string


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


def bruteforce_affine_cipher(plain_text, cipher_text):
    for key1 in range(1, 26, 2):
        for key2 in range(0, 26, 1):
            if encrypt(key1, key2, plain_text) == cipher_text:
                return key1, key2

    return False, False


key_bruteforced_1, key_bruteforced_2 = bruteforce_affine_cipher(PLAIN_TEXT, CIPHER_TEXT)

if not key_bruteforced_1:
    print("Bruteforce attack failed")
else:
    print(f"Key 1: {key_bruteforced_1} | Key 2: {key_bruteforced_2}")
