1. Install mkdocs with `pip install mkdocs`, if you haven't already. Note that you need [pip](https://pip.pypa.io/en/stable/installing/) for this to work
2. In the tools directory, paste the .docx files you would like to convert. Note that only .docx files will be converted - if you have a .doc or another format, either save it as a docx or convert it manually
3. In powershell, `cd` to tools and run `python .\spiraconvert.py options` where options is either 'auto' (`python .\spiraconvert.py auto`) or the names of the files you would like to convert without the file extension (`python .\spiraconvert.py "SpiraTestPlanTeam IDE Integration Guide" "SpiraTestPlanTeam External Bug Tracking Integration Guide" "SpiraTest-Team Automated Testing Integration Guide"`)
4. The script will run, copying iles into the `./temp` folder in the root directory as it goes. These markdown files and the images should be pasted into the `./docs` directory in the apropriate folders.
5. Review the files for weirdness (code usually isn't formatted, unecessary introduction files, legal files, etc)
6. Put all the new files in mkdocs.yml where you would like. The `nav` property will generate the top navbar in the structure you define. Run `mkdocs serve` to test it out, which can be viewed at `http://127.0.0.1:8000/`

Table formatting is a huge pain

TODO: Bug tracking, email, automated testing, version control

REGEX:
\< to <
\_ to _
\" to "
\' to '
\@ to @