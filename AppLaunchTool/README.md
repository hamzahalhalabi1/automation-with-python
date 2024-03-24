# App Launch Tool

App Launch Tool is a Python script that simplifies the process of launching programs directly from the command line. It is particularly useful for programs with multi-word names.

## Features

- Quickly launch programs from the command line.
- Handles programs with multi-word names seamlessly.
- Easy to use and customizable.

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/hamzahalhalabi1/automation-with-python.git
    ```

2. Navigate to the `AppLaunchTool` directory:

    ```bash
    cd automation-with-python/AppLaunchTool
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use the App Launch Tool, follow these steps:

1. Open the command prompt or terminal.
2. Navigate to the `AppLaunchTool` directory.
3. Run the script followed by the name of the program you want to launch. If the program name consists of multiple words, enclose it in double quotation marks.

    Example:
    ```bash
    chrome
    C:\Users\hamza\AppData\Local\Programs\Microsoft VS Code\Code.exe
    etc..
    ```

## Configuration

You can customize the behavior of the App Launch Tool by modifying the `launcher.py` script according to your requirements.

## Limitations

Some file names can be tricky and not run as expected so you have to find the name of the real file manually or copy the path. Aditionally running Microsoft default apps have their own syntax so you have to keep that in mind.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or create a pull request.

## License

You can use this program but try to refrence me somehow :)
