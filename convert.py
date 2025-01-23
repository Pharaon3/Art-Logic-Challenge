"""
Custom Encoding and Decoding Module

This module provides two functions: `custom_encode` and `custom_decode`. 
The `custom_encode` function transforms an input string into a list of integers 
using bitwise operations and packing of ASCII values. The `custom_decode` function 
takes a list of encoded integers and reconstructs the original string.

Encoding Scheme:
- The input string is processed in groups of four characters.
- Each group of four characters is packed into a 32-bit integer using bitwise operations.
- The resulting list of integers represents the encoded form of the original string.

Decoding Scheme:
- The encoded integers are unpacked into 32-bit chunks.
- The original ASCII values are extracted from each chunk and reassembled into the decoded string.

Module Functions:
- custom_encode(input_string): Encodes a string into a list of integers.
- custom_decode(encoded_list): Decodes a list of integers back into the original string.

"""
def custom_encode(input_string):
   """
   Encodes a given string into a list of integers using a custom scheme.
   
   This scheme processes the input string in groups of four characters, converting 
   them into integers using bitwise operations to pack their ASCII values.

   @param input_string: The string to encode.
   @return: A list of integers representing the encoded data.
   """
   chunked_values = []  # Holds the packed integers for each group of four characters
   current_chunk = 0  # The current chunk being constructed
   shift_offset = 0  # Tracks the current bit position within a chunk

   for char in input_string:
      current_chunk |= ord(char) << shift_offset  # Embed the ASCII value at the correct position
      shift_offset += 8  # Move to the next byte position
      if shift_offset == 32:  # When four characters (32 bits) are processed
         chunked_values.append(current_chunk)  # Save the chunk
         current_chunk = 0  # Reset for the next chunk
         shift_offset = 0  # Reset the bit position

   # Handle the remaining characters in the last incomplete chunk
   if shift_offset > 0:
      chunked_values.append(current_chunk)

   # Transform chunks into encoded integers using a custom mapping
   encoded_result = []
   for chunk in chunked_values:
      encoded = 0  # Encoded version of the chunk
      bit_counter = 0  # Tracks the bit mapping
      while chunk > 0:
         encoded |= (chunk & 1) << ((bit_counter % 8) * 4 + (bit_counter // 8))
         chunk >>= 1
         bit_counter += 1
      encoded_result.append(encoded)

   return encoded_result


def custom_decode(encoded_list):
   """
   Decodes a list of integers back into the original string using the custom scheme.
   
   This process reconstructs the original ASCII values from the encoded integers
   and reassembles the string.

   @param encoded_list: A list of integers representing the encoded data.
   @return: The decoded string.
   """
   reconstructed_values = []  # Holds reconstructed 32-bit chunks
   for encoded in encoded_list:
      chunk = 0  # Temporary holder for the reconstructed chunk
      bit_tracker = 0  # Tracks the bit mapping for decoding
      while encoded > 0:
         if encoded & 1:
            chunk |= 1 << ((bit_tracker % 4) * 8 + (bit_tracker // 4))
         encoded >>= 1
         bit_tracker += 1
      reconstructed_values.append(chunk)

   # Convert reconstructed values back into characters
   decoded_string = ""
   for chunk in reconstructed_values:
      for i in range(4):  # Extract up to 4 characters from each 32-bit chunk
         char_code = (chunk >> (i * 8)) & 0xFF
         if char_code != 0:  # Ignore padding zeros
            decoded_string += chr(char_code)

   return decoded_string
