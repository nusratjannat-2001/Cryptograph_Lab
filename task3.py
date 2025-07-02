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
    rows = (length + width - 1) // width  # ceiling division

    plaintext = [' '] * length  # Placeholder list for decrypted text

    idx = 0
    for i in range(width):
        for j in range(i, length, width):
            plaintext[j] = ciphertext[idx]
            idx += 1

    return ''.join(plaintext)


if __name__ == "__main__":
    plaintext = "DEPARTMENT OF COMPUTER SCIENCE AND TECHNOLOGY UNIVERSITY OF RAJSHAHI BANGLADESH"
    plaintext = plaintext.replace(" ", "")  # Remove spaces

    width = int(input("Enter the width for Transposition Cipher: "))
    
    print(f"Plaintext:  {plaintext}")
    # Encryption
    ciphertext = encrypt_transposition(plaintext, width)
    print("Encrypted Text:", ciphertext)

    # Decryption
    decryptedtext = decrypt_transposition(ciphertext, width)
    print("Decrypted Text:", decryptedtext)
