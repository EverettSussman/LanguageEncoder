import numpy as np

def encode(message, key=None):
    """
    Encodes a message by replacing letters with
    other letters.
    """

    if key is None:
        # Set cipher value for encoding
        key = np.random.choice(range(1,26))

    print(message)

    encoded = ""
    # Iterate through message
    for char in message:
        # If character is a letter
        if char.isalpha():
            encoded += cipher(key, char)
        else:
            encoded += char

    print(encoded)
    return encoded


def cipher(key, char):
    """
    Determines the cipher letter based on
    the key.
    """
    if char.isupper():
        buf = 65
    else:
        buf = 97
    numVal = ord(char) - buf
    numVal = (numVal + key) % 26 + buf
    return chr(numVal)
