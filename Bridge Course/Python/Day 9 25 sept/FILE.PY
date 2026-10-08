import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("=== Random Password Generator ===")

try:
    length = int(input("Enter password length: "))

    if length < 4:
        print("Password length should be at least 4.")
    else:
        password = generate_password(length)
        print("\nGenerated Password:", password)

except ValueError:
    print("Please enter a valid number.")