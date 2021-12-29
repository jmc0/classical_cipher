"""
Caesar cipher.
"""

import argparse
from utils import count_letter_percentage, get_single_key_and_mutual_ic
from utils import IDX_TO_CHAR, CHAR_TO_IDX, LENGTH_OF_ALPHABET, ALPHABET


def caesar_encode(plaintext: str, key: int) -> str:
    key %= LENGTH_OF_ALPHABET
    ciphertext = ''
    for c in plaintext:
        upper = 0
        if c in ALPHABET:
            if c.isupper():
                upper = 1
                c = c.lower()
            c = IDX_TO_CHAR[(CHAR_TO_IDX[c] + key) % LENGTH_OF_ALPHABET]
            if upper:
                c = c.upper()
            ciphertext += c
        else:
            ciphertext += c
    return ciphertext


def caesar_decode(ciphertext: str, key: int = None) -> str:
    if not key:
        letter_and_per_sorted = count_letter_percentage(ciphertext)
        key, best_mutual_ic = get_single_key_and_mutual_ic(letter_and_per_sorted)
        print("The possible key is: %d." % (key))
    else:
        key %= LENGTH_OF_ALPHABET
    plaintext = ''
    for c in ciphertext:
        upper = 0
        if c in ALPHABET:
            if c.isupper():
                c = c.lower()
                upper = 1
            p = IDX_TO_CHAR[(CHAR_TO_IDX[c] - key) % LENGTH_OF_ALPHABET]
            if upper:
                p = p.upper()
            plaintext += p
        else:
            plaintext += c
    return plaintext


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--plaintext', type=str, default='', help='Plaintext')
    parser.add_argument('-c', '--ciphertext', type=str, default='', help='Caesar Cipher')
    parser.add_argument('-k', '--key', type=int, default=None, help='key to decode the cipher')
    args = parser.parse_args()
    if args.plaintext:
        if args.key:
            print("The plaintext is: \"%s\"." % args.plaintext)
            print("The key is: %d." % args.key)
            ciphertext = caesar_encode(args.plaintext, args.key)
            print("The ciphertext is : \"%s\"." % ciphertext)
    if args.ciphertext:    
        print("The ciphertext is: \"%s\"." % args.ciphertext)
        if args.key:
            print('The key is: %d.' % args.key)
        plaintext = caesar_decode(args.ciphertext, args.key)
        print("The plaintext is: \"%s\"." % plaintext)
