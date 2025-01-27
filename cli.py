"""
String Transformation Utility

This program provides functionality to transform text between its original form and
a custom numerical representation.

It offers two main operations:
1. Encoding: Translates text into a sequence of integers based on character ASCII values.
2. Decoding: Reconstructs the original text from the numerical sequence.

Functions:
- encode_string(text): Converts text into a series of integers.
- decode_sequence(numbers): Converts a sequence of integers back into text.

The script takes user input, applies the transformations, and displays the results.
"""

from convert import encode, decode, is_ascii

def main():
    """
    Main function to execute the encoding and decoding process.

    This function collects user input, encodes the input text into a sequence of 
    integers using a custom encoding scheme, and then decodes it back to verify 
    the transformation. The encoded data and reconstructed text are displayed to the user.
    """
    # Collect user input
    user_text = input("Input text for transformation: ")

    if not is_ascii(user_text):
        return print("Error: Input Text is not ASCII-compatible.")

    # Perform encoding
    encoded_data = encode(user_text)
    print("Encoded Output:", encoded_data)

    # Perform decoding
    reconstructed_text = decode(encoded_data)
    print("Reconstructed Text:", reconstructed_text)

if __name__ == "__main__":
    main()
