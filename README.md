# Mono- and Polyalphabetic Ciphers

This tool encrypts and decrypts messages using a **monoalphabetic substitution cipher**. It leverages the `argparse` module to handle command-line arguments.

## Usage


### Arguments

- `--encrypt KEY`: Encrypts the contents of `FILE` using the provided `KEY`.
- `--decrypt KEY`: Decrypts the contents of `FILE` using the provided `KEY`.
- `--out OUTFILE`: Specifies the output file to save the encrypted/decrypted text. If omitted, output is printed to the console.
- `FILE`: The input file containing the plaintext or ciphertext.

> **Note:** The `KEY` should be a 26-character string that represents a permutation of the alphabet (a-z), with each character appearing only once.

## Example Usage

1. **Navigate to the script's directory:**

   ```bash
   cd $PATH/src/mono

   python3 mono.py --encrypt qwertyuiopasdfghjklzxcvbnm plaintext.txt --out encrypted.txt

   python3 mono.py --decrypt qwertyuiopasdfghjklzxcvbnm encrypted.txt --out decrypted.txt


Simply copy and paste this text into your `README.md` file to improve its appearance and readability.


