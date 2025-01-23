def encode_string(stringToEncode):
    """
    Encodes a given string into a list of integers using a custom encoding scheme.
    
    The encoding process groups characters into 4-character segments, 
    shifting their ASCII values into an integer buffer. Each segment is 
    combined into a single integer, which is then transformed into the 
    final encoded output.

    @param stringToEncode: The string to be encoded.
    @return: A list of integers representing the encoded string.
    """
    buffer = []  # Buffer to hold intermediate encoded values
    encoded_output = []  # Final encoded output

    # Process each character in the input string
    for index, character in enumerate(stringToEncode):
        if index % 4 == 0:
            buffer.append(0)  # Initialize a new buffer element for every 4 characters
        ascii_value = ord(character)  # Get the ASCII value of the character
        # Shift and combine the ASCII value into the appropriate buffer element
        buffer[index // 4] |= ascii_value << ((index % 4) * 8)

    # Convert buffer values to encoded output
    for value in buffer:
        encoded_value = 0  # Initialize encoded value for this buffer element
        bit_position = 0  # Bit position counter for mapping bits
        while value > 0:
            # Map the least significant bit (LSB) to the encoded value
            encoded_value |= (value & 1) << ((bit_position % 8) * 4 + (bit_position // 8))
            value >>= 1  # Shift right to process the next bit
            bit_position += 1  # Move to the next bit position
        encoded_output.append(encoded_value)  # Append the encoded value to the output list

    return encoded_output

def decode_encoded(encoded_values):
    """
    Decodes a list of integers back into the original string using the custom encoding scheme.
    
    The decoding process retrieves the original ASCII values from the encoded integers,
    reconstructing the original string by mapping the bits back to their corresponding characters.

    @param encoded_values: A list of integers representing the encoded string.
    @return: The original decoded string.
    """
    decoded_result = ""  # Final decoded string
    intermediate_buffer = []  # Buffer for intermediate decoded values

    # Process each encoded value
    for encoded in encoded_values:
        temp_value = 0  # Initialize temporary value for decoding
        for bit_index in range(32):  # Assume 32-bit encoded data
            if (encoded >> bit_index) & 1:
                # Map the bit to its corresponding position in the original character encoding
                temp_value |= (1 << (bit_index % 4) * 8 + (bit_index // 4))
        intermediate_buffer.append(temp_value)  # Append the reconstructed value to the buffer

    # Convert intermediate buffer to decoded string
    for value in intermediate_buffer:
        for segment in range(4):
            # Extract ASCII value from each segment
            ascii_val = (value >> (segment * 8)) & 0xFF
            if ascii_val != 0:  # Skip null characters
                decoded_result += chr(ascii_val)  # Append the character to the result

    return decoded_result
