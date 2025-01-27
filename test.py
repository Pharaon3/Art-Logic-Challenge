"""
Python test code for encode and decode functions. 
The test code uses the unittest module to validate 
the correctness of the encoding and decoding processes.
"""
import unittest

from convert import decode, encode, is_ascii

class TestCustomTextTransformation(unittest.TestCase):
    """
    Unit tests for the Custom Text Transformation module.

    This test class validates the functionality of the `encode` and `decode` functions.
    The module provides a mechanism to encode a string into a list of integers and decode it back 
    to the original string using bitwise operations and ASCII encoding.

    Test Cases:
    - is_ascii:
        Ensures that string is ASCII-compatible.
    - test_encode_decode:
        Ensures that encoding and decoding are reversible, i.e., the decoded string matches the original.
    - test_encode_output:
        Validates that the encoded output matches the expected format for a given input string.
    - test_decode_output:
        Verifies that the decoding process reconstructs the original string from a known encoded value.
    - test_edge_cases:
        Tests edge cases such as empty strings, special characters, and Unicode characters.

    The tests cover various scenarios, including:
    - Strings of different lengths (empty, single character, multiple characters).
    - Strings containing special characters and Unicode symbols.
    - Edge cases like padding and leftover characters during encoding.

    These tests ensure the correctness, robustness, and reliability of the encoding and decoding functions.
    """

    def test_ascii(self):
        """
        Test strings that contain only ASCII characters.
        """
        self.assertTrue(is_ascii("Hello"), "Failed for all-ASCII string")
        self.assertTrue(is_ascii("12345"), "Failed for numeric ASCII string")
        self.assertTrue(is_ascii("!@#$%^&*()_+"), "Failed for special characters")
        self.assertFalse(is_ascii("Hello 😊"), "Failed for string with emoji")
        self.assertFalse(is_ascii("Café"), "Failed for string with accented character")
        self.assertFalse(is_ascii("ASCII: 123, Unicode: ★"), "Failed for mixed ASCII and Unicode symbols")


    def test_encode_decode(self):
        """
        Test if the encoding and decoding processes are reversible.
        """
        test_strings = [
            "",  # Empty string
            "a",  # Single character
            "abcd",  # Exactly 4 characters
            "abcde",  # More than 4 characters
            "Hello, World!",  # Common phrase
            "This is a longer string to test the custom encoding and decoding.",
        ]

        for original in test_strings:
            with self.subTest(original=original):
                encoded = encode(original)
                decoded = decode(encoded)
                self.assertEqual(decoded, original, f"Failed for string: {original}")

    def test_encode_output(self):
        """
        Test if the encoded output matches the expected format.
        """
        input_strings = [
            "A",
            "FRED",
            " :^)",            
            "egad, a base tone denotes a bad age"
        ]
        expected_encodeds = [
            [16777217],
            [251792692],
            [79094888],
            [267389735, 82841860, 267651166, 250793668, 233835785, 267665210, 99680277, 133170194, 124782119]
        ]  # Manually calculated encoded value

        for index, input_string in enumerate(input_strings):
            expected_encoded = expected_encodeds[index]
            encoded = encode(input_string)
            self.assertEqual(encoded, expected_encoded, "Encoded output does not match expected format.")

    def test_decode_output(self):
        """
        Test if the decoding process reconstructs the original string.
        """
        encoded_inputs = [
            [16777217],
            [251792692],
            [79094888],
            [267389735, 82841860, 267651166, 250793668, 233835785, 267665210, 99680277, 133170194, 124782119]
        ]

        expected_outputs = [
            "A",
            "FRED",
            " :^)",            
            "egad, a base tone denotes a bad age"
        ] # Manually calculated decoded value

        for index, encoded_input in enumerate(encoded_inputs):
            expected_output = expected_outputs[index]
            decoded = decode(encoded_input)
            self.assertEqual(decoded, expected_output, "Decoded output does not match expected string.")

    def test_edge_cases(self):
        """
        Test edge cases like empty strings and special characters.
        """
        # Empty string
        self.assertEqual(encode(""), [], "Encoding an empty string should return an empty list.")
        self.assertEqual(decode([]), "", "Decoding an empty list should return an empty string.")

        # Special characters
        special_string = "!@#$%^&*()_+"
        encoded = encode(special_string)
        decoded = decode(encoded)
        self.assertEqual(decoded, special_string, "Failed for special characters.")

       # Unicode characters
        unicode_string = "😊🚀"
        encoded = encode(unicode_string)
        decoded = decode(encoded)
        self.assertEqual(decoded, unicode_string, "Failed for Unicode characters.")

if __name__ == "__main__":
    unittest.main()
