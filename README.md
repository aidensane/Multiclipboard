# Multiclipboard
This is a simple clipboard manager program written in Python that allows users to save and load data to and from the clipboard using command-line arguments.

# How it works
The program reads in a command-line argument and based on the argument, either saves, loads, or lists data that has been copied to the clipboard. Data is saved to a JSON file, and the clipboard library is used to interact with the clipboard.

# Usage
To use the program, run the script and pass in one of the following commands as an argument:

1. save: saves the data currently in the clipboard to a JSON file using a key
2. load: loads the data from the JSON file based on the provided key and copies it to the clipboard
3. list: lists all saved data and their corresponding keys
# Requirements
1. Python 3.x
2. clipboard library (can be installed using pip)
