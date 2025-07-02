def encrypt_transposition(text, width):
    ciphertext = ""
    length = len(text)

    # Read column-wise
    for i in range(width):
        for j in range(i, length, width):
            ciphertext += text[j]

    return ciphertext


def decrypt_transposition(ciphertext, width):
    length = len(ciphertext)
    rows = (length + width - 1) // width  # Ceiling division
    plaintext = [' '] * length  # Placeholder for decrypted text

    idx = 0
    for i in range(width):
        for j in range(i, length, width):
            plaintext[j] = ciphertext[idx]
            idx += 1

    return ''.join(plaintext)


if __name__ == "__main__":
    plaintext = "DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING"
    plaintext = plaintext.replace(" ", "")  # Remove spaces

    width = int(input("Enter the width for Transposition Cipher: "))

    # 🔐 Double Encryption
    temp_ciphertext = encrypt_transposition(plaintext, width)
    ciphertext = encrypt_transposition(temp_ciphertext, width)

    print("Encrypted Text:", ciphertext)

    # 🔓 Double Decryption
    temp_decryptedtext = decrypt_transposition(ciphertext, width)
    decryptedtext = decrypt_transposition(temp_decryptedtext, width)

    print("Decrypted Text:", decryptedtext)
