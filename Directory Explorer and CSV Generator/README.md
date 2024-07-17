

# Directory Explorer and CSV Generator

## Overview
The Directory Explorer and CSV Generator is a Python script that allows you to explore the contents of a directory and its subdirectories. It generates a CSV file containing the names of all files and folders within the specified directory, organized in a hierarchical structure.

## Features
- Recursively explores a directory and its subdirectories.
- Generates a CSV file containing the names of files and folders, along with their types (file or folder).
- Output CSV file is formatted for easy analysis and manipulation.

## How to Use
1. **Installation**: 
   - Ensure you have Python installed on your system.
   - Download or clone the script to your local machine.

2. **Usage**:
   - Run the script using Python.
   - Input the directory path when prompted.
   - The script will generate a CSV file named `directory_contents.csv` in the same directory as the script.

3. **Output**:
   - The generated CSV file will contain two columns: `Name` and `Type`.
   - The `Name` column includes the names of files and folders.
   - The `Type` column specifies whether each entry is a file or a folder.

## Example
Suppose you have a directory named `example_directory` with the following structure:
```
example_directory/
    ├── file1.txt
    ├── folder1/
    │   ├── file2.txt
    │   └── file3.txt
    └── folder2/
        └── file4.txt
```

Running the script and providing `example_directory` as input will generate a CSV file with the following content:
```
Name,Type
file1.txt,File
folder1,Folder
file2.txt,File
file3.txt,File
folder2,Folder
file4.txt,File
```

## Dependencies
- Python 3.x
- No additional dependencies required.

## License
Refrence me please :_)