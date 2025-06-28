def encrypt_caesar(text, shift=3):
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif 'a' <= char <= 'z':
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char

    return result

def decrypt_caesar(text):
    return encrypt_caesar(text, -3)

def main():

    with open("input.txt", "r") as file:
        text = file.read()

    t = encrypt_caesar(text)

    x = decrypt_caesar(t)

    print("Original Text:\n", text)
    print("\nEncrypted Text:\n", t)
    print("\nDecrypted Text:\n", x)

  
if __name__ == "__main__":
    main()