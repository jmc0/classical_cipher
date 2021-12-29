from caesar_cipher import caesar_encode, caesar_decode


def test_caesar():
    print('-' * 100)
    print("Running the caesar encode test example.")
    plaintext = 'If he had anything confidential to say, he wrote it in cipher, that is, by so changing the order of the letters of the alphabet, that not a word could be made out.'
    key = 7
    print("The plaintext is: \"%s\"." % plaintext)
    print("The key is: %d" % key)
    ciphertext = caesar_encode(plaintext, key)
    print("The ciphertext is: \"%s\"." % ciphertext)
    print('-' * 100)
    print("Running the caesar decode with key test example.")
    print("The ciphertext is: \"%s\"." % ciphertext)
    print("The key is: %d." % key)
    plaintext = caesar_decode(ciphertext, key)
    print("The plaintext is: \"%s\"." % plaintext)
    print('-' * 100)
    print("Running the caesar decode without key test example.")
    print("The ciphertext is: \"%s\"." % ciphertext)
    plaintext = caesar_decode(ciphertext)
    print("The plaintext is: \"%s\"." % plaintext)

if __name__ == '__main__':
    test_caesar()
