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

# Caesar decoding with key
python caesar_cipher.py -c 'Pm ol ohk hufaopun jvumpkluaphs av zhf.' -k 7

# Caesar decoding without key
python caesar_cipher.py -c 'Pm ol ohk hufaopun jvumpkluaphs av zhf.'
```

### Caesar
```shell
# Linear encoding (C=a*P+b(mod 26))
python linear_cipher.py -p "If he had anything confidential to say." -a 3 -b 1

# Linear decoding with key
python linear_cipher.py -c "Zq wn wbk bovgwzot hroqzknogzbi gr dbv." -a 3 -b 1

```
