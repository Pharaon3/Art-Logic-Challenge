# Flask-Based String Transformer

A Python project that provides a custom string encoding and decoding mechanism, along with a simple Flask-based web interface for interactive usage.

---

## Features

- **Custom Encoding**: Converts strings into a sequence of integers using bitwise operations.
- **Accurate Decoding**: Reconstructs the original string from its encoded numerical representation.
- **Web Interface**: A user-friendly Flask application to encode and decode strings interactively.
- **Command-Line Interface (CLI)**: Supports direct encoding and decoding from the command line.

---

## Installation

1. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

### Flask Web Interface
1. Start the Flask server:
    ```bash
    python app.py
    ```
2. Open your web browser and go to:
    ```
    http://127.0.0.1:5000/
    ```
3. Input your string in the text box and submit it to see the encoded and decoded results.

### Command-Line Interface
Run the command line script to encode and decode a sample string:
```bash
python cli.py
```

### Testing
To run the tests, use the unittest module:
```bash
python -m unittest test.py
```

### Limitations
The encoding process assumes that the input string is ASCII-compatible.


## Project Structure
- app.py: Main Flask application.
- transformer.py: Contains encoding and decoding logic.
- cli.py: CLI for encoding and decoding.
- test.py: Unit tests for encoding and decoding.
- templates/: HTML templates for the Flask web interface.
- requirements.txt: Dependencies for the project.