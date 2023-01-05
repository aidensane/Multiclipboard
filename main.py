import sys
import clipboard
import json


def save_items(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


def load_items(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)


if len(sys.argv) == 2:
    command = sys.argv[1]
    print(command)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()

        print("save")
    elif command == "load":
        print("load")
    elif command == "list":
        print("list")
    else:
        print("Unknown command")
else:
    print("Please pass exactly one command")
