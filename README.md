NLP Tokenizer

A Python program that tokenizes text using two different strategies — a simple whitespace split and a more advanced regex-based approach — and compares the results.

Built for Assignment 2.5: Build Your Own NLP Tokenizer.

What it does

The program reads in a text file and tokenizes it two ways:

Whitespace Tokenizer — splits text only on spaces, using Python's built-in .split(). Fast, but punctuation stays glued to words (e.g. "yard." stays as one token) and contractions like "didn't" stay as a single unit.
Regex Tokenizer — uses regular expressions to separate punctuation from words, keep decimal numbers intact (e.g. 12.50), split contractions into their parts (e.g. "didn't" → "did" + "n't"), and keep hyphenated words together (e.g. "well-known").

After running both, the program prints:

Total token count
Number of unique tokens
The first 20 tokens
The 5 most common tokens
A side-by-side comparison of both tokenizers
