# PDF Merger Tool

PDF Merger Tool is a simple Python script that combines multiple PDF files into a single PDF file. This tool is useful for merging multiple documents into a single file for easier handling and distribution.

## Features

- Combines all PDF files in a specified folder into a single PDF file.
- Simple and easy-to-use script.

## Prerequisites

- Python 3.6 or higher
- PyPDF2 library

## Installation

1. Make sure you have Python installed. You can download it from [python.org](https://www.python.org/).

2. Install the PyPDF2 library using pip:
    ```bash
    pip install PyPDF2
    ```

## Usage

1. Clone or download this repository to your local machine.

2. Navigate to the directory where the script is located.

3. Open the `combine_pdfs.py` script and update the `input_folder` and `output_filename` variables:
    ```python
    if __name__ == "__main__":
        input_folder = r"C:\path\to\your\pdf\folder"  # Replace with the path to your folder containing PDFs
        output_filename = "combined.pdf"  # Replace with the desired output filename
        combine_pdfs(input_folder, output_filename)
    ```

4. Run the script:
    ```bash
    python combine_pdfs.py
    ```

5. The combined PDF will be created in the same directory as the script with the specified output filename.

## Example

If you have a folder with the following PDFs:

- document1.pdf
- document2.pdf
- document3.pdf

After running the script, you will get a single file named `combined.pdf` containing all the pages from `document1.pdf`, `document2.pdf`, and `document3.pdf`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to improve the project.

## Acknowledgements

- [PyPDF2](https://pypi.org/project/PyPDF2/) library for handling PDF operations.
