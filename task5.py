def letter_to_number_1based(c):
    return ord(c.upper()) - ord('A') + 1

def number_to_letter_1based(n):
    return chr((n - 1) % 26 + ord('A'))

def otp_encrypt(plaintext, key):
    ciphertext = ""
    for p, k in zip(plaintext, key):
        p_num = letter_to_number_1based(p)
        k_num = letter_to_number_1based(k)
        c_num = (p_num + k_num) % 26
        if c_num == 0:
            c_num = 26
        ciphertext += number_to_letter_1based(c_num)
    return ciphertext

def otp_decrypt(ciphertext, key):
    plaintext = ""
    for c, k in zip(ciphertext, key):
        c_num = letter_to_number_1based(c)
        k_num = letter_to_number_1based(k)
        p_num = (c_num - k_num + 26) % 26
        if p_num == 0:
            p_num = 26
        plaintext += number_to_letter_1based(p_num)
    return plaintext

if __name__ == "__main__":
    with open("text.txt", "r") as f:
        plaintext = f.readline().strip().upper()

    with open("key.txt", "r") as f:
        enc_full_key = f.readline().strip().upper()

    if len(enc_full_key) < len(plaintext):
        print("Error: Encryption key is too short.")
        exit(1)

    enc_key = enc_full_key[:len(plaintext)]
    remaining_enc_key = enc_full_key[len(plaintext):]

    cipher = otp_encrypt(plaintext, enc_key)

    print("Plaintext:   ", plaintext)
    print("Enc Key:     ", enc_key)
    print("Ciphertext:  ", cipher)

    with open("key.txt", "w") as f:
        f.write(remaining_enc_key)
    print("Encryption key updated (used part removed).")

    with open("key2.txt", "r") as f:
        dec_full_key = f.readline().strip().upper()

    if len(dec_full_key) < len(cipher):
        print("Error: Decryption key is too short.")
        exit(1)

    dec_key = dec_full_key[:len(cipher)]
    remaining_dec_key = dec_full_key[len(cipher):]

    recovered = otp_decrypt(cipher, dec_key)

    print("Dec Key:     ", dec_key)
    print("Decrypted:   ", recovered)

    with open("key2.txt", "w") as f:
        f.write(remaining_dec_key)
    print("Decryption key updated (used part removed).")
