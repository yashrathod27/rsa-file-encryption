RSA Encryption & Decryption:

This application is a Python-based implementation of the RSA cryptographic algorithm developed for the Applied Cryptography module at the University of West London. It provides a terminal-based interface to generate public and private key pairs and safely process text files.

Project Structure

code.py - The core script containing the RSA mathematical algorithms, menu interface, and file operations.

text.txt - The original source file containing the plaintext message to be protected.

text.txt.encrypted - The output file containing the secure ciphertext integers.

text.txt.decrypted - The final output file showing the successfully decrypted plaintext.


System Functionality

1. Key Generation

Prime Selection: The tool automatically picks two distinct random prime numbers ($p$ and $q$) within a localized range of 1 to 99.

Modulus and Totient Calculation: It computes the product $n = p \times q$ to establish the modulus and determines Euler's totient $\phi(n) = (p - 1) \times (q - 1)$.

Key Pair Production: The program randomly selects a public exponent $e$ that is coprime to $\phi(n)$, and calculates its modular multiplicative inverse $d$. This produces a working public key $(e, n)$ and private key $(d, n)$ instantly without complex heavy computations.

2. File Encryption

The application processes the target text file by mapping each character to its equivalent numerical value. It applies the RSA encryption formula to generate a secure encrypted output file.

3. File Decryption

Using the correct private key parameters, the script reverses the mathematical operations on the encrypted data. It translates the numbers back into plain characters and saves the completely restored text into a separate decrypted file.

How to Run the Script

Step 1: Launch the Program

Make sure Python is installed on your computer. Open your terminal or Command Prompt in the folder and run:

```
python code.py
```

Step 2: Generate Cryptographic Keys

Choose the key generation option from the main menu. Save or copy down your generated public and private key components.

Step 3: Run Encryption

Select the encryption option from the menu. The script reads your source file, encrypts the text content, and outputs the encrypted file in the same folder.

Step 4: Run Decryption

Select the decryption option from the menu. Enter your private key values when prompted to securely restore the encrypted file back into readable text.
