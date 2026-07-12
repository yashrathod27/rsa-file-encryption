import random
import hashlib
from math import gcd
import tkinter as tk
from tkinter import filedialog

def print_main_heading(text):
    print(f"{'=' * 60}")
    print(f"# {text.center(56)} #")
    print(f"{'=' * 60}")

def print_menu_heading(text):
    print(f"{'-' * 60}")
    print(f"# {text.center(56)} #")
    print(f"{'-' * 60}")

def print_section_heading(text):
    print(f"\n# {text} #\n")

def print_message(label, message):
    print(f"\n# {label} #")
    print(f"{message}\n")

def print_success(text):
    print(f"[SUCCESS] {text}")

def print_error(text):
    print(f"[ERROR] {text}")

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime():
    while True:
        candidate = random.randint(1, 99)
        if is_prime(candidate):
            return candidate

def generate_keys():
    p = generate_prime()
    q = generate_prime()
    while p == q:
        q = generate_prime()
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    def mod_inverse(a, m):
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1

    d = mod_inverse(e, phi)
    return (e, n), (d, n)

def encrypt_message(message, public_key):
    e, n = public_key
    checksum = hashlib.sha256(message.encode()).hexdigest()
    message_with_checksum = f"{message}|{checksum}"
    return [pow(ord(char), e, n) for char in message_with_checksum]

def decrypt_message(ciphertext, private_key):
    d, n = private_key
    decrypted_text = ''.join([chr(pow(c, d, n)) for c in ciphertext])
    try:
        message, checksum = decrypted_text.rsplit('|', 1)
        if hashlib.sha256(message.encode()).hexdigest() != checksum:
            raise ValueError("Checksum verification failed. Data integrity compromised.")
        return message
    except ValueError:
        raise ValueError("Invalid key or corrupted data.")

def select_file():
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    filepath = filedialog.askopenfilename(title="Select File", filetypes=(("All Files", "*.*"),))
    if not filepath:
        print_error("No file selected. Please try again.")
        return None
    print_message("File Selected", f"File path: {filepath}")
    return filepath

def encrypt_file():
    print_section_heading("File Encryption Initiated")
    filepath = select_file()
    if not filepath:
        return

    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            plaintext = file.read()

        print_message("File Content", plaintext)
        public_key_input = input("Enter public key (format: e,n): ").strip()
        public_key = tuple(map(int, public_key_input.split(',')))

        ciphertext = encrypt_message(plaintext, public_key)
        encrypted_content = ' '.join(map(str, ciphertext))

        encrypted_filepath = f"{filepath}.encrypted"
        with open(encrypted_filepath, 'w', encoding='utf-8') as file:
            file.write(encrypted_content)
        print_message("Encrypted Content", encrypted_content)
        print_success(f"Encryption successful. Saved as: {encrypted_filepath}")
    except Exception as e:
        print_error(f"Encryption error: {e}")

def decrypt_file():
    print_section_heading("File Decryption Initiated")
    filepath = select_file()
    if not filepath:
        return

    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            ciphertext = list(map(int, file.read().split()))

        private_key_input = input("Enter private key (format: d,n): ").strip()
        private_key = tuple(map(int, private_key_input.split(',')))

        plaintext = decrypt_message(ciphertext, private_key)

        decrypted_filepath = filepath.replace(".encrypted", ".decrypted")
        with open(decrypted_filepath, 'w', encoding='utf-8') as file:
            file.write(plaintext)
        print_message("Decrypted Content", plaintext)
        print_success(f"Decryption successful. Saved as: {decrypted_filepath}")
    except ValueError as e:
        print_error(f"Decryption failed: {e}")
    except Exception as e:
        print_error(f"Unexpected error: {e}")

def rsa_program():
    print_main_heading("RSA Encryption & Decryption System")
    while True:
        print_menu_heading("MAIN MENU")
        print("1. Generate RSA Keys")
        print("2. Encrypt File")
        print("3. Decrypt File")
        print("4. Exit")

        choice = input("\nEnter your selection (1-4): ").strip()

        if choice == "1":
            print_section_heading("Key Pair Generation")
            public_key, private_key = generate_keys()
            print(f"Public Key (For encryption): {public_key}")
            print(f"Private Key (Keep secure): {private_key}")
            print_success("Keys generated successfully.")

        elif choice == "2":
            encrypt_file()

        elif choice == "3":
            decrypt_file()

        elif choice == "4":
            print_main_heading("Thank you for using the system. Exiting.")
            break

        else:
            print_error("Invalid selection. Please choose a valid option.")

if __name__ == "__main__":
    rsa_program()
