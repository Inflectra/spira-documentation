1. Install mkdocs with `pip install mkdocs`, if you haven't already. Note that you need [pip](https://pip.pypa.io/en/stable/installing/) for this to work
2. In the tools directory, paste the .docx files you would like to convert. Note that only .docx files will be converted - if you have a .doc or another format, either save it as a docx or convert it manually
3. In powershell, `cd` to tools and run `python .\spiraconvert.py options` where options is either 'auto' (`python .\spiraconvert.py auto`) or the names of the files you would like to convert without the file extension (`python .\spiraconvert.py "SpiraTestPlanTeam IDE Integration Guide" "SpiraTestPlanTeam External Bug Tracking Integration Guide" "SpiraTest-Team Automated Testing Integration Guide"`)
4. The script will run, copying iles into the `./temp` folder in the root directory as it goes. These markdown files and the images should be pasted into the `./docs` directory in the apropriate folders.
5. Review the files for weirdness (more information below)
6. Put all the new files in mkdocs.yml where you would like. The `nav` property will generate the top navbar in the structure you define. Run `mkdocs serve` to test it out, which can be viewed at http://127.0.0.1:8000/


## Conversion Problems
- Table formatting is generally a huge pain and needs to be done manually
- Code usually isn't formatted and generally has excessive escape characters (I just pasted the code directly from word as it was easier)
- The script will spit out an uneccesary `Introduction` or `Legal` file if it was present or put a legal notice in the `.md` file who's corresponding section in the word file was at the bottom of the word file.
- Unnecessary escape characters: Just do a find and replace in your editor of choice in the `docs\` directory with the criteria below:
    - \\< to <
    - \\> to > **IFF THE OCCURANCE IS IN A CODE BLOCK, OTHERWISE NECESSARY** 
    - \\" to "
    - \\' to '
    - \\@ to @
    - ^®^ to <sup>®</sup>
    - ^1^ to <sup>1</sup>
    - \$ to $