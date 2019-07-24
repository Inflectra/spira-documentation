import os
import re

root_folder = "../docs"
src_folder = root_folder
link_regex = re.compile(r"\[[^\]]*\]\([^\)]+\)", re.IGNORECASE)
ref_regex = re.compile(r"\[([^\]]*)\]\(([^\)]+)\)", re.IGNORECASE)

file_set = set()


def main():
    global src_folder
    directories = os.listdir(root_folder)
    for directory in directories:
        if os.path.isdir(root_folder + "/" + directory):
            src_folder = root_folder + "/" + directory
            process_all()
            check_files()


def check_files():
    files = os.listdir(src_folder + "/img")
    for f in files:
        if "img/" + f not in file_set:
            print("del " + src_folder + "/img/" + f)


def process_all():
    files = os.listdir(src_folder)
    for f in files:
        if f.endswith(".md"):
            process(f)


def process(file_name):
    with open(src_folder + "/" + file_name, encoding='utf-8') as input:
        for line in input:
            links = link_regex.findall(line)
            if len(links) > 0:
                for link in links:
                    match = ref_regex.match(link)
                    title = match.group(1)
                    href = match.group(2)

                    if href.startswith("img/"):
                        file_set.add(href)


main()
