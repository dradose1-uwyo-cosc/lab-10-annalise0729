# Annalise Gade
# UWYO COSC 1010
# Submission Date: 11/24/24
# Lab 10
# Lab Section: 15
# Sources, people worked with, help given to: None
# No further comments

#import modules you will need 

from hashlib import sha256 
from pathlib import Path

def get_hash(to_hash):
    """You can use """
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()

# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."

# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.

# You will need to include a try-except-catch block in your code.
# - The reading of files needs to occur in the try blocks.
try:
    path = Path('rockyou.txt')
    rockyou_contents = path.read_text()
    rockyou = rockyou_contents.splitlines()
except FileNotFoundError:
    print(f"'{path}' file not found. Please put correct file path.")
    exit
except Exception:
    print(f"Error reading '{path}': {Exception}")
    exit

# - Read in the value stored within `hash`.
#   - You must use a try and except block.
try:
    path2 = Path('hash')
    hash = path2.read_text()
except FileNotFoundError:
    print(f"'{path2}' file not found. Please put correct file path.")
    exit
except Exception:
    print(f"Error reading '{path2}': {Exception}")
    exit

# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.

try:
    for line in rockyou:
        line = line.strip()
        line_hash = get_hash(line)
        if line_hash == hash:
            print("Password found!")
            print(f"The password is: {line}")
            print(line_hash)
            break
    else:
        print("Password not found :(")
except Exception:
    print(f"Error: {Exception}")
    exit