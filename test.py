"""
Unit test suite for transformation functions.

Validates the correctness of encoding, decoding, and ASCII compatibility.
"""

import unittest
from convert import custom_decode, custom_encode, check_ascii


class TransformationTests(unittest.TestCase):
   """
   Test suite for text transformation functions, including encoding and decoding.
   """

   def test_ascii_validation(self):
      """
      Verify ASCII compatibility checks.
      """
      self.assertTrue(check_ascii("Hello"), "Failed for ASCII-only string.")
      self.assertTrue(check_ascii("12345"), "Failed for numeric ASCII.")
      self.assertTrue(check_ascii("~!@#$%^&*()"), "Failed for ASCII symbols.")

      # negative test: should not allow Unicode.
      self.assertFalse(check_ascii("Hello 🌍"), "Failed for string with emoji.")
      self.assertFalse(check_ascii("Résumé"), "Failed for accented character.")
      self.assertFalse(check_ascii("ASCII ✓, Unicode ✪"), "Failed for mixed content.")

   def test_reversible_transformations(self):
      """
      Ensure encoding and decoding operations are reversible.
      """
      cases = [
         "",
         "x",
         "word",
         "phrase example",
         "Let's test this string thoroughly!",
         "Complexity increases with longer examples.",
      ]
      for text in cases:
         with self.subTest(text=text):
            self.assertEqual(
               custom_decode(custom_encode(text)),
               text,
               f"Reversible test failed for: {text}",
            )

   def test_encoding_format(self):
      """
      Check if encoding outputs match expected results.
      """
      inputs = ["A", "FRED", " :^)", "egad, a base tone denotes a bad age"]
      expected = [
         [16777217],
         [251792692],
         [79094888],
         [
            267389735,
            82841860,
            267651166,
            250793668,
            233835785,
            267665210,
            99680277,
            133170194,
            124782119,
         ],
      ]
      for idx, val in enumerate(inputs):
         with self.subTest(val=val):
            self.assertEqual(
               custom_encode(val), expected[idx], "Encoding mismatch."
            )

   def test_decoding_consistency(self):
      """
      Validate decoding restores encoded inputs to original.
      """
      encoded_cases = [
         [16777217],
         [251792692],
         [79094888],
         [
            267389735,
            82841860,
            267651166,
            250793668,
            233835785,
            267665210,
            99680277,
            133170194,
            124782119,
         ],
      ]
      expected_results = ["A", "FRED", " :^)", "egad, a base tone denotes a bad age"]
      for idx, code in enumerate(encoded_cases):
         with self.subTest(code=code):
            self.assertEqual(
               custom_decode(code), expected_results[idx], "Decoding mismatch."
            )

   def test_corner_cases(self):
      """
      Address edge scenarios like empty inputs and special symbols.
      """

      # should return empty array when encode empty string
      self.assertEqual(custom_encode(""), [], "Empty string encoding failed.")
      self.assertEqual(custom_decode([]), "", "Empty list decoding failed.")

      # should allow special characters.
      special = "!@#$%^&*()"
      self.assertEqual(
         custom_decode(custom_encode(special)),
         special,
         "Special characters test failed.",
      )

      # @dev negative test: should not allow encode unicode.
      unicode_sample = "🚀✨"
      self.assertNotEqual(
         custom_decode(custom_encode(unicode_sample)),
         unicode_sample,
         "Unicode character handling failed.",
      )


if __name__ == "__main__":
   unittest.main()
