# Classical Cipher
Classical Cipher decoder and encoder.
1. Caesar Cipher
2. Linear Cipher
3. Vigenere Cipher


## Requirements
1. python==3.9.2
2. pytest==6.2.5

## Run
### Caesar
```shell
# Caesar encoding
python caesar_cipher.py -p 'If he had anything confidential to say.' -k 7

# Input plaintext by file
python caesar_cipher.py -pf plaintext.txt -k 7

# Caesar decoding with key
python caesar_cipher.py -c 'Pm ol ohk hufaopun jvumpkluaphs av zhf.' -k 7

# Caesar decoding without key. Maybe not working when ciphertext is too short.
python caesar_cipher.py -c 'Pm ol ohk hufaopun jvumpkluaphs av zhf.'

# Input ciphertext by file
python caesar_cipher.py -cf ciphertext.txt
```

### Caesar
```shell
# Linear encoding (C=a*P+b(mod 26))
python linear_cipher.py -p "If he had anything confidential to say." -a 3 -b 1

# Linear decoding with key
python linear_cipher.py -c "Zq wn wbk bovgwzot hroqzknogzbi gr dbv." -a 3 -b 1

```

### Vigenere
```shell
# Vigenere encoding
python vigenere_cipher.py -pf p.txt -k cryptii

# Vigenere decoding with key
python vigenere_cipher.py -cf c.txt -k cryptii

# Vigenere decoding with the length of the key. Maybe not working when ciphertext is too short.
python vigenere_cipher.py -cf c.txt -kl 7

# Vigenere decoding just with the ciphertext. Maybe not working when ciphertext is too short.
python vigenere_cipher.py -cf c.txt
```

## Test
```shell
# Test linear Cipher
pytest tests/test_linear.py

# Test Caesar Cipher
pytest tests/test_caesar.py

# Test Vigenere Cipher
pytest tests/test_vigenere.py
```
