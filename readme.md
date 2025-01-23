# String Encoding and Decoding Project (Flask)

## Overview
This project implements a custom string encoding and decoding mechanism, built with Python and Flask. The encoding process transforms a string into a list of integers, while the decoding process reconstructs the original string from those integers. A simple Flask-based web interface is provided for users to encode and decode strings interactively.

---

## Features
- **Custom Encoding Scheme**: Converts strings into lists of integers using bitwise operations.
- **Accurate Decoding**: Reconstructs the original string from the encoded integers.
- **Web Interface**: User-friendly Flask application for encoding and decoding strings.
- **Command-Line Interface (CLI)**: Test encoding and decoding directly via a CLI.

---

## Installation

Follow these steps to set up the project:

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the Flask application:
    ```bash
    python app.py
    ```

---

## Usage

### Flask Web Interface
1. Launch the Flask application:
    ```bash
    python app.py
    ```
2. Open your browser and navigate to:
    ```
    http://127.0.0.1:5000/
    ```
3. Enter a string in the text box and submit to see the encoded integers and decoded string.

### Command-Line Interface (CLI)
To test the encoding and decoding functionality via the command line:
```bash
python test.py
