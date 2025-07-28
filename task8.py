import hashlib

def md5_hash(text):
    # Create an MD5 hash object
    hash_object = hashlib.md5()
    
    # Convert input to bytes and update the hash object
    hash_object.update(text.encode())

    # Return the hexadecimal digest
    return hash_object.hexdigest()

# Take input from the user
user_input = input("Enter text to hash using MD5: ")

# Compute and display the MD5 hash
hashed_output = md5_hash(user_input)
print(f"MD5 hash of '{user_input}' is:\n{hashed_output}")

