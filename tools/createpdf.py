"""
Convert markdown files to PDF automatically. Some formatting may be weird, 
but it should work for the most part
"""

import yaml
import shutil
import subprocess

# Heading names in the YAML file to convert to PDF
convert = ["User Manual", "Admin Guide"]
docs_location = "../docs/"


def main():
    # Open the MKDocs config file
    config = yaml.safe_load(open("../mkdocs.yml")).get("nav")
    # Overall section in the nav (like User Manual, Quick Start Gude, Integrations, etc)
    for section in config:
        for heading in convert:
            if heading in section:
                # Get the list of files to convert, in order
                files = process(section[heading])
                # Find the folder they're in and copy them to this directory
                folder = files[0][:files[0].rfind('\\')]
                folder_to_copy = docs_location + folder
                # Copy the files, we will delete them once we're done
                shutil.copytree(folder_to_copy, folder)
                # Print the command being run
                print("pandoc -s \"" + "\" \"".join(files).replace(folder + "\\", "") +
                      "\" -o " + folder + ".pdf")
                # Actually convert the files in order
                subprocess.call("pandoc -s \"" + "\" \"".join(files).replace(folder + "\\", "") +
                                "\" -o " + folder + ".pdf", cwd=folder)
                # Copy the new PDF to the root of the tools directory
                shutil.copyfile(folder + "/" + folder +
                                ".pdf", folder + ".pdf")
                # Remove any unused files
                shutil.rmtree(folder)


# Process each section - this will return a list of the files to convert recursively
def process(to_convert):
    to_return = []
    for file_object in to_convert:
        for atr in file_object:
            # Either the name of the file or another list, which will be processed recursively
            file_name = file_object[atr]
            if type(file_name) == list:
                to_return.extend(process(file_name))
            else:
                to_return.append(file_name)
    return to_return


main()
