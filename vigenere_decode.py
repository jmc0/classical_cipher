#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright ©  2021-10-05 22:51 bucktoothsir <rsliu.xd@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Decode Vigenere Cipher
"""

import argparse

from utils import IC_OF_ENGLISH_VIGENERE_GROUP, IDX_TO_CHAR, LENGTH_OF_ALPHABET, ALPHABET, CHAR_TO_IDX
from utils import Friedman, count_letter_percentage, get_single_key_and_mutual_ic

def vigenere_decode(ciphertext, key=None, key_len=None):
    all_plaintext = []
    if not key:
        if not key_length:
            key_len_list = Friedman(ciphertext)
        else:
            key_len_list = [key_len]
        for key_len in key_len_list:
            best_key_char = ''
            best_key_num_list = []
            cipher_group = get_group_of_cipher(ciphertext, key_len)
            average_ic = 0
            for g in cipher_group:
                letter_and_per_sorted = count_letter_percentage(g)
                single_key, best_mutual_ic = get_single_key_and_mutual_ic(letter_and_per_sorted)
                best_key_num_list.append(single_key)
                best_key_char += IDX_TO_CHAR[single_key]
                average_ic += best_mutual_ic
            average_ic /= len(cipher_group)
            if average_ic > IC_OF_ENGLISH_VIGENERE_GROUP: 
                if not key_len:
                    print('For possible %d length key, the best key is %s' % (key_len, best_key_char))
                else:
                    print('For input %d length key, the best key is %s' % (key_len, best_key_char))
            idx = 0
            for c in ciphertext:
                if c.lower() in ALPHABET:
                    plaintext += IDX_TO_CHAR[(CHAR_TO_IDX[c.lower()] - best_key_num_list[idx%key_len]) % LENGTH_OF_ALPHABET]
                    idx += 1

def vigenere_decode_with_key(ciphertext, key):
    plaintext = ''
    idx = 0
    for c in ciphertext:
        if c.lower() in ALPHABET:
            plaintext += IDX_TO_CHAR[(CHAR_TO_IDX[c.lower()] - best_key_num_list[idx%key_len]) % LENGTH_OF_ALPHABET]
            idx += 1
        else:
            plaintext += c
    return plaintext




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--ciphertext', type=str, default='', help='Vigenere Cipher')
    parser.add_argument('--key', type=str, default=None, help='key to decode the cipher')
    parser.add_argument('--key_len', type=int, default=None, help='length of key')
    parser.add_argument('--test', action='store_true', help='if run the test example')
    args = parser.parse_args()
    if args.test:
        test()
    else:
        if not args.key:
            plaintext = vigenere_decode_with_key(ciphertext, args.key)






