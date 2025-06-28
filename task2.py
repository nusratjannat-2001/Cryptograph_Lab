import os

encryption_dict = {}
with open("output.txt", "r") as f:
    lines = f.readlines()[1:]  
    for line in lines:
        parts = line.strip().split(" -> ")
        if len(parts) == 2:
            encryption_dict[parts[0]] = parts[1]

decryption_dict = {v: k for k, v in encryption_dict.items()}

plaintext = "hellothereagai"

def split_blocks(text):
    i = 0
    blocks = []
    while i < len(text):
        if i + 3 <= len(text) and text[i:i+3] in encryption_dict:
            blocks.append(text[i:i+3])
            i += 3
        
        elif i + 2 <= len(text) and text[i:i+2] in encryption_dict:
            blocks.append(text[i:i+2])
            i += 2
       
        elif text[i:i+1] in encryption_dict:
            blocks.append(text[i:i+1])
            i += 1
        else:
            raise ValueError(f"No matching block found for: {text[i:]}")
    return blocks


plaintext_blocks = split_blocks(plaintext)
cipher_blocks = [encryption_dict[blk] for blk in plaintext_blocks]
ciphertext = ''.join(cipher_blocks)


recovered_blocks = [decryption_dict[blk] for blk in cipher_blocks]
recovered_plaintext = ''.join(recovered_blocks)


print("Plaintext:         ", plaintext)
print("Split blocks:      ", plaintext_blocks)
print("Cipher blocks:     ", cipher_blocks)
print("Ciphertext:        ", ciphertext)
print("Decrypted text:    ", recovered_plaintext)