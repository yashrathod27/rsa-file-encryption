RSA Encryption & Decryption:

This application is a Python-based implementation of the RSA cryptographic algorithm developed for the Applied Cryptography module at the University of West London. It provides a terminal-based interface to generate public and private key pairs and safely process text files.

Project Structure:

code.py - The core script containing the RSA mathematical algorithms, menu interface, and file operations.

text.txt - The original source file containing the plaintext message to be protected.

text.txt.encrypted - The output file containing the secure ciphertext integers.

text.txt.decrypted - The final output file showing the successfully decrypted plaintext.


System Functionality:

1. Key Generation

Prime Selection: The tool automatically picks two distinct random prime numbers ($p$ and $q$) within a localized range of 1 to 99.

Modulus and Totient Calculation: It computes the product $n = p \times q$ to establish the modulus and determines Euler's totient $\phi(n) = (p - 1) \times (q - 1)$.

Key Pair Production: The program randomly selects a public exponent $e$ that is coprime to $\phi(n)$, and calculates its modular multiplicative inverse $d$. This produces a working public key $(e, n)$ and private key $(d, n)$ instantly without complex heavy computations.

2. File Encryption

ASCII Character Mapping: The application processes the target text file by mapping each character to its equivalent numerical ASCII value.

RSA Formula Processing: It applies the standard mathematical formula ($c = m^e \pmod n$) using the public key parameters to output a secure ciphertext file.

3. File Decryption

Mathematical Reversal: Using the private key parameters, the script reverses the mathematical operations on the encrypted data ($m = c^d \pmod n$).

Plaintext Restoration: It translates the numeric streams back into readable text characters and saves the completely restored text into a separate decrypted file.

#How to Run the Script:

#Step 1: Launch the Program

Make sure Python is installed on your computer. Open your terminal or Command Prompt in the folder and run:

```
python code.py
```

#Step 2: Generate Cryptographic Keys

Select option 1 ("Generate RSA Keys") from the main menu. 

The script will instantly compute and display your public key pair and private key pair on the screen. 

Copy these parameters down.

#Step 3: Run File Encryption

Select option 2 ("Encrypt File") from the menu. 

A Tkinter graphical file window will pop up. 

Choose your text.txt file, input your public key values when prompted, and the .encrypted file will appear in the folder.

#Step 4: Run File Decryption

Select option 3 ("Decrypt File") from the menu. 

Select the encrypted file using the pop-up window, input your secret private key values, and verify that the message content successfully matches your original plaintext. 

CRITICAL REMINDER: You must use the exact private key numbers ($d$ and $n$) that were generated in Step 2 to successfully decrypt the file and completely restore it back into readable text.
