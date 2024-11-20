import random
import string
import hashlib
import secrets #For better randomness in security-sensitive applications

EXCLUDED_CHARACTERS = set("""(){}[]|`¬¦! "£$%^&*"<>:;#~_-+=,@""")

def filter_special_characters():
    return ''.join(char for char in string.punctuation if char not in EXCLUDED_CHARACTERS)

def generate_password(use_uppercase=True, use_numbers=True, use_symbols=True, length=None):
    all_characters = string.ascii_lowercase
    if use_uppercase:
        all_characters += string.ascii_uppercase
    if use_numbers:
        all_characters += string.digits
    if use_symbols:
        all_characters += filter_special_characters()

    if not all_characters:
        raise ValueError("No character sets selected for password generation.")

    length = length or secrets.choice(range(10, 16)) #Use secrets for better randomness.
    return ''.join(secrets.choice(all_characters) for i in range(length)) #More efficient string creation

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def save_to_file(content, filename="passwords.txt", mode="a"):
    try:
        with open(filename, mode) as file:
            file.write(content + "\n")
        print(f"Content saved to {filename}")
    except IOError as e:
        print(f"Error saving to file: {e}")

if __name__ == "__main__":
    try:
        password = generate_password(use_uppercase=True, use_numbers=True, use_symbols=True)
        print("Generated password:", password)
        save_to_file(password)
        hashed_password = hash_password(password)
        save_to_file(hashed_password)
    except ValueError as e:
        print("Error:", e)
    except Exception as e: #Catch other potential errors
        print(f"An unexpected error occurred: {e}")