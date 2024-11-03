import argparse

letters = "abcdefghijklmnopqrstuvwxyz"

def main():
    parser = argparse.ArgumentParser(prog="Mono", description="Mono-alphabet decrypt/encrypt")
    parser.add_argument("--encrypt", metavar="KEY", help="key to encrypt")
    parser.add_argument("--decrypt", metavar="KEY", help="key to decrypt")
    parser.add_argument("--out", metavar="OUTFILE", help="encrypted/decrypted file as output")
    parser.add_argument("file", metavar="FILE", help="a given file to read data")

    args = parser.parse_args()

    # determine action en- or decrypt
    if args.encrypt:
        key = args.encrypt
        action = encrypt
    elif args.decrypt:
        key = args.decrypt
        action = decrypt
    else:
        parser.error("either --encrypt or --decrypt must be specified")

    # check if the key is valid
    if len(set(key)) != 26 or len(key) != 26:
        parser.error("Key must be 26 characters, including every letter of the alphabet only once")

    if args.encrypt is None and args.decrypt is  None:
        print("There is a problem with the given inputs")

    # read, process and give the output message
    message = read_file(args.file).lower() # read the file and make all letters lowercase
    output = action(message, key)

    if args.out:
        write_file(args.out , output)
    else:
        print(output)

# encrypts the plaintext using the key
def encrypt(plaintext, key):
    encrypted = '' # that will be the output
    encrypt_map = {letters[i]: key[i] for i in range(26)}  # pairs each letter in "letters" to the corresponding letter in "key"
    return encrypted.join(encrypt_map[char] if char in letters else '' for char in plaintext)

# decrypts the ciphertext using the key
def decrypt(ciphertext, key):
    decrypted = ''
    decrypt_map = {key[i]: letters[i] for i in range(26)} # paris each letter in "key" to the corresponding letter in "letter"
    return decrypted.join(decrypt_map[char] if char in letters else '' for char in ciphertext)

# reads the contents of a file
def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

# writes the contents to a file
def write_file(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)

if __name__ == "__main__":
    main()
