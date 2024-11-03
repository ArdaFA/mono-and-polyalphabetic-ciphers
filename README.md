# mono-and-polyalphabetic-ciphers

a tool using argparse module which encrypts and decrypts a message using a monoalphabetic subs. cipher. 

usage: 'mono.py [-h] (--encrypt KEY | --decrypt KEY) [--out OUTFILE] FILE' 

example usage: 
    'cd $PATH/src/mono'
    'python3 mono.py --encrypt qwertyuiopasdfghjklzxcvbnm plaintext.txt --out encrypted.txt'
    'python3 mono.py --decrypt qwertyuiopasdfghjklzxcvbnm encrypted.txt --out decrypted.txt'
