"""
Renames image files to be the same as the file they're referenced in
Command line arguments:
arg 1: Name of the folder being processed
arg 2: Name of the .md file being processed (NOT INCLUDING .md)
"""
import collections
import math
import os
import re
import shutil
import sys


src_folder = "../temp/" + sys.argv[1]
dst_folder = "../temp/" + sys.argv[1] + "/img"
img_regex = re.compile(r"image[0-9]+[.pngjpeg]+", re.IGNORECASE)
data: list

# Names of images used in this file
image_names = []


def main():
    global data
    # Get the name of the images in the file
    with open("../temp/" + sys.argv[1] + "/" + sys.argv[2] + ".md", "r") as file:
        data = file.readlines()
    for l in data:
        result = img_regex.search(l)
        if(result):
            image_names.append(result.group(0))

    print(str(image_names))
    if not os.path.isdir(dst_folder):
        os.mkdir(dst_folder)
    process_all()

    # Update the file
    with open("../temp/" + sys.argv[1] + "/" + sys.argv[2] + ".md", "w") as file:
        file.writelines(data)


def process_all():
    files = os.listdir(src_folder + "/media")
    for f in files:
        # Only want to process images in the file being processed
        if not f.endswith(".md") and not f == "img" and f in image_names:
            process(f)


def process(f_name):
    # Name of the new file, subbing out spaces for underscores
    new_name = (sys.argv[2] + f_name.replace("image", "_")).replace(" ", "_")
    dst_file = dst_folder + "/" + new_name
    print(dst_file)
    shutil.copyfile("../temp/" + sys.argv[1] + "/media/" + f_name, dst_file)
    # Replace link in file with new filename
    data[:] = [l.replace(sys.argv[1] + "/media/" + f_name, "img/" + new_name)
               for l in data]


main()
