# another_a_little_bit_generic_ceaser_cipher
Just a psychological break caused by insecurities about my programming fundamentals and a little of who knows, a 'portfolio?'
# Caesar Cipher in Python

A simple Python implementation of the **Caesar Cipher**, built as a hands-on exercise while studying introductory cryptography.

This project supports:

- text encryption
- text decryption
- brute-force testing of all possible shifts

The goal of this project is not to provide real-world secure encryption, but to reinforce the fundamentals behind classical substitution ciphers, character shifting, modulo arithmetic, and simple code organization in Python.

---

## What is the Caesar Cipher?

The Caesar Cipher is a classical substitution cipher in which each letter in a message is shifted by a fixed number of positions in the alphabet.

For example, with a shift of `3`:

- `a` becomes `d`
- `b` becomes `e`
- `c` becomes `f`

So the text `abc` becomes `def`.

When the shift goes past the end of the alphabet, it wraps around:

- `x` becomes `a`
- `y` becomes `b`
- `z` becomes `c`

This is why modulo `% 26` is used.

---

## Features

- Encrypts plaintext using a configurable shift
- Decrypts ciphertext using the same core logic
- Supports lowercase letters
- Supports uppercase letters
- Preserves spaces, punctuation, and other non-alphabetic characters
- Supports brute-force mode by testing all 26 possible shifts
- Handles large shift values through modulo arithmetic

---

## Project Structure

`ceaser_cipher.py`

Main elements of the project:

- `CaesarCipher` class
- `_shift_text()` internal method
- `encrypt()` method
- `decrypt()` method
- `bruteforce()` method
- `app_menu()` command-line menu

---

## How It Works

### `_shift_text(plaintext, jumps)`

This is the core method of the project.

It:

1. iterates through the text character by character  
2. checks whether the character is lowercase or uppercase  
3. converts the character into its Unicode value using `ord()`  
4. applies the shift using modulo `% 26`  
5. converts the result back to a character using `chr()`

This method is reused by both encryption and decryption.

### `encrypt(plaintext, jumps)`

Encrypts a plaintext string by shifting its letters forward.

### `decrypt(ciphertext, jumps)`

Decrypts a ciphertext string by shifting its letters backward.

### `bruteforce(ciphertext)`

Tries every possible shift from `0` to `25` and prints all possible outputs.

---

## Example Usage

### Encryption

Input:

`plaintext: hello`  
`shift: 3`

Output:

`khoor`

### Decryption

Input:

`ciphertext: khoor`  
`shift: 3`

Output:

`hello`

### Brute Force

Input:

`khoor`

Possible output:

`The text with jump 0: khoor`  
`The text with jump 1: jgnnq`  
`The text with jump 2: ifmmp`  
`The text with jump 3: hello`

---

## How to Run

Make sure you have Python 3 installed.

Run the program with:

`python ceaser_cipher.py`

---

## Menu Options

When running the script, the following options are available:

1. Encrypt  
2. Decrypt (only if you know how many shifts the text has)  
3. Bruteforce a Caesar cipher text  
0. Exit

---

## Concepts Practiced

This project was useful for practicing:

- Python classes and methods
- internal/private method conventions
- string iteration
- conditionals
- `ord()` and `chr()`
- command-line input handling
- exception handling with `try` / `except`

---

## Limitations

This project is intended for **learning purposes only**.

The Caesar Cipher is **not secure** and should not be used for real-world encryption.

It is easy to break because:

- There are only 26 possible shifts
- brute force is trivial
- Frequency analysis can also reveal the plaintext

---

## Future Improvements

Some possible improvements for this project:

- rename `CeaserCipher` to `CaesarCipher`
- rename `ceaser_cipher.py` to `caesar_cipher.py`
- add unit tests
- improve CLI formatting
- return brute-force results as a data structure instead of only printing them
- expand the project into a larger symmetric cryptography manager

---

## Why I Built This

I built this project as a practical exercise while studying cryptography.

The main objective was to understand:

- how letter shifting actually works
- why modulo arithmetic matters
- how encryption and decryption can share the same core logic
- why the Caesar Cipher is weak from a security perspective
- how to structure a small Python project in a clean and understandable way

---


## Disclaimer

This project is for educational purposes only.
