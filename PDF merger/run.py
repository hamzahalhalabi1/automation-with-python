import os
from PyPDF2 import PdfMerger

def combine_pdfs(input_folder, output_filename):
    # Create a PdfMerger object
    merger = PdfMerger()

    # List all PDF files in the input folder
    pdf_files = [f for f in os.listdir(input_folder) if f.endswith('.pdf')]

    # Sort the PDF files (optional, if you want to combine them in a specific order)
    pdf_files.sort()

    # Append each PDF file to the merger
    for pdf in pdf_files:
        merger.append(os.path.join(input_folder, pdf))

    # Write out the merged PDF
    merger.write(output_filename)
    merger.close()
    print(f"All PDFs combined into {output_filename}")

if __name__ == "__main__":
    input_folder = "path/to/your/pdf/folder"  # Replace with the path to your folder containing PDFs
    output_filename = "combined.pdf"  # Replace with the desired output filename
    combine_pdfs(input_folder, output_filename)
