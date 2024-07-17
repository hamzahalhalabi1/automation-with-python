import os
import csv

def process_directory(directory, script_directory, writer):
    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for name in files:
            writer.writerow([name, 'File'])
        for name in dirs:
            writer.writerow([name, 'Folder'])
            subdirectory = os.path.join(root, name)
            process_directory(subdirectory, script_directory, writer)
        # Add an empty row to denote end of directory content
        writer.writerow([])

if __name__ == "__main__":
    directory = input("Enter the directory path: ")
    script_directory = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(script_directory, "directory_contents.csv")
    
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Type'])  # Writing headers
        process_directory(directory, script_directory, writer)
    
    print("CSV file created successfully.")
