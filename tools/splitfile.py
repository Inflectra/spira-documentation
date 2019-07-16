import sys
import re

src_file = "../temp/" + sys.argv[1] + "/" + sys.argv[1] + ".md"

header_regex = re.compile("^#[ ]+")
filename_regex = re.compile("[/:]+")
number_regex = re.compile("#+ +[0-9.]+ ")


def main():
    f = open(src_file, "r")
    for line in f:
        # Remove numbering from headings, so ## 1.2 VSCode -> ## VSCode
        line = number_regex.sub(
            "#" * line.count("#") + " ", line) if number_regex.search(line) else line

        # If line has an H1, start a new file
        if header_regex.search(line):
            # If file has been defined, close it and prepare for a new one
            try:
                new_file
            except:
                pass
            else:
                new_file.close()
            # Remove offending characters and pound signs
            file_name = str.rstrip(filename_regex.sub(
                "", header_regex.sub("", line))) + ".md"
            if len(file_name) > 3:
                # Create a new file with the same name as the heading
                new_file = open(
                    "../temp/" + sys.argv[1] + "/" + file_name, "w")
                new_file.write(line)
        else:
            try:
                new_file.write(line)
            except:
                pass

    try:
        new_file.close()
    except:
        pass


main()
