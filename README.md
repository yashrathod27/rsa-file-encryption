\# RSA File Encryption and Decryption Tool



A lightweight Python implementation of the RSA (Rivest-Shamir-Adleman) cryptographic algorithm to securely encrypt and decrypt text files. This project handles key generation, mathematical encryption, and safe block-by-block data restoration.



\## Features

\- \*\*Asymmetric Encryption:\*\* Uses a public key for encryption and a private key for decryption.

\- \*\*File-to-File Processing:\*\* Reads a standard text file (`.txt`), outputs a secure encrypted file (`.txt.encrypted`), and reverses it back cleanly (`.txt.decrypted`).

\- \*\*Pure Python Implementation:\*\* Built using native mathematical principles without relying on heavy external third-party dependencies.



\## Files Structure

\- `code.py` - The core Python script containing the RSA algorithm logic and file I/O operations.

\- `text.txt` - The original source file containing the plaintext message.

\- `text.txt.encrypted` - The resulting file holding the ciphertext after running encryption.

\- `text.txt.decrypted` - The final output file verifying perfect restoration of the original plaintext.



\## How It Works

1\. \*\*Key Generation:\*\* The script computes a public key exponent $(e, n)$ and a private key exponent $(d, n)$ using prime numbers.

2\. \*\*Encryption:\*\* Each character in the target text file is converted into its ASCII/Unicode numerical equivalent and encrypted using the formula:  

&#x20;  $C \\equiv M^e \\pmod n$

3\. \*\*Decryption:\*\* The encrypted integers are processed back into characters using the private key formula:  

&#x20;  $M \\equiv C^d \\pmod n$



\## Usage

Ensure your Python file and the target `text.txt` are in the same folder, then execute the script:

```bash

python code.py

