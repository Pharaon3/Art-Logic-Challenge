# String Encoding and Decoding Project (Flask)

## Overview
This project provides a custom implementation of string encoding and decoding using Python and Flask. The encoding mechanism transforms strings into lists of integers, and the decoding mechanism accurately reconstructs the original string. Users can interact with these features through a web-based interface or a command-line interface (CLI).

---

## Features
- **Custom Encoding**: Converts strings into lists of integers using bitwise operations.
- **Accurate Decoding**: Reconstructs the original string from the encoded integers.
- **Interactive Web Interface**: User-friendly Flask application for string transformation.
- **Command-Line Utility**: Test and use encoding/decoding functionality via a CLI.

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
2. Open your web browser and navigate to:
    ```
    http://localhost:5000/
    ```
3. Enter a string in the input field and submit the form to see the encoded and decoded results.

### Command-Line Interface (CLI)
To test the encoding and decoding functionality via the command line:
```bash
python cli.py
```

### Testing
To run the unit tests and validate the encoding/decoding functionality:
```bash
python -m unittest test.py
```

---

## Project Structure
```
project-root/
├── app.py          # Flask application for web interface
├── base.py         # Core encoding and decoding logic
├── cli.py          # Command-line interface for testing
├── test.py         # Unit tests for validation
├── templates/
│   └── template.html # HTML template for the web interface
├── requirements.txt # Project dependencies
└── README.md       # Project documentation
```

---
