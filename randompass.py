import random
import string
import hashlib

# Define special characters to exclude
EXCLUDED_CHARACTERS = """(){}[]|`¬¦! "£$%^&*"<>:;#~_-+=,@"""


def filter_special_characters():
    """Returns allowed special characters after filtering excluded ones."""
    return ''.join(char for char in string.punctuation if char not in EXCLUDED_CHARACTERS)


def generate_password(use_uppercase=True, use_numbers=True, use_symbols=True, length=random.randint(10, 15)):
    # Character pools
    pools = {
        'lowercase': string.ascii_lowercase,
        'uppercase': string.ascii_uppercase if use_uppercase else '',
        'numbers': string.digits if use_numbers else '',
        'symbols': filter_special_characters() if use_symbols else ''
    }

    # Combines selected pools
    all_characters = ''.join(pools.values())
    if not all_characters:
        raise ValueError("No character sets selected for password generation.")


    # Generates password
    return ''.join(random.choices(all_characters, k=length))


def hash_password(password):
    """Hashes a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()


def save_to_file(content, filename="passwords.txt", mode="a"):
    """
    File mode ('a' for append, 'w' for overwrite)
    """
    with open(filename, mode) as file:
        file.write(content + "\n")
    print(f"Content saved to {filename}")


# Main logic for demonstration
if __name__ == "__main__":
    try:
        # Generates password
        password = generate_password(use_uppercase=True, use_numbers=True, use_symbols=True)
        print("Generated password:", password)

        # Saves raw password
        # save_to_file(password)

        # Hash and save the password
        hashed_password = hash_password(password)
        save_to_file(hashed_password)
    except ValueError as e:
        print("Error:", e)
