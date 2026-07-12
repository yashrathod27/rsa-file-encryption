RSA Encryption & Decryption:

This application is a Python-based implementation of the RSA cryptographic algorithm developed for the Applied Cryptography (CP50087E) module at the University of West London. It provides a method for generating keys, encrypting and decrypting text files, and ensuring data integrity using cryptographic hashing.  

Features & Component Architecture

1. RSA Key Generation

Prime Number Processing: The system takes two distinct prime numbers, $p$ and $q$, to calculate the modulus $n$ and Euler's totient $\phi(n)$.  

Key Pair Production: It derives the public exponent $e$ and the private exponent $d$. This creates the public key used for encryption and the private key used for decryption.  

2. File Encryption & Decryption

ASCII Character Mapping: The encryption function converts characters from a selected text file into their corresponding numerical ASCII values before applying the RSA formula.  

Tkinter GUI Integration: Instead of manual path typing, the script utilizes Python's built-in Tkinter library to launch a native file explorer window, allowing users to visually select .txt files.  

3. Integrity Verification (SHA-256)

Checksum Creation: To prevent unauthorized tampering, the application generates a unique SHA-256 hash of the original file content during encryption.  

Verification Check: Upon decryption, the system recalculates the SHA-256 hash of the decrypted output and compares it to the original checksum to confirm the data remained unaltered.  
