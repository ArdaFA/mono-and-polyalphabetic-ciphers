import argparse
from collections import Counter

alphabet = "abcdefghijklmnopqrstuvwxyz"
key = [" "] * 26 # defining key

def main():
    parser = argparse.ArgumentParser(prog="break_mono", description="Monoalphabetic cipher decryption.")
    parser.add_argument("ciphertext_file", help="File containing the ciphertext to decrypt.")
    args = parser.parse_args()

    # fixed file path to find occurrence
    common_file = 'common.txt'

    # take the given file and set it into variable
    ciphertext_file = args.ciphertext_file

    """ find most used 3 letters
    NORMALLY, the most used letters in english are:
        E
        T
        A
        O
        I """

    print("*-*-" * 10)
    # find the most used 5 letters in common file
    most_common_letters = find_most_used_letters(common_file)
    most_common_three = ''.join(most_common_letters)
    print("most used letters in common text is: ", most_common_three)


    # find the most used 5 letters in cipher text
    most_cipher_letters = find_most_used_letters(ciphertext_file)
    most_cipher_three = ''.join(most_cipher_letters)
    print("most used letters in ciphertext is:  ", most_cipher_three)

    # set the most used 3 letters into key according to 2 inputs (common file, cipher text)
    # first one

    for i in range(len(most_common_three)-1):
        # find which letter is most used in common
        letter = most_common_three[i]
        if letter in alphabet:
            # take the position of this letter and set according key letter at this position
            index = alphabet.index(letter)
            key[index] = most_cipher_three[i]


    print("key after most used letters")
    print("               |")
    print("               |")
    print("               V")
    print("alphabet: " + alphabet)
    key_string = "".join(key)
    print("key     : " + key_string)
    print("*-*-" * 10)

    # bigram = 2er string
    # find the most used 5 bigrams in common file
    most_common_bigrams = find_most_used_bigrams(common_file)
    most_common_five_bigrams = ''.join(most_common_bigrams)
    # join this bigrams with two spaces in between
    most_common_five_bigrams = "".join(
        [most_common_five_bigrams[i:i + 2] for i in range(0, len(most_common_five_bigrams), 2)])
    print("Most used bigrams in commontext:", most_common_five_bigrams)



    # find the most used 5 bigrams in cipher text
    most_cipher_bigrams = find_most_used_bigrams(ciphertext_file)
    most_cipher_five_bigrams = ''.join(most_cipher_bigrams)
    # join the bigrams with two spaces in between
    most_cipher_five_bigrams = "".join(
        [most_cipher_five_bigrams[i:i + 2] for i in range(0, len(most_cipher_five_bigrams), 2)])
    print("Most used bigrams in ciphertext:", most_cipher_five_bigrams)

    # check if the letters in bigrams already exist in key
    for i in range(0, len(most_cipher_bigrams)-2):
        if i % 2 == 0: # first letters of each cipher bigrams
            if most_cipher_five_bigrams[i] != " ": # except the space between
                if most_cipher_five_bigrams[i] in key: # if the first letter of bigrams is already in key
                    other_cipher_letter = most_cipher_five_bigrams[i+1] # d
                    corresponding_letter = most_common_five_bigrams[i+1] # r
                    index = alphabet.index(corresponding_letter) # index of r
                    key[index] = other_cipher_letter # set d at same place in key
                if most_cipher_five_bigrams[i] not in key:
                    if most_cipher_five_bigrams[i+1] in key:
                        other_cipher_letter = most_cipher_five_bigrams[i] # y
                        corresponding_letter = most_common_five_bigrams[i] # e
                        index = alphabet.index(corresponding_letter) # index of e
                        key[index] = other_cipher_letter

    print("key after most used bigrams")
    print("               |")
    print("               |")
    print("               V")
    print("alphabet: " + alphabet)
    key_string = "".join(key)
    print("key     : " + key_string)
    print("*-*-" * 10)

    """find most used 3er chars (trigram) ... do kinda the same add some letters to the key"""

    """find most used 4er chars (four-gram) ... do kinda the same add some more letters to the key"""

    """ do this until ????  how many n-gram??"""

def find_most_used_letters(file_path):
    # read file and convert text to lowercase
    with open(file_path, 'r') as file:
        text = file.read().lower()

    # filter only alphabetic characters
    letters = [char for char in text if char.isalpha()]

    # count occurrences of each letter
    letter_counts = Counter(letters)

    # get the 3 most common letters
    most_common_three = dict(letter_counts.most_common(26))

    return most_common_three
    #print(most_common_five)

def find_most_used_bigrams(file_path):
    # read file and convert text to lowercase
    with open(file_path, 'r') as file:
        text = file.read().lower()

    # filter only alphabetic characters
    text = ''.join(char for char in text if char.isalpha())

    # create pairs of two consecutive characters
    pairs = [text[i:i + 2] for i in range(len(text) - 1)]

    # count occurrences of each pair
    pair_counts = Counter(pairs)

    # get the 5 most common pairs
    most_common_five = dict(pair_counts.most_common(3000))

    return most_common_five

