import hashlib

def sha_hash(text, algorithm='sha256'):
    # Select the hashing algorithm
    if algorithm.lower() == 'sha1':
        hash_object = hashlib.sha1()
    elif algorithm.lower() == 'sha256':
        hash_object = hashlib.sha256()
    elif algorithm.lower() == 'sha512':
        hash_object = hashlib.sha512()
    else:
        raise ValueError("Unsupported algorithm! Use 'sha1', 'sha256', or 'sha512'.")

    # Update the hash object with bytes
    hash_object.update(text.encode())

    # Return the hexadecimal digest
    return hash_object.hexdigest()

# Take input from the user
text_input = input("Enter text to hash: ")
algorithm_input = input("Choose algorithm (sha1 / sha256 / sha512): ")

try:
    hashed_result = sha_hash(text_input, algorithm_input)
    print(f"{algorithm_input.upper()} hash of '{text_input}':\n{hashed_result}")
except ValueError as e:
    print(e)
