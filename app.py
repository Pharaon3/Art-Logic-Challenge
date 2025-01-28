"""
    Flask Application for String Encoding and Decoding
    This application encodes and decodes strings using a custom encoding scheme.
"""
from flask import Flask, render_template, request
from convert import custom_encode, custom_decode, check_ascii

# Initialize the Flask application
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_encoding():
   """
   Handles the encoding and decoding of input strings.
   
   This function processes both GET and POST requests. For GET requests,
   it renders the initial page. For POST requests, it retrieves the string
   from the form, encodes it, and decodes it back for verification.
   
   Returns:
      A rendered HTML page with the input string, encoded result, 
      and decoded string if applicable.
   """
   input_string = ""  # Stores the input string from the user
   encoded_result = None  # Encoded output as a list of integers
   decoded_result = None  # Decoded string from the encoded result
   err_txt = None # Error text

   if request.method == 'POST':
      input_string = request.form.get('inputString', '')  # Retrieve the input string
      if check_ascii(input_string):  # Ensure the input is not empty
         encoded_result = custom_encode(input_string)  # Perform encoding
         decoded_result = custom_decode(encoded_result)  # Perform decoding for verification
      else:
         err_txt = "It is not ASCII-compatible."

   # Render the template with the results
   return render_template(
      'encode.html',
      input_string=input_string,
      encoded_result=encoded_result,
      decoded_result=decoded_result,
      err_txt=err_txt
   )

# Run the Flask application
if __name__ == '__main__':
   app.run(debug=True)
