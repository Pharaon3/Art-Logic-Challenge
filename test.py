from convert import encode_string, decode_encoded
stringToEncode = input("String To Encode: ")
EncodedDec = encode_string(stringToEncode)
print(EncodedDec)
DecodedString = decode_encoded(EncodedDec)
print(DecodedString)