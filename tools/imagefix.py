import collections
import math
import os
import re
import shutil
import sys

src_folder = "../temp/" + sys.argv[1]
dst_folder = "../temp/" + sys.argv[1] + "/img"


def main():
    if not os.path.isdir(dst_folder):
        os.mkdir(dst_folder)
    process_all()


def process_all():
    files = os.listdir(src_folder)
    for f in files:
        if not f.endswith(".md") and not f == "img":
            process(f)


def process(f_name):
    print(f_name)
    files = os.listdir(src_folder + "/" + f_name)
    for f in files:
        src_file = src_folder + "/" + f_name + "/" + f
        print(src_file)
        dst_file = dst_folder + "/" + sys.argv[1] + f.replace("image", "")
        print(dst_file)
        shutil.copyfile(src_file, dst_file)


main()
