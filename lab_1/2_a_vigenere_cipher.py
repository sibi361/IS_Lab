"""
    Cipher: Vigenere
"""

import string


PLAIN_TEXT = f"hi my name is Karan 123 {string.ascii_letters}{string.digits}"

KEY = "pascal"


def extend_key(key, plain_text):
    while len(key) < len(plain_text):
        key += key
    return key[:len(plain_text)]


def encrypt(key, plain_text):
    key_wrapped = extend_key(key, plain_text)
    cipher = ""

    for idx, character in enumerate(plain_text):
        key_char = key_wrapped[idx]
        key_char_ascii = ord(key_char)
        if key_char in string.ascii_lowercase:
            key_char_ascii -= 97
        elif character in string.ascii_uppercase:
            key_char_ascii -= 65
        elif character in string.digits:
            key_char_ascii -= 48
        else:
            print(f"Invalid character in key: {key_char}")
            exit(0)

        if character in string.ascii_lowercase:
            cipher += chr((ord(character) - 97 + key_char_ascii) % 26 + 97)
        elif character in string.ascii_uppercase:
            cipher += chr((ord(character) - 65 + key_char_ascii) % 26 + 65)
        elif character in string.digits:
            cipher += chr((ord(character) - 48 + key_char_ascii) % 10 + 48)
        else:
            cipher += character

    return cipher


def decrypt(key, cipher_text):
    key_wrapped = extend_key(key, PLAIN_TEXT)
    plain = ""

    for idx, character in enumerate(cipher_text):
        key_char = key_wrapped[idx]
        key_char_ascii = ord(key_char)
        if key_char in string.ascii_lowercase:
            key_char_ascii -= 97
        elif character in string.ascii_uppercase:
            key_char_ascii -= 65
        elif character in string.digits:
            key_char_ascii -= 48
        else:
            print(f"Invalid character in key: {key_char}")
            exit(0)

        if character in string.ascii_lowercase:
            plain += chr((ord(character) - 97 - key_char_ascii) % 26 + 97)
        elif character in string.ascii_uppercase:
            plain += chr((ord(character) - 65 - key_char_ascii) % 26 + 65)
        elif character in string.digits:
            plain += chr((ord(character) - 48 - key_char_ascii) % 10 + 48)
        else:
            plain += character

    return plain


cipher_text = encrypt(KEY, PLAIN_TEXT)

print(f"Encrypted cipher text:\n{cipher_text}\n")

plain_text = decrypt(KEY, cipher_text)

print(f"Decrypted plain text:\n{plain_text}")
