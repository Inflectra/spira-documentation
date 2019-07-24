"""
This file will print out commands to delete any images that are not currently in use in markdown. 
It takes no parameters and will automatically search through the docs/ folder. Here are some limitations:
- If an image name has a parenthesis in it (like `Importing_from_Microsoft_Excel_(Office365)_24.png`),
    the script will print it out no matter what. Please review them before you delete in case they are actually used.
- If the image reference is across multiple lines , the image will be printed out. 
    Please move the reference to one line and run the command again and it should disappear.
"""

import os
import re

root_folder = "../docs"
src_folder = root_folder
link_regex = re.compile(r"\[[^\]]*\]\([^\)]+\)", re.IGNORECASE)
ref_regex = re.compile(r"\[([^\]]*)\]\(([^\)]+)\)", re.IGNORECASE)

file_set = set()


def main():
    global src_folder, file_set
    # Get the directories in docs/ folder
    directories = os.listdir(root_folder)
    for directory in directories:
        file_set = set()
        if os.path.isdir(root_folder + "/" + directory):
            # Process everything in every subdirectory of docs
            src_folder = root_folder + "/" + directory
            process_all()
            check_files()


def check_files():
    files = os.listdir(src_folder + "/img")
    for f in files:
        if "img/" + f not in file_set:
            # Print out the command if the file found is not referenced anywhere
            print("del " + src_folder + "/img/" + f)


def process_all():
    # Look through every .md file in the folder currently being processed
    files = os.listdir(src_folder)
    for f in files:
        if f.endswith(".md"):
            process(f)


def process(file_name):
    with open(src_folder + "/" + file_name, encoding='utf-8') as input:
        for line in input:
            links = link_regex.findall(line)
            # Look for links in the line
            if len(links) > 0:
                for link in links:
                    match = ref_regex.match(link)
                    title = match.group(1)
                    href = match.group(2)

                    # If we found a file, add it to the set so we know not to...
                    # ...print out a delete command
                    if href.startswith("img/"):
                        file_set.add(href)


main()
