"""
Custom Text Transformation Module

This module provides two key functions: `encode_text` and `decode_data`. 
- `encode_text` converts an input string into a sequence of integers 
  using bitwise manipulation and ASCII encoding.
- `decode_data` reconstructs the original string from a list of encoded integers.

Encoding Strategy:
- The input string is processed in blocks of four characters.
- Each block of four characters is packed into a 32-bit integer using bitwise operations.
- The result is a list of integers that represents the encoded form of the string.

Decoding Strategy:
- Each integer in the encoded list is unpacked to extract the 32-bit chunks.
- The ASCII values for each character are derived from these chunks, and the original 
string is rebuilt.

Module Functions:
- encode_text(input_string): Encodes the string into a list of integers.
- decode_data(encoded_list): Decodes the list of integers back into the string.
"""

def is_ascii(input_string):
    """
    Check if all characters in the input string are ASCII-compatible.

    This function iterates through each character in the input string and
    verifies whether its Unicode code point is less than 128 (the ASCII range).

    Args:
        input_string (str): The string to check for ASCII compatibility.

    Returns:
        bool: True if all characters in the string are ASCII-compatible, False otherwise.

    Example:
        >>> is_ascii("Hello")
        True
        >>> is_ascii("Hello 😊")
        False
    """
    return all(ord(char) < 128 for char in input_string)

def encode(input_string):
    """
    Encodes a string into a list of integers by packing groups of four characters.

    This function breaks the string into 4-character chunks, converts each chunk 
    to a 32-bit integer by bitwise packing of their ASCII values.

    @param input_string: The text to be encoded.
    @return: A list of integers representing the encoded version of the text.
    """
    packed_chunks = []  # Stores the 32-bit chunks formed from 4 characters
    chunk = 0  # The current chunk being processed
    bit_position = 0  # The current bit position within the chunk

    # Loop through each character in the input string
    for char in input_string:
        chunk |= ord(char) << bit_position  # Add the ASCII value to the current chunk
        bit_position += 8  # Shift by 8 bits for the next character
        if bit_position == 32:  # Once 4 characters (32 bits) are packed
            packed_chunks.append(chunk)  # Store the packed chunk
            chunk = 0  # Reset for the next chunk
            bit_position = 0  # Reset the bit position for the next 32 bits

    # If there are leftover characters, store them as a smaller chunk
    if bit_position > 0:
        packed_chunks.append(chunk)

    # Convert packed chunks into a custom integer representation
    encoded_output = []
    for chunk in packed_chunks:
        encoded_value = 0  # The transformed chunk
        bit_index = 0  # Keeps track of the bit position in the encoded value
        while chunk > 0:
            encoded_value |= (chunk & 1) << ((bit_index % 8) * 4 + (bit_index // 8))
            chunk >>= 1
            bit_index += 1
        encoded_output.append(encoded_value)

    return encoded_output


def decode(encoded_list):
    """
    Decodes a list of integers back into the original string.

    This function takes each encoded integer, unpacks it into 32-bit chunks, 
    and retrieves the original ASCII values of the characters to reconstruct the string.

    @param encoded_list: A list of encoded integers.
    @return: The reconstructed original string.
    """
    decoded_chunks = []  # Holds the decoded 32-bit chunks
    for encoded_value in encoded_list:
        chunk = 0  # Temporary variable to reconstruct the chunk
        bit_pos = 0  # Tracks the bit positions during decoding
        while encoded_value > 0:
            if encoded_value & 1:
                chunk |= 1 << ((bit_pos % 4) * 8 + (bit_pos // 4))
            encoded_value >>= 1
            bit_pos += 1
        decoded_chunks.append(chunk)

    # Convert the decoded chunks back into characters
    original_text = ""
    for chunk in decoded_chunks:
        for i in range(4):  # Extract up to 4 characters from each chunk
            char_ascii = (chunk >> (i * 8)) & 0xFF
            if char_ascii != 0:  # Skip padding zeros
                original_text += chr(char_ascii)

    return original_text
