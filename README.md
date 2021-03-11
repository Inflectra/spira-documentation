# Getting Started
This documentation uses [MkDocs](https://www.mkdocs.org/) - documentation using Markdown. This is an open source system that takes a folder system of markdown files with associated files (eg images) and renders them into HTML with nice features like site navigation and search, and on page navigation. It is similar to other services like Jekyll or OctoPress, but it is focused on documentation, not blogging.

We can fully change the theme used and its features using a basic templating language and normal CSS. If needed you can insert HTML into the Markdown files and it will get passed through as HTML.


## The broad workflow:
- write and edit in markdown
- make sure new pages are accessible using the main navigation (in the mkdocs.yml)
- check that there are no broken images or links
- save, commit, and push your changes to Github - this gets the source code of our documentation in place
- deploy from a local machine using a simple command from the command line to build, commit, push, and deploy the rendered files to Github
- Github hosts these deployed files as a static site

## Git workflow
- Quick fixes should be done on master - eg typos
- New pages or larger changes should be done in a branch off master (eg. reporting-pages)
- There is a special branch called "gh-pages" that you should NEVER touch. It is the deployment branch and is handled automatically by MkDocs. 


## Getting the build environment set up
1. Refer to [MkDocs](https://www.mkdocs.org/#installation) to install Python, pip, then MkDocs
2. Run `pip install -r requirements.txt` to install everything our base theme needs - it should also install MKdocs
3. Clone this repo to your local machine
4. Edit files as needed
5. Run `npm install broken-link-checker -g` (need node and npm for this) - used for checking for broken links before deployment. For more info see [here](https://matthewsetter.com/writing-tools/npm-broken-link-checker/)


# Working with the docs and Markdown
- [How to create files and style them](https://www.mkdocs.org/user-guide/writing-your-docs/)
- Markdown is a straightforward way to write human readable text that renders to display HTML headings, **bold**, *italics*, links, images, numbered lists, bulleted lists, tables, line breaks, and code blocks.
- To make a paragraph make sure to leave an empty line between paragraphs (ie press return twice)
- You don't need to leave an empty line between list items
- You can have a list that has differently indented levels. Make sure each new indent uses 4 spaces
- Using MkDocs you can also make links to places in other files in the documentation which is really handy



# Key commands
- **Running a local test server**: from the current branch, run `mkdocs serve`. The web server should be available at localhost:8000
- **Edit and commit your documentation changes**: files can be edited and committed straight on Github, and created, deleted, or edited from the desktop. Work in the relevant branch (master to make the changes live) and commit code as normal using Git. 
- **CHECK FOR ERRORS**:

    - run `mkdocs build` - this will show pages not linked in the navigation (likely fine) and images broken links that you can then repair
    - run `mkdocs serve` then in a new terminal window run `blc http://localhost:8000/About/release-notes-v6 -ro -e`. This checks for internal links only
    - once this has finished (will take a few minutes) search in the output for "─BROKEN─". This will give you the bad link and you can see above the page the link is on (the line above starting "Getting links from: http://localhost:8000...").
    - you can separately run `blc http://localhost:8000/About/release-notes-v6 -ro -i` to check for external broken links but this will throw lots of errors on things like twitter on every page

- **Deploy to to GitHub Pages**: from the local machine when on the master branch, run `mkdocs gh-deploy` and that's it! Your changes should be live after the command finishes!


# Maintenance Operations

Can run `mkdocs build --clean`. After some time, files may be removed from the documentation but they will still reside in the site directory. Run this command to remove those stale files.

## Delete Unused Pictures
From the tools directory, run the command `python .\unusedimgs.py`. This will generate a list of commands you can paste into the console to delete the file. ***PLEASE READ LIMITATIONS BEFORE YOU PROCEED AND DELETE IMAGES*** 


### Limitations
- If an image name has a parenthesis in it (like `Importing_from_Microsoft_Excel_(Office365)_24.png`), the script will print it out no matter what. Please review them before you delete in case they are actually used.
- If the image reference is across multiple lines (like the example below), the image will be printed out. Please move the reference to one line and run the command again and it should disappear.

```
...

![Git stores data as snapshots of the project over time.](img/Using_Git_47.png)

...
```
 


## REGEXes to tidy up the markdown files
* To combine paragraphs split across multiple lines: `([A-Za-z",\*<>\. 0-9&\(\)])\n([A-Za-z",\*<>\. 0-9&\(\)])` => `$1 $2`
* To get rid of extra line breaks: `\n\n\n` => `\n\n` and run until it can't be run anymore
* To add spacing before headings: `\n#` => `\n\n#`



# Conversion processes

## MD to PDF
1. Install [MiTeX](https://miktex.org/howto/install-miktex)
2. Install pyyaml with `pip install pyyaml`
3. Review the `convert` array in `createpdf.py`, which will automatically convert toplevel items in the `nav` in `mkdocs.yml` to a PDF. Each toplevel entry will get its own PDF. 
4. Review `Admin Guide.yml` and `User Manual.yml` in the tools directory. These contain the formatting for the header and footer
    - `\fancyhead[LO,LE]{SpiraPlan Administration Guide}` will put `SpiraPlan Administration Guide` in the top 
    (`fancyhead`) left (`[L*,L*]`) of odd and even pages (`[*O,*E]`)
    - `\fancyfooter` works the same
5. In the tools directory, run the command `python .\createpdf.py`
 
**Possible Issues**: If a line starts with a file/folder URI (ex. C:\WINDOWS), the script will error out. Just find the ofending line in the markdown and format it in some way (wrapping it with grave marks (\`) to make it format as code works well.)


## docx to MD (used to create these docs)
1. Install mkdocs with `pip install mkdocs`, if you haven't already. Note that you need [pip](https://pip.pypa.io/en/stable/installing/) and Python for this to work. 
2. [Install Pandoc](https://pandoc.org/installing.html)
3. In the tools directory, paste the .docx files you would like to convert. Note that only .docx files will be converted - if you have a .doc or another format, either save it as a docx or convert it manually
4. In a shell, `cd` to tools and run `python .\spiraconvert.py options` where options is either 'auto' (`python .\spiraconvert.py auto`) or the names of the files you would like to convert without the file extension (`python .\spiraconvert.py "SpiraTestPlanTeam IDE Integration Guide" "SpiraTestPlanTeam External Bug Tracking Integration Guide" "SpiraTest-Team Automated Testing Integration Guide"`)
5. The script will run, copying iles into the `./temp` folder in the root directory as it goes. These markdown files and the images should be pasted into the `./docs` directory in the apropriate folders.
6. Review the files for weirdness (more information below)
7. Put all the new files in mkdocs.yml where you would like. The `nav` property will generate the top navbar in the structure you define. Run `mkdocs serve` to test it out, which can be viewed at http://127.0.0.1:8000/


### Conversion Problems
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