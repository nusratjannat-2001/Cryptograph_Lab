def encryption(plaintext, key):
    ciphertext = ""

    for p_char, k_char in zip(plaintext, key):
        base = ord(p_char) - ord('A')
        key_base = ord(k_char) - ord('A')
        ch = (base + key_base + 1) % 26 + ord('A')
        ciphertext += chr(ch)

    return ciphertext


def decryption(ciphertext, key):
    plaintext = ""

    for c_char, k_char in zip(ciphertext, key):
        base = ord(c_char) - ord('A')
        key_base = ord(k_char) - ord('A')
        ch = (base - key_base + 26 - 1) % 26 + ord('A')
        plaintext += chr(ch)

    return plaintext


if __name__ == "__main__":
    # Read input from files
    with open("text.txt", "r") as f:
        input_text = f.readline().strip()

    with open("key.txt", "r") as f:
        key = f.readline().strip().upper()

    print("Input text:", input_text)
    print("Key:", key)

    # Clean input: keep only letters, uppercase
    plaintext = "".join(ch.upper() for ch in input_text if ch.isalpha())

    if len(plaintext) > len(key):
        print("Length not matched")
        exit(0)

    # Encrypt
    cipher = encryption(plaintext, key)
    print("Cipher:", cipher)

    # Decrypt
    decrypt = decryption(cipher, key)
    print("Decrypt:", decrypt)
