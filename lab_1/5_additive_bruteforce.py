"""
    Cipher: Additive
"""

PLAIN_TEXT_1 = "YES"

CIPHER_TEXT_1 = "CIW"

CIPHER_TEXT_2 = "XVIEWYWI"


import string


def encrypt(key, plain_text):
    cipher = ""

    for character in plain_text:
        if character in string.ascii_lowercase:
            cipher += chr((ord(character) - 97 + key) % 26 + 97)
        elif character in string.ascii_uppercase:
            cipher += chr((ord(character) - 65 + key) % 26 + 65)
        elif character in string.digits:
            cipher += chr((ord(character) - 48 + key) % 10 + 48)
        else:
            cipher += character

    return cipher


def decrypt(key, cipher_text):
    plain = ""

    for character in cipher_text:
        if character in string.ascii_lowercase:
            plain += chr((ord(character) - 97 - key) % 26 + 97)
        elif character in string.ascii_uppercase:
            plain += chr((ord(character) - 65 - key) % 26 + 65)
        elif character in string.digits:
            plain += chr((ord(character) - 48 - key) % 10 + 48)
        else:
            plain += character

    return plain


def bruteforce_additive_cipher(plain_text, cipher_text):
    for key in range(26):
        if encrypt(key, plain_text) == cipher_text:
            return key

    return False


key_bruteforced = bruteforce_additive_cipher(PLAIN_TEXT_1, CIPHER_TEXT_1)

if not key_bruteforced:
    print("Bruteforce attack failed")
else:
    print(f"Key: {key_bruteforced}")

plain_text_2 = decrypt(key_bruteforced, CIPHER_TEXT_2)

print(f"{CIPHER_TEXT_2} -> {plain_text_2}")
