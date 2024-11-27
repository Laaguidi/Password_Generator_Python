import random
import string

def generate_password(length=12, include_uppercase=True, include_lowercase=True, include_digits=True, include_symbols=True):
    """
    Generates a random password of the specified length, including the specified character sets.

    Args:
        length (int, optional): The desired length of the password. Defaults to 12.
        include_uppercase (bool, optional): Whether to include uppercase letters. Defaults to True.
        include_lowercase (bool, optional): Whether to include lowercase letters. Defaults to True.
        include_digits (bool, optional): Whether to include digits. Defaults to True.
        include_symbols (bool, optional): Whether to include symbols. Defaults to True.

    Returns:
        str: The generated password.
    """

    characters = ""
    ##include_uppercase is a boolean variable (True or False).
    ## If include_uppercase is True, the uppercase alphabet (from 
    ## string.ascii_uppercase, which is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ') ## is added to the characters pool.

    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be selected.")
    
    #''.join() takes a list of characters and combines (joins) them into a single string.
    #This part is a for loop that runs length times.
    #_ is a placeholder variable (conventionally used when the loop variable isn’t needed).
    #range(length) means the loop will run as many times as the password's length (default is 12).
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password = generate_password()
    print("Generated password:", password)