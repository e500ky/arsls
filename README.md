# ARSLS - Link Shortener

## Description
ARSLS (ArsTech Link Shortener) is a simple and efficient URL shortener built using Python and CustomTkinter. This application allows users to shorten long URLs quickly and easily, with an intuitive GUI.

## Features
- User-friendly graphical interface
- Instant URL shortening using TinyURL
- Copy the shortened URL to the clipboard with a single click
- Keyboard shortcut support for quick conversion

## Requirements
Make sure you have Python installed on your system. Additionally, install the required dependencies:

```sh
pip install customtkinter pyshorteners pyperclip
```

## Usage
1. Run the application:
   ```sh
   python main.py
   ```
2. Enter the URL you want to shorten in the input field.
3. Press the "Convert" button or press `Enter`.
4. Click on the shortened URL field to copy it to the clipboard.

## Code Structure
- `Shorter` class: Handles URL shortening using the TinyURL API.
- `GUI` class: Defines the application window and GUI components.
- `convert()` function: Converts the input URL into a shortened version and displays it.

## License
This project is licensed under the MIT License.

## Author
Developed by ArsTech.
