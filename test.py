"""
Unit test suite for transformation functions.

Validates the correctness of encoding, decoding, and ASCII compatibility.
"""

import unittest
from base import decode_custom, encode_custom, is_ascii_only


class TestTransformations(unittest.TestCase):
   """
   Test suite for text transformation functions, including encoding and decoding.
   """

   def test_ascii_compliance(self):
      """
      Ensure proper ASCII compatibility checks.
      """
      self.assertTrue(is_ascii_only("Hello World"), "Failed for ASCII string.")
      self.assertTrue(is_ascii_only("12345"), "Failed for digits.")
      self.assertTrue(is_ascii_only("!@#$%^&*()"), "Failed for symbols.")

      # negative test: should not allow Unicode.
      self.assertFalse(is_ascii_only("Goodbye 🌍"), "Failed for emoji string.")
      self.assertFalse(is_ascii_only("Café"), "Failed for accented characters.")
      self.assertFalse(
         is_ascii_only("ASCII ✔, Unicode ✪"), "Failed for mixed content."
      )

   def test_encoding_decoding_round_trip(self):
      """
      Ensure that encoding and decoding are reversible without data loss.
      """
      sample_texts = [
         "",
         "y",
         "apple",
         "encoded phrase",
         "This is a more complicated test string!",
         "The longer the input, the more complex the result.",
      ]
      for text in sample_texts:
         with self.subTest(text=text):
            self.assertEqual(
               decode_custom(encode_custom(text)),
               text,
               f"Round-trip failure for text: {text}",
            )

   def test_encoded_output(self):
      """
      Ensure the encoding produces the expected results.
      """
      data = [
         "tacocat",
         "never odd or even",
         "lager, sir, is regal",
         "go hang a salami, I'm a lasagna hog",
         "egad, a base tone denotes a bad age",
      ]
      expected_encoding = [
         [267487694, 125043731],
         [267657050, 233917524, 234374596, 250875466, 17830160],
         [267394382, 167322264, 66212897, 200937635, 267422503],
         [
            200319795,
            133178981,
            234094669,
            267441422,
            78666124,
            99619077,
            267653454,
            133178165,
            124794470,
         ],
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
      for idx, item in enumerate(data):
         with self.subTest(item=item):
            self.assertEqual(
               encode_custom(item), expected_encoding[idx], "Encoding mismatch."
            )

   def test_decoded_output(self):
      """
      Ensure that decoding correctly restores the original data.
      """
      encoded_samples = [
         [267487694, 125043731],
         [267657050, 233917524, 234374596, 250875466, 17830160],
         [267394382, 167322264, 66212897, 200937635, 267422503],
         [
            200319795,
            133178981,
            234094669,
            267441422,
            78666124,
            99619077,
            267653454,
            133178165,
            124794470,
         ],
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
      expected_decoding = [
         "tacocat",
         "never odd or even",
         "lager, sir, is regal",
         "go hang a salami, I'm a lasagna hog",
         "egad, a base tone denotes a bad age",
      ]
      for idx, encoded_data in enumerate(encoded_samples):
         with self.subTest(encoded_data=encoded_data):
            self.assertEqual(
               decode_custom(encoded_data),
               expected_decoding[idx],
               "Decoding mismatch.",
            )

   def test_edge_cases(self):
      """
      Handle special cases such as empty input or special symbols.
      """

      # Should return empty result for encoding an empty string.
      self.assertEqual(encode_custom(""), [], "Empty string encoding failed.")
      self.assertEqual(decode_custom([]), "", "Empty list decoding failed.")

      # Test with special symbols.
      special_chars = "!@#$%^&*()_+"
      self.assertEqual(
         decode_custom(encode_custom(special_chars)),
         special_chars,
         "Special characters test failed.",
      )

      # Negative case: should not encode unicode characters.
      unicode_example = "🌟💫"
      self.assertNotEqual(
         decode_custom(encode_custom(unicode_example)),
         unicode_example,
         "Unicode handling test failed.",
      )


if __name__ == "__main__":
   unittest.main()
