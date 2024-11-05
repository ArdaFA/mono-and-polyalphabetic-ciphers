import argparse
from collections import Counter

def load_words(file_path):
    """Load the list of common English words."""
    with open(file_path, "r") as f:
        return f.read().splitlines()

def load_ciphertext(file_path):
    """Load the ciphertext from the specified file and ensure it’s in lowercase."""
    with open(file_path, "r") as f:
        return f.read().strip().lower()  # Ensure ciphertext is lowercase

def perform_frequency_analysis(text):
    """Perform frequency analysis on the ciphertext."""
    return sorted(Counter(text).items(), key=lambda x: x[1], reverse=True)

def initial_mapping(ciphertext_frequency, english_frequency_order):
    """Create an initial letter mapping based on frequency analysis."""
    mapping = {}
    for i, (cipher_letter, _) in enumerate(ciphertext_frequency):
        if i < len(english_frequency_order):
            mapping[cipher_letter] = english_frequency_order[i]
    print("Initial Mapping:", mapping)  # Debugging line
    return mapping

def substitute(text, mapping):
    """Substitute the ciphertext letters according to the provided mapping."""
    return ''.join(mapping.get(c, c) for c in text)

def find_known_words(decoded_text, word_list):
    """Find known words in the decoded text."""
    return [word for word in word_list if word in decoded_text]

def refine_mapping(ciphertext, words, best_mapping, english_frequency_order, iterations=10):
    """Iteratively refine the letter mapping to increase word matches."""
    best_decoded_text = substitute(ciphertext, best_mapping)
    max_words_found = len(find_known_words(best_decoded_text, words))

    for _ in range(iterations):
        current_mapping = best_mapping.copy()

        for i in range(len(english_frequency_order)):
            for j in range(i + 1, len(english_frequency_order)):
                swapped_mapping = current_mapping.copy()
                letter1, letter2 = english_frequency_order[i], english_frequency_order[j]

                # Find the letters in the current mapping
                cipher1 = next((k for k, v in swapped_mapping.items() if v == letter1), None)
                cipher2 = next((k for k, v in swapped_mapping.items() if v == letter2), None)

                if cipher1 and cipher2:
                    # Swap them in the mapping
                    swapped_mapping[cipher1], swapped_mapping[cipher2] = swapped_mapping[cipher2], swapped_mapping[cipher1]

                    # Check the updated decoded text
                    decoded_text = substitute(ciphertext, swapped_mapping)
                    words_found = find_known_words(decoded_text, words)

                    # Update best mapping if more words are found
                    if len(words_found) > max_words_found:
                        max_words_found = len(words_found)
                        best_mapping = swapped_mapping
                        best_decoded_text = decoded_text

        print("Best Mapping After Refinement:", best_mapping)  # Debugging line

    return best_mapping, best_decoded_text

def main():
    # Argument parsing
    parser = argparse.ArgumentParser(description="Break a monoalphabetic substitution cipher.")
    parser.add_argument("FILE", help="Path to the ciphertext file")
    args = parser.parse_args()

    # Load resources
    words = load_words("common.txt")
    ciphertext = load_ciphertext(args.FILE)

    # Frequency analysis and initial mapping
    ciphertext_frequency = perform_frequency_analysis(ciphertext)
    print("Ciphertext Frequency:", ciphertext_frequency)  # Debugging line
    english_frequency_order = "etaoinshrdlcumwfgypbvkjxqz"
    best_mapping = initial_mapping(ciphertext_frequency, english_frequency_order)

    # Refine mapping
    best_mapping, _ = refine_mapping(ciphertext, words, best_mapping, english_frequency_order)

    # Output the derived key in a-z order
    print("Final Derived Key (a-z order):")
    print("".join(best_mapping.get(chr(i), '?') for i in range(ord('a'), ord('z') + 1)))

if __name__ == "__main__":
    main()
