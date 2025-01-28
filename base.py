"""
Custom Encoding and Decoding Module

This module provides two functions: `encode_custom` and `decode_custom`. 
The `encode_custom` function transforms an input string into a list of integers 
using bitwise operations and packing of ASCII values. The `decode_custom` function 
takes a list of encoded integers and reconstructs the original string.

Encoding Scheme:
- The input string is processed in blocks of four characters.
- Each block of four characters is packed into a 32-bit integer using bitwise operations.
- The resulting list of integers represents the encoded form of the original string.

Decoding Scheme:
- The encoded integers are unpacked into 32-bit chunks.
- The original ASCII values are extracted from each chunk and reassembled into the decoded string.

Module Functions:
- encode_custom(input_data): Encodes a string into a list of integers.
- decode_custom(encoded_data): Decodes a list of integers back into the original string.
"""

def is_ascii_only(text):
   """
   Check if all characters in the string are ASCII characters.

   @param: text (str): The string to check.
   @return: bool: True if all characters are in the ASCII range; otherwise False.
   """
   return not any(ord(c) > 127 for c in text)

def encode_custom(input_data):
   """
   Custom encoding function that turns a string into a list of integers.
   
   The input string is processed in blocks of four characters, which are encoded 
   using bitwise operations to pack the ASCII values into integers.

   @param input_data: The string to encode.
   @return: A list of integers representing the encoded data.
   """
   packed_chunks = []  # To hold the integer values of each character block
   temp_chunk = 0  # Current chunk being formed
   bit_position = 0  # Position of the current bit within the chunk

   for char in input_data:
      temp_chunk |= ord(char) << bit_position  # Pack ASCII value into the chunk
      bit_position += 8  # Move to the next byte position
      if bit_position == 32:  # When the chunk is full
         packed_chunks.append(temp_chunk)  # Save the chunk
         temp_chunk = 0  # Reset chunk for the next group
         bit_position = 0  # Reset bit position

   # Process the remaining characters in the last chunk if any
   if bit_position > 0:
      packed_chunks.append(temp_chunk)

   # Now encode the chunks into a list of integers using a custom mapping
   encoded_output = []
   for chunk in packed_chunks:
      encoded_value = 0  # Will hold the encoded version of the chunk
      bit_counter = 0  # Tracks the bit position
      while chunk > 0:
         encoded_value |= (chunk & 1) << ((bit_counter % 8) * 4 + (bit_counter // 8))
         chunk >>= 1
         bit_counter += 1
      encoded_output.append(encoded_value)

   return encoded_output

def decode_custom(encoded_data):
   """
   Custom decoding function that reconstructs the original string from a list of integers.
   
   This function extracts the ASCII values from the encoded integers and reassembles 
   the original string.

   @param encoded_data: A list of integers representing the encoded data.
   @return: The decoded string.
   """
   restored_chunks = []  # List to hold reconstructed 32-bit chunks
   for encoded_value in encoded_data:
      chunk = 0  # Temporary holder for chunk reconstruction
      bit_pos = 0  # Tracks the bit position during decoding
      while encoded_value > 0:
         if encoded_value & 1:
            chunk |= 1 << ((bit_pos % 4) * 8 + (bit_pos // 4))
         encoded_value >>= 1
         bit_pos += 1
      restored_chunks.append(chunk)

   # Rebuild the original string from the chunks
   output_string = ""
   for chunk in restored_chunks:
      for i in range(4):  # Extract up to 4 characters from each chunk
         char_value = (chunk >> (i * 8)) & 0xFF
         if char_value != 0:  # Skip zero padding
            output_string += chr(char_value)

   return output_string
