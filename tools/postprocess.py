import collections
import math
import os
import re
import sys

#src_folder = "../input"
src_folder = "../temp/" + sys.argv[1]
dst_folder = "../temp/" + sys.argv[1]

link_regex = re.compile(
    r"file:///C:\\work\\Temp\\HM\\HTML\\([a-z_\-]+)\.htm", re.IGNORECASE)
img_regex = re.compile(
    r"\(([a-z0-9_\-]+)/media/image([0-9]+\.[a-z]+)", re.IGNORECASE)
size_regex = re.compile(
    r"{width=\"[0-9\.]+in\" height=\"[0-9\.]+in\"}", re.IGNORECASE)

size1_regex = re.compile(r"{width=\"[0-9\.]+in\"", re.IGNORECASE)
size2_regex = re.compile(r"height=\"[0-9\.]+in\"}", re.IGNORECASE)
underline_regex = re.compile(r"\[.+]{.underline}")


def main():
    process_all()


def process_all():
    files = os.listdir(src_folder)
    for f in files:
        if f.endswith(".md"):
            process(f)


def process(file_name):
    print(file_name)
    with open(dst_folder + "/" + re.compile("_OLD").sub("", file_name), "w+", encoding='utf-8') as output:
        with open(src_folder + "/" + file_name, encoding='utf-8') as input:
            count = 0
            for line in input:
                if line == "\n":
                    output.write(line)
                    count += 1
                    continue
                l = line.lstrip()
                if l.startswith("---") is False:
                    if count == 0:
                        ind = l.find("**   [Top]")
                        if ind > 0:
                            l = l[:ind] + "\n\n"
                        l = l.replace("**", "# ")
                    if l.startswith("[Top](file") or l.startswith("[Previous](file") or l.startswith("[Next](file"):
                        continue
                    l = link_regex.sub("../\\1/", l)
                    # l = img_regex.sub("(./img/\\1\\2", l)
                    l = size_regex.sub("\n", l)
                    l = size1_regex.sub("\n", l)
                    l = size2_regex.sub("\n", l)
                    # Remove {.underline} and associated brackets from the text
                    result = underline_regex.search(line)
                    if result:
                        start_index = line.index(result.group(0))
                        end_index = line.index("{.underline}")
                        string = line[start_index + 1:end_index - 1]
                        l = underline_regex.sub(string, line)
                    output.write(l)
                    count += 1


main()
