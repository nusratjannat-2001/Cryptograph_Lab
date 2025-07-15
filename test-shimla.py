def char_to_num(c):
    return ord(c.upper()) - ord('A') + 1

def num_to_char(n):
    return chr(((n - 1) % 26) + ord('A'))

def encrypt_otp(plaintext, key):
    ciphertext = ""
    for p_char, k_char in zip(plaintext, key):
        p = char_to_num(p_char)
        k = char_to_num(k_char)
        c = (p + k) % 26
        ciphertext += num_to_char(c)
    return ciphertext

def decrypt_otp(ciphertext, key):
    plaintext = ""
    for c_char, k_char in zip(ciphertext, key):
        c = char_to_num(c_char)
        k = char_to_num(k_char)
        p = (c - k + 26) % 26
        plaintext += num_to_char(p)
    return plaintext

def trim_used_key(filename, used_length):
    with open(filename, 'r') as file:
        content = file.read().strip()
    remaining = content[used_length:] if used_length < len(content) else ""
    with open(filename, 'w') as file:
        file.write(remaining)

def main():
    plaintext = input("Enter plaintext (A-Z letters only): ").strip().upper()

    with open("key.txt", 'r') as f:
        key = f.read().strip().upper()

    if len(key) < len(plaintext):
        print("Error: Key in key.txt is shorter than plaintext.")
        return

    ciphertext = encrypt_otp(plaintext, key)
    print("Encrypted Text:", ciphertext)

    trim_used_key("key.txt", len(plaintext))

    with open("key2.txt", 'r') as f:
        key2 = f.read().strip().upper()

    if len(key2) < len(ciphertext):
        print("Error: Key in key2.txt is shorter than ciphertext.")
        return

    decrypted = decrypt_otp(ciphertext, key2)
    print("Decrypted Text:", decrypted)

    trim_used_key("key2.txt", len(ciphertext))

if __name__ == "__main__":
    main()
