"""
    Cipher: Playfair
"""

import string
import random

PADDING_CHARACTER = "X"

IGNORED_CHARACTER = "I"
IGNORED_CHARACTER_REPLACEMENT = "J"

# PLAIN_TEXT = f"HELLO{string.ascii_uppercase}"
PLAIN_TEXT = "Thekeyishiddenunderthedoorpad".upper()

# key = [list("LGDBA"), list("QMHEC"), list(
#     "URNJF"), list("XVSOK"), list("ZYWTP")]


def generate_key():
    key_charset = list(string.ascii_uppercase)
    key_charset.remove(IGNORED_CHARACTER)

    key = ""
    while len(key) < 25:
        temp = ""

        while temp in key:
            temp = random.choice(key_charset)

        key += temp

    key_matrix = [[key[i * 5 + j] for j in range(5)] for i in range(5)]

    return key_matrix


def print_key(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print(f"KEY:\n{'\n'.join(table)}")
    print()


def fix_consecutive_repetitions_in_plain_text(plain_text):
    plain_text_post_ignored_char_removal = plain_text.replace(IGNORED_CHARACTER.lower(), IGNORED_CHARACTER_REPLACEMENT.lower(
    )).replace(IGNORED_CHARACTER.upper(), IGNORED_CHARACTER_REPLACEMENT.upper())

    chars = list(plain_text_post_ignored_char_removal)

    for idx, char in enumerate(chars):
        try:
            if chars[idx + 1] == char:
                chars.insert(idx + 1, PADDING_CHARACTER)
        except IndexError:
            break

    plain_text_new = "".join(chars)

    if len(plain_text_new) % 2:
        plain_text_new += PADDING_CHARACTER

    return plain_text_new


def encrypt(key, plain_text_fixed):
    cipher = ""

    for idx in range(0, len(plain_text_fixed), 2):

        row_idx = []
        col_idx = []

        for character in plain_text_fixed[idx: idx + 2]:
            found = False

            for i, row in enumerate(key):
                for j, key_char in enumerate(row):
                    if key_char == character:
                        # print(f"row: {i} | col: {j} | {key_char}")
                        row_idx.append(i)
                        col_idx.append(j)
                        found = True
                        break
                if found:
                    break

        # print(row_idx, col_idx)

        if row_idx[0] == row_idx[1]:
            # print("Same row")
            cipher += key[(row_idx[0]) % 5][(col_idx[0] + 1) % 5]
            cipher += key[(row_idx[0]) % 5][(col_idx[1] + 1) % 5]
        elif col_idx[0] == col_idx[1]:
            # print("Same column")
            cipher += key[(row_idx[0] + 1) % 5][(col_idx[0]) % 5]
            cipher += key[(row_idx[1] + 1) % 5][(col_idx[0]) % 5]
        else:
            # print("Not in same row/column")
            cipher += key[(row_idx[0]) % 5][(col_idx[1]) % 5]
            cipher += key[(row_idx[1]) % 5][(col_idx[0]) % 5]

        # print()

    return cipher


def decrypt(key, cipher_text):
    cipher = ""

    for idx in range(0, len(cipher_text), 2):

        row_idx = []
        col_idx = []

        for character in cipher_text[idx: idx + 2]:
            found = False

            for i, row in enumerate(key):
                for j, key_char in enumerate(row):
                    if key_char == character:
                        # print(f"row: {i} | col: {j} | {key_char}")
                        row_idx.append(i)
                        col_idx.append(j)
                        found = True
                        break
                if found:
                    break

        if row_idx[0] == row_idx[1]:
            # print("Same row")
            cipher += key[(row_idx[0]) % 5][(col_idx[0] - 1) % 5]
            cipher += key[(row_idx[0]) % 5][(col_idx[1] - 1) % 5]
        elif col_idx[0] == col_idx[1]:
            # print("Same column")
            cipher += key[(row_idx[0] - 1) % 5][(col_idx[0]) % 5]
            cipher += key[(row_idx[1] - 1) % 5][(col_idx[0]) % 5]
        else:
            # print("Not in same row/column")
            cipher += key[(row_idx[0]) % 5][(col_idx[1]) % 5]
            cipher += key[(row_idx[1]) % 5][(col_idx[0]) % 5]

        # print()

    return cipher


# key = generate_key()


key = [list("GUJDA"), list("NCEBF"), list(
    "HKLMO"), list("PQRST"), list("VWXYZ")]

print_key(key)

plain_text_fixed = fix_consecutive_repetitions_in_plain_text(PLAIN_TEXT)

print(f"plain_text_fixed: {plain_text_fixed}\n")

cipher_text = encrypt(key, plain_text_fixed)

print(f"Encrypted cipher text:\n{cipher_text}\n")

plain_text = decrypt(key, cipher_text)

print(f"Decrypted plain text:\n{plain_text}")
