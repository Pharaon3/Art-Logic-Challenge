"""
String Encoding and Decoding Script

This script allows the user to encode and decode a string using a custom encoding scheme.

The encoding process converts a string into a list of integers by packing the ASCII values
of characters into 32-bit chunks. The decoding process reverses this, reconstructing the
original string from the list of encoded integers.

Functions:
- custom_encode(input_string): Encodes the input string into a list of integers.
- custom_decode(encoded_list): Decodes the list of integers back into the original string.

The user is prompted to input a string, which is then encoded and decoded, with both results
displayed.

"""
from convert import custom_encode, custom_decode

# Prompt the user for input
input_string = input("Enter a string to encode: ")

# Encode the string
encoded_result = custom_encode(input_string)
print("Encoded Result:", encoded_result)

# Decode the encoded result
decoded_string = custom_decode(encoded_result)
print("Decoded String:", decoded_string)
