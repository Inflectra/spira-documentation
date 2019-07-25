"""
This simple script uses git to rename all the documentation files to use dashes instead of spaces in the name
After running this you will need to run a find and replace from '%20' to '-'
"""

import subprocess
import os

docs_dir = "../docs/"


def main():
    # Get the contents of the docs directory
    contents = os.listdir(docs_dir)
    for f in contents:
        process(f, docs_dir)

# Recursively process a given folder/file


def process(file_name, path):
    if os.path.isdir(path + file_name):
        # Recursively process the directory
        for f in os.listdir(path + file_name):
            process(f, path + file_name + "/")
    else:
        if " " in file_name:
            print("Renaming " + file_name + " to " +
                  file_name.replace(" ", "-"))
            subprocess.call("git mv \"" + path + file_name +
                            "\" " + path + file_name.replace(" ", "-"))


main()
