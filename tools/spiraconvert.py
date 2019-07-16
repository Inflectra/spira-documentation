r"""
Converts word documents to markdown and images in the ../temp folder
NOTE: This will only work with .docx files. .doc files will need to be converted first or done manually 
Command line arguments:
Either auto (like python spiraconvert.py auto) or all of the file names (excluding extension) 
you would like to convert, like python .\spiraconvert.py "SpiraTestPlanTeam IDE Integration Guide" 
    "SpiraTestPlanTeam External Bug Tracking Integration Guide" "SpiraTest-Team Automated Testing Integration Guide"
"""
import re
import sys
import os
import shutil
import subprocess

parameters = sys.argv[1:]

# Make temp dir if it doesn't already exist
if not os.path.isdir("../temp"):
    os.mkdir("../temp")

# If auto, retrieve all of the docx files
if parameters[0] == "auto":
    parameters = []
    files = os.listdir(".")
    for f in files:
        if f.endswith(".docx"):
            parameters.append(f.replace(".docx", ""))

for file in parameters:
    # Convert the docx to .md
    subprocess.call("convdocx.cmd \"" + file + ".docx\"")
    # Replace the spaces with underscores as that's what pandoc does
    converted_name = re.compile(" ").sub("_", file)
    # Copy the MD and images into temp
    shutil.copytree(converted_name, "../temp/" + converted_name)
    shutil.copyfile(converted_name + ".md", "../temp/" +
                    converted_name + "/" + converted_name + "_OLD.md")

    # Remove leftover word formatting
    subprocess.call("python postprocess.py " + converted_name)
    # Delete the old markdown file
    os.remove("../temp/" + converted_name + "/" + converted_name + "_OLD.md")
    subprocess.call("python splitfile.py " + converted_name)

    # Rename images in each new file
    files = os.listdir("../temp/" + converted_name)
    for f in files:
        if f != "img" and f != "media" and f != converted_name + ".md":
            subprocess.call("python imagefix.py " + converted_name +
                            " \"" + f.replace(".md", "") + "\"")

    # Delete the old media folder
    shutil.rmtree("../temp/" + converted_name + "/media")
    # Delete the big markdown file
    os.remove("../temp/" + converted_name + "/" + converted_name + ".md")

    # Clean up the tools folder
    shutil.rmtree(converted_name)
    os.remove(converted_name + ".md")
