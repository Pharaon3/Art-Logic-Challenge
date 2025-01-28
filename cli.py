"""
Text Transformation Tool

This script provides a utility for converting text to a custom numerical representation and back.

Features:
1. Encode text into a list of integers.
2. Decode integers back into the original text.

Functions:
- encode_custom(text): Converts plain text to its numerical form.
- decode_custom(numbers): Reconstructs text from its numerical form.

This script includes interactive functionality for demonstration purposes.
"""

from base import encode_custom, decode_custom, is_ascii_only

def main():
   """
   Main function to execute the text transformation workflow.

   - Takes user input for text conversion.
   - Checks for ASCII compatibility.
   - Encodes text to integers and decodes it back for validation.
   """
   user_input = input("Enter text to transform: ")

   if not is_ascii_only(user_input):
      print("Error: Input contains non-ASCII characters.")
      return

   # Perform encoding
   encoded_numbers = encode_custom(user_input)
   print("Encoded Representation:", encoded_numbers)

   # Perform decoding
   decoded_text = decode_custom(encoded_numbers)
   print("Decoded Text:", decoded_text)

if __name__ == "__main__":
   main()
