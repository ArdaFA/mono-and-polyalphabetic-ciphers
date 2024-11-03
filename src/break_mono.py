import argparse

letters = "abcdefghijklmnopqrstuvwxyz"
match_dict = {}

def count_letter_frequencies(file_path):
    # a dictionary to hold letter counts
    letter_count = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}  # count for each letter

    try:
        with open(file_path, 'r') as file:
            # read the contents of the file
            contents = file.read().lower()  # convert to lowercase

            # count the occurrences of each letter
            for char in contents:
                if char.isalpha():  # check if the character is a letter
                    letter_count[char] += 1
        return letter_count

    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
        return None

# generate a key mapping from common frequencies to cipher frequencies
def generate_key(common_frequencies, cipher_frequencies):

    # sort letters by frequency in descending order
    sorted_common = sorted(common_frequencies.items(), key=lambda item: item[1], reverse=True)
    sorted_cipher = sorted(cipher_frequencies.items(), key=lambda item: item[1], reverse=True)

    # create the key mapping
    key_mapping = {}
    for (common_letter, _), (cipher_letter, _) in zip(sorted_common, sorted_cipher):
        key_mapping[common_letter] = cipher_letter

    return key_mapping


if __name__ == "__main__":
    common_file_path = 'common.txt'  # path to common.txt file
    common_letter_frequencies = count_letter_frequencies(common_file_path)

    print("COMMON TEXT: ")
    print("See how many times each letter appear in common.txt file")
    if common_letter_frequencies:
        # print the letter counts
        for letter, count in common_letter_frequencies.items():
            print(f"{letter} = {count}")
    print("---------------------")
    decrypted_file_path = 'ciphertext.txt'
    decrypted_letter_frequencies = count_letter_frequencies(decrypted_file_path)

    print("CIPHER TEXT: ")
    print("See how many times each letter appear in ciphertext.txt file")
    if decrypted_file_path:
        # print the letter counts
        for letter, count in decrypted_letter_frequencies.items():
            print(f"{letter} = {count}")
    print("---------------------")

    # generate and print the key
    key = generate_key(common_letter_frequencies, decrypted_letter_frequencies)
    print("Generated Key:")
    print("See the generated key sorted by frequency:")
    for cipher_letter, common_letter in key.items():
        print(f"{cipher_letter} -> {common_letter}")
    print("---------------------")

    # output the derived key sorted according to alphabet
    encryption_key = ''
    print("print the key according to alphabet:")
    for common_letter in sorted(key):  # Sort the keys alphabetically
        cipher_letter = key[common_letter]
        print(f"{common_letter} -> {cipher_letter}")
        encryption_key += cipher_letter
    print(encryption_key)