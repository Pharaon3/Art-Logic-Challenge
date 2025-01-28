"""
Text Transformation Tool

This script enables text conversion between its plain form and a custom
numerical representation.

Features:
1. Text to numbers (encoding).
2. Numbers to text (decoding).

Functions:
- encode_text(txt): Converts plain text to integers.
- decode_numbers(nums): Reconstructs plain text from integers.

This tool interacts with the user to demonstrate transformations.
"""

from base import custom_encode, custom_decode, check_ascii

def execute():
   """
   Core function to handle the transformation process.

   Gathers user input, verifies ASCII compatibility, encodes text to integers,
   and decodes back to the original. Results are displayed for review.
   """
   # Input from user
   txt = input("Enter text for conversion: ")

   if not check_ascii(txt):
      print("Input is not ASCII-compatible.")
      return

   # Encoding phase
   nums = custom_encode(txt)
   print("Encoded Data:", nums)

   # Decoding phase
   restored = custom_decode(nums)
   print("Decoded Text:", restored)

if __name__ == "__main__":
   execute()
