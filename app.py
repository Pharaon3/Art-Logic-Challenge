from flask import Flask, render_template, request
from convert import encode_string, decode_encoded

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def encode_view():
    stringToEncode = ""
    encoded_dec = None
    decoded_string = None

    if request.method == 'POST':
        stringToEncode = request.form.get('stringToEncode', '')
        encoded_dec = encode_string(stringToEncode)
        decoded_string = decode_encoded(encoded_dec)

    return render_template('encode.html', 
                           stringToEncode=stringToEncode, 
                           encoded_dec=encoded_dec, 
                           decoded_string=decoded_string)

if __name__ == '__main__':
    app.run(debug=True)
