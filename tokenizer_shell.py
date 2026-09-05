"""
Tokenizer Assignment - Starter Template

Name: Cayden Goddard
Date: 9/04/2026

Instructions:
- Complete each function where indicated with TODO comments.
- Do NOT delete function definitions.
- You may add helper functions if needed.
"""

import re
from collections import Counter


def read_text_file(filename):
    """
    Read and return the contents of a text file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def whitespace_tokenize(text):
    """
    Tokenize text using whitespace only.

    Example:
    "Hello world!" -> ["Hello", "world!"]
    """
    return text.split()


def preprocess_contractions(text):
    """
    Separate common contractions like:
    don't -> do n't
    I'm -> I 'm

    Hint: Use re.sub()
    """
    text = re.sub(r"(\w+)n't\b", r"\1 n't", text)
    text = re.sub(r"(\w+)'(m|re|ve|ll|d|s)\b", r"\1 '\2", text)
    return text


def regex_tokenize(text):
    """
    Tokenize text using regular expressions.

    Handles:
    - punctuation (separated out)
    - numbers (decimals like 12.50 kept together)
    - contractions (after preprocessing, e.g. "n't", "'m")
    - hyphenated words kept together (e.g. "well-known")
    """
    text = preprocess_contractions(text)

    pattern = r"n't|'\w+|\d+\.\d+|[\w-]+|[^\w\s]"
    tokens = re.findall(pattern, text)

    return tokens


def token_statistics(tokens):
    """
    Return:
    - total number of tokens
    - number of unique tokens
    - frequency counts
    """
    total = len(tokens)
    frequencies = Counter(tokens)
    unique = len(frequencies)

    return total, unique, frequencies


def print_token_report(name, tokens):
    """
    Print:
    - total tokens
    - unique tokens
    - first 20 tokens
    """
    total, unique, frequencies = token_statistics(tokens)

    print(f"\n=== {name} ===")
    print(f"Total tokens: {total}")
    print(f"Unique tokens: {unique}")
    print("First 20 tokens:", tokens[:20])
    print("Top 5 most common tokens:", frequencies.most_common(5))


def compare_tokenizers(tokens1, tokens2):
    """
    Compare two token lists.
    """
    print("\n=== Comparison ===")

    print("Tokenizer 1 total:", len(tokens1))
    print("Tokenizer 2 total:", len(tokens2))

    print("Tokenizer 1 unique:", len(set(tokens1)))
    print("Tokenizer 2 unique:", len(set(tokens2)))

    print("\nTokenizer 1 sample:", tokens1[:10])
    print("Tokenizer 2 sample:", tokens2[:10])


def main():
    #Change this to the file you will provide
    filename = "sample_text.txt"

    try:
        text = read_text_file(filename)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return

    whitespace_tokens = whitespace_tokenize(text)
    regex_tokens = regex_tokenize(text)

    print_token_report("Whitespace Tokenizer", whitespace_tokens)
    print_token_report("Regex Tokenizer", regex_tokens)

    compare_tokenizers(whitespace_tokens, regex_tokens)


if __name__ == "__main__":
    main()