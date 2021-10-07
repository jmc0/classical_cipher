#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright ©  2021-10-05 00:09 bucktoothsir <rsliu.xd@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Decode Caesar cipher.
"""

import argparse
from utils import count_letter_percentage, get_single_key_and_mutual_ic
from utils import IDX_TO_CHAR, CHAR_TO_IDX, LENGTH_OF_ALPHABET, ALPHABET


def caecar_decode(ciphertext, key=None):
    if not key:
        letter_and_per_sorted = count_letter_percentage(ciphertext)
        key, best_mutual_ic = get_single_key_and_mutual_ic(letter_and_per_sorted)
        print("The possible key is %d" % (key))
    else:
        if key < 0 or key > 25:
            raise ValueError('the key should >= 0 and <= 26')
        print("The input key is %d" % key)
    plaintext = ''
    for c in ciphertext:
        if c.lower() in ALPHABET:
            plaintext += IDX_TO_CHAR[(CHAR_TO_IDX[c.lower()] - key) % LENGTH_OF_ALPHABET]
        else:
            plaintext += c
    return plaintext


def test():
    print("Running the test example")
    ciphertext = 'WLSJNIALUJBS JLCIL NI NBY GIXYLH UAY QUM YZZYWNCPYFS MSHIHSGIOM QCNB YHWLSJNCIH, NBY WIHPYLMCIH IZ CHZILGUNCIH ZLIG U LYUXUVFY MNUNY NI UJJULYHN HIHMYHMY.'
    print("The ciphertext is %s" % ciphertext)
    plaintext = caecar_decode(ciphertext)
    print("The plaintext is %s" % plaintext)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--ciphertext', type=str, default='', help='Caesar Cipher')
    parser.add_argument('--key', type=int, default=None, help='key to decode the cipher')
    parser.add_argument('--test', action='store_true', help='if run the test example')
    args = parser.parse_args()
    if args.test:
        test()
    else:
        print("The ciphertext is %s" % args.ciphertext)
        plaintext = caecar_decode(args.ciphertext, args.key)
        print("The plaintext is %s" % plaintext)
