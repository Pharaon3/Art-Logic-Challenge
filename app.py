"""
   Flask Web Application for Custom String Transformation
   This app encodes and decodes strings using a custom transformation scheme.
"""

from flask import Flask, render_template, request
from base import encode_custom, decode_custom, is_ascii_only

# Initialize Flask app instance
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def transform_string():
   """
   Manages the transformation (encoding and decoding) of input strings.

   Handles both GET and POST requests:
     - GET: Renders the main page.
     - POST: Retrieves the input string, encodes it, and decodes it for validation.

   Returns:
      A rendered HTML page displaying the input, encoded result, 
      and decoded string (if successful).
   """
   original_text = ""  # Stores user-provided string
   encoded_output = None  # Encoded representation of the string
   decoded_output = None  # Reconstructed original string after decoding
   error_message = None  # Holds error message if the input is invalid

   if request.method == 'POST':
      original_text = request.form.get('inputString', '')  # Fetch user input
      if is_ascii_only(original_text):  # Validate ASCII-only characters
         encoded_output = encode_custom(original_text)  # Perform encoding
         decoded_output = decode_custom(encoded_output)  # Decode to verify correctness
      else:
         error_message = "The input is not compatible with ASCII encoding."

   # Render the HTML page with results
   return render_template(
      'template.html',
      original_text=original_text,
      encoded_output=encoded_output,
      decoded_output=decoded_output,
      error_message=error_message
   )

# Launch the Flask application
if __name__ == '__main__':
   app.run(debug=True)
