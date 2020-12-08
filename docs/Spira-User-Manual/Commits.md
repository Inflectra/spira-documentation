# Commits

## Linking To Artifacts In Commit Messages
When developers are working on source code, it is often to fix a bug, create a feature described in a user story, or deal with a task. To let you trace what commits (and therefore file changes) SpiraPlan reads commit messages for links to artifacts. If SpiraPlan finds any links in the commit message it automatically creates the association between the commit and the artifact(s). You can view these associations from the [commit details](#commit-details) page, or from the associations tab of any artifact.

How does this work? The commit message has to contain one or more artifact token. For example [TK:123], or [IN:456], or [RQ:789]. These tokens are short and do not get in the way of the rest of the commit message.Artifact tokens are in the following format: `[{artifact identifier}:{artifact id}]`

The first half of the token, is a two-letter code, used throughout SpiraPlan and visible on almost every page in the application. For example, a requirement's identifier is "**RQ**". Incidents are "**IN**", and test cases are "**TC**". The artifact ID is the number of the artifact. If you go to the details page for an artifact, you will always see this artifact token near the top of the page. Clicking on it copies it to your clipboard. Then you can paste it into your commit message.

**Note:** If you forget to add the association during the commit, go to the details page for that commit in SpiraPlan, and click 'Add Association' to add the association at any time.


## Commit List
When you click on Developing \> Commits on the global navigation bar, you will be taken to the commits list screen. This shows you all commits in the current branch. You can sort and filter this list, or browse the different pages (up to 500 commits can be displayed on the page at any one time).

![](img/Source_Code_401.png)

Each commit in the list is displayed with its name, a description of what changed in the commit, the name of the person who committed the commit, and whether the commit was a change of the actual content, or just a change of the properties of the content. Clicking on the hyperlink for the commit name will take you to the [Commit Details page](#commit-details)  for that commit.

Above the main right-hand pane, there is the **branch selector**. This lets you choose which branch in the source code repository is being viewed.


## Commit Details

When you click on a commit hyperlink in either the product commit log or the file commits tab described above, you are taken to the commit details page illustrated below:

![](img/Source_Code_402.png)

This page is made up of three areas; the left pane is for navigation, the upper part of the main pane contains the details of the commit, and the bottom part of the right pane contains the list of files that were changed in this commit and the list of artifacts that the commit is associated with.

The navigation pane consists of a link that will take you back to the source code commit list, as well as a list of other commits associated with the current file. This latter list is useful as a navigation shortcut; you can quickly view the detailed information of all the peer commits by clicking on the navigation links without having to first return to the main commit list page.

The top part of the main pane allows you to view the details of this commit in the version control system, including the description of what was changed, the date that the change was made, and the name of the person who made the change.

The lower part of the main pane can be switched between two different views by clicking the appropriate tab. Initially the pane will be in "Files" mode, but it can be switched to "Associations" as well. The functionality in each of these two views is described below:


### Files

This view displays the list of files that were changed in the current commit:

![](img/Source_Code_403.png)

Each file in the list is displayed with its name, the file-size, who made changes to the file, what action was performed on the file (added, deleted, replaced, updated, etc.) and the most recent commit that exists for that file. Clicking on the filename will take you to the appropriate [file details page](../Source-Code#source-code-file-details), and clicking on the commit hyperlink will take you the appropriate commit.


### Associations

This view displays a list of the SpiraPlan artifacts in the current product that are associated with the current commit. This allows you to see which requirements, incidents or tasks were affected by this specific change to the source code:

![](img/Source_Code_404.png)

Clicking on the hyperlink for the artifact will take you to the appropriate artifact page inside the product (assuming your user has permissions to access that information).

In addition to the associations that are created from within the source code management system, you can add associations between source code commits and SpiraPlan artifacts from within SpiraPlan interface itself. To do this, you simply need to click on the '***Add Association***' button:

![](img/Source_Code_405.png)

To add the association, you just need to select the type of artifact being associated (requirement, test case, incident, etc.) and the numeric ID of the artifact and then click the "***Add Association***" button.

For example to add an association to Requirement RQ00005 you would choose Artifact Type = Requirement and Artifact ID = 5.


## Commit File Details