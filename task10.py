def modular_pow(base, exponent, modulus):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent //= 2
        base = (base * base) % modulus
    return result

p = 47
q = 71
n = p * q            # 3337
phi = (p - 1) * (q - 1)  # 3220
e = 79
d = pow(e, -1, phi)
#print("d =", d) 


message = "6882326879666683"
block_size = 3
blocks = [int(message[i:i+block_size]) for i in range(0, len(message), block_size)]
print(f"Original message blocks: {blocks}")

encrypted_blocks = [modular_pow(m, e, n) for m in blocks]
print(f"Encrypted blocks: {encrypted_blocks}")

decrypted_blocks = [modular_pow(c, d, n) for c in encrypted_blocks]
print(f"Decrypted blocks: {decrypted_blocks}")

reconstructed_message = ''.join([f"{m:03d}" for m in decrypted_blocks])
print(f"Reconstructed message: {reconstructed_message}")
