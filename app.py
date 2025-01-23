"""
Flask Application for String Encoding and Decoding

This application provides a web interface to encode and decode strings
using a custom encoding scheme.
"""
from flask import Flask, render_template, request
from convert import custom_encode, custom_decode

# Initialize the Flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def encode_decode_handler():
   """
   Manages string encoding and decoding via HTTP requests.

   - For GET requests: Renders the input form.
   - For POST requests: Processes the input string to encode it into a list
     of integers and decodes it back to verify correctness.

   Returns:
      Rendered HTML template displaying the input, encoded, 
      and decoded results (if applicable).
   """
   input_text = ""  # User's input string
   encoded_output = None  # Encoded list of integers
   decoded_output = None  # Decoded string after encoding

   if request.method == 'POST':
      # Retrieve the input string from the form
      input_text = request.form.get('inputString', '').strip()
      if input_text:  # Proceed only if the input is not empty
         encoded_output = custom_encode(input_text)  # Encode the input
         decoded_output = custom_decode(encoded_output)  # Decode for verification

   # Render the template with results
   return render_template(
      'ui.html',
      input_text=input_text,
      encoded_output=encoded_output,
      decoded_output=decoded_output
   )

# Entry point for the Flask app
if __name__ == '__main__':
   app.run(debug=True)
