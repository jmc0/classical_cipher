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
from utils import Friedman, count_letter_percentage, get_single_key_and_mutual_ic, get_group_of_cipher

def vigenere_decode(ciphertext):
    key_len_list = Friedman(ciphertext)
    keylen_to_plaintext_and_key = {}
    for key_len in key_len_list:
        plaintext, best_key_char = vigenere_decode_with_key_len(ciphertext, key_len)
        keylen_to_plaintext_and_key[key_len] = [plaintext, best_key_char]
    return keylen_to_plaintext_and_key


def vigenere_decode_with_key_len(ciphertext, key_len):
    best_key_char = ''
    cipher_group = get_group_of_cipher(ciphertext, key_len)
    average_ic = 0
    for g in cipher_group:
        letter_and_per_sorted = count_letter_percentage(g)
        single_key, best_mutual_ic = get_single_key_and_mutual_ic(letter_and_per_sorted)
        best_key_char += IDX_TO_CHAR[single_key]
        average_ic += best_mutual_ic
    average_ic /= len(cipher_group)
    if average_ic > IC_OF_ENGLISH_VIGENERE_GROUP: 
        plaintext = vigenere_decode_with_key(ciphertext, best_key_char)
    else:
        plaintext = None
    return plaintext, best_key_char


def vigenere_decode_with_key(ciphertext, key):
    plaintext = ''
    idx = 0
    key_len = len(key)
    key_in_num = []
    for k in key:
        key_in_num.append(CHAR_TO_IDX[k.lower()])
    for c in ciphertext:
        if c.lower() in ALPHABET:
            plaintext += IDX_TO_CHAR[(CHAR_TO_IDX[c.lower()] - key_in_num[idx%key_len]) % LENGTH_OF_ALPHABET]
            idx += 1
        else:
            plaintext += c
    return plaintext


def test():
    ciphertext = "CTIOSLIP UYIHWMCJC RPIAFWZU KPU FV C XDDIIHCA HRU IMCLVRN BTJLEKYJL EXCQCZX DCVN JMGJMGZ, IEEZNWXZQV WHW JVQAS SWVMC IIVP MUMITVQKL ME RZPJXZEM, PZ QRPG P DSLNL-QL GIAXIHRRNGHA ARU CCHARTM DM XYG BTJLEKYJL. FIGIZPRX C UTZWRIM LPXYQCI BWZPO UYIHWMCJC RPIAFWZU MHZIEVQPSPP TMFBMIGL ZUSNNMSNI FH BWL GZRPTY YJGL PUH GGZWHTJ QN IOI BGG XUZFNDTK, XYWA BHOZPO TZTZQVPNI, STQQLVP, DCGNPRTG, SLJVEBXVR, RPL HV SE OWGL EKVZPJXZXM PWTIQIROIJ VW IOI TTGEAEECTNAMTCTAF YEKVUVVDGL. XA ARU NXUECNG TETCKKXAPP TMRVKEKHTK ME VPT UMEGBTLRKJ KTUXLTG IOEK UMRYITA WU H GZRPTY'W RNODYMKJU XZ RFV I HLRJKJAL RFT XGHGKKKPS WRHMVBEIF WU TIJUIVL WVECGPXP; KV UHGK, KB LHW WWZIOII TMPSMQGL IOEK CVN HHVSCPAI TTGEASXTIEOMT UKWLQV (KVRSYUKVV JMGJMGZ) WYQCAK VVOIXU WVECGL IMGV XM XYG ISCIIUIGF JLNTN BRUGZHAEEFA IOI TKXWLV RNODYMKJU XAWVNN. HLGLTQIF SW VPT RIP WATK WYQCAK ECQVT II JWNUPGZGVI MSI C ODVH TKXWLV KQ UPPRKCQC JSEHQSLRKKIAPXP WVSLV RP IIAETM. BWPW WWVSHQVPBPS TIKVRPTCG EPZ JZTAI LBGNQRPXCA AIHXVF JN HYXWAIL OVTKZOSWHA PUH ZU OTUIICTAF GRNTTK OVTKZOSWHA'H WVZPKXWPV; CTILVECBXCICA ICK QFTM QSYEVTN, PX NCA GLWKCBTK FP ETPBHV UPPURFP, BWL MEXMCASI QN XUJFTUPAMFP BWLSIA ICK XYG NJUHROMCAECU WU ALVQZTAMTCT RYCGVWVYEGJG, PZ WYCVCVR'J OIMPQ: 'KJM TUIDA SCVAJ VPT ZCJVMB."
    print("Running the test examples...")

    #Test vigenere decode with key
    key = 'cipher'
    print('Running vigenere decode with key...')
    print('The cipher text is %s ' % ciphertext)
    print('The input key is %s ' % key)
    plaintext = vigenere_decode_with_key(ciphertext, key)
    print('The plain text is %s' % plaintext)

    #Test vigenere decode with key length
    key_len = 6
    print('Running vigenere decode with key length...')
    print('The input key length is %d ' % key_len)
    plaintext, best_key_char = vigenere_decode_with_key_len(ciphertext, key_len)
    if plaintext:
        print('For input %d length key, the best key is %s' % (key_len, best_key_char))
        print('The plain text is %s' % plaintext)
    else:
        print('For input %d length key, there isn\'t a valid key' % (key_len))

    #test vigenere decode without key and key length
    print('Running vigenere_decode just with cipher...')
    keylen_to_plaintext_and_key = vigenere_decode(ciphertext)
    if keylen_to_plaintext_and_key:
        for item in keylen_to_plaintext_and_key.items():
            key_len = item[0]
            plaintext = item[1][0]
            key_char = item[1][1]
            if plaintext:
                print('For possible %d length key, the best key is %s' % (key_len, key_char))
                print('The plain text is %s ' % plaintext)
            else:
                print('For possible %d length key, there isn\'t a valid key' % (key_len))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--ciphertext', type=str, default=None, help='Vigenere Cipher')
    parser.add_argument('--cipherfile', type=str, default=None, help='Vigenere Cipher File')
    parser.add_argument('--key', type=str, default=None, help='key to decode the cipher')
    parser.add_argument('--key_len', type=int, default=None, help='length of key')
    parser.add_argument('--test', action='store_true', help='if run the test example')
    args = parser.parse_args()
    if args.test:
        test()
    else:
        import pdb
        pdb.set_trace()
        if args.ciphertext:
            ciphertext = args.ciphertext
        if args.cipherfile:
            with open(args.cipherfile) as f:
                ciphertext = f.read()
        if not args.key:
            if not args.key_len:
                plaintext = vigenere_decode(ciphertext)
            else:
                plaintext = vigenere_decode_with_key_len = (ciphertext, args.key_len)
        else:
            plaintext= vigenere_decode_with_key(ciphertext, args.key)
