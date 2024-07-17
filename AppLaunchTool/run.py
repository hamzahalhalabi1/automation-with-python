import os
import subprocess

def open_programs_from_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            program = line.strip()
            if os.path.exists(program):  # Check if it's a file path
                subprocess.Popen([program], shell=True)
            else:  # Assume it's a program name
                subprocess.Popen(['start', program], shell=True)

def main():
    script_directory = os.path.dirname(os.path.realpath(__file__))
    text_file = 'programs_list.txt'
    file_path = os.path.join(script_directory, text_file)

    if os.path.exists(file_path):
        open_programs_from_file(file_path)
    else:
        print(f"Error: {text_file} not found in the script directory.")

if __name__ == "__main__":
    main()
