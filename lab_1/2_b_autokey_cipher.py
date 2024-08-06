"""
    Cipher: Autokey
"""

import string


PLAIN_TEXT = f"HELLO{string.ascii_letters}{string.digits}"

KEY = 100


def encrypt(key, plain_text):
    cipher = ""
    first_iteration = True

    for idx, character in enumerate(plain_text):
        if not first_iteration:
            key_char = plain_text[idx - 1]
            key = ord(key_char)
            if key_char in string.ascii_lowercase:
                key -= 97
            elif key_char in string.ascii_uppercase:
                key -= 65
            elif key_char in string.digits:
                key -= 48
            else:
                print(f"Invalid character in key: {key_char}")
                exit(0)
        first_iteration = False

        if character in string.ascii_lowercase:
            cipher += chr((ord(character) - 97 + key) % 26 + 97)
        elif character in string.ascii_uppercase:
            cipher += chr((ord(character) - 65 + key) % 26 + 65)
        elif character in string.digits:
            cipher += chr((ord(character) - 48 + key) % 10 + 48)

    return cipher


def decrypt(key, cipher_text):
    plain = ""
    first_iteration = True

    for idx, character in enumerate(cipher_text):
        if not first_iteration:
            key_char = plain[idx - 1]
            key = ord(key_char)
            if key_char in string.ascii_lowercase:
                key -= 97
            elif key_char in string.ascii_uppercase:
                key -= 65
            elif key_char in string.digits:
                key -= 48
            else:
                print(f"Invalid character in key: {key_char}")
                exit(0)
        first_iteration = False

        if character in string.ascii_lowercase:
            plain += chr((ord(character) - 97 - key) % 26 + 97)
        elif character in string.ascii_uppercase:
            plain += chr((ord(character) - 65 - key) % 26 + 65)
        elif character in string.digits:
            plain += chr((ord(character) - 48 - key) % 10 + 48)

    return plain


cipher_text = encrypt(KEY, PLAIN_TEXT)

print(f"Encrypted cipher text:\n{cipher_text}\n")

plain_text = decrypt(KEY, cipher_text)

print(f"Decrypted plain text:\n{plain_text}")
