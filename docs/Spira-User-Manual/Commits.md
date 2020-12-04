# Commits


## Commit List

If you click on the "***View Revision Log***" button on the main Source Code page, it will take you to the Revision List page that displays all the revisions made to the product in a sortable, filterable list:

![](img/Source_Code_401.png)

Each revision in the list is displayed with its name, a description of what changed in the revision, the name of the person who committed the revision, and whether the revision was a change of the actual content, or just a change of the properties of the content. Clicking on the hyperlink for the revision name will take you to the [Revision Details page](#source-code-revision-details)  for that revision.

Above the main right-hand pane, there is the **branch selector**. This lets you choose which branch in the source code repository is being viewed.


## Commit Details

When you click on a revision hyperlink in either the product revision log or the file revisions tab described above, you are taken to the revision details page illustrated below:

![](img/Source_Code_402.png)

This page is made up of three areas; the left pane is for navigation, the upper part of the main pane contains the details of the revision, and the bottom part of the right pane contains the list of files that were changed in this revision and the list of artifacts that the revision is associated with.

The navigation pane consists of a link that will take you back to the source code revision list, as well as a list of other revisions associated with the current file. This latter list is useful as a navigation shortcut; you can quickly view the detailed information of all the peer revisions by clicking on the navigation links without having to first return to the main revision list page.

The top part of the main pane allows you to view the details of this revision in the version control system, including the description of what was changed, the date that the change was made, and the name of the person who made the change.

The lower part of the main pane can be switched between two different views by clicking the appropriate tab. Initially the pane will be in "Files" mode, but it can be switched to "Associations" as well. The functionality in each of these two views is described below:


### Files

This view displays the list of files that were changed in the current revision:

![](img/Source_Code_403.png)

Each file in the list is displayed with its name, the file-size, who made changes to the file, what action was performed on the file (added, deleted, replaced, updated, etc.) and the most recent revision that exists for that file. Clicking on the filename will take you to the appropriate [file details page](#source-code-file-details), and clicking on the revision hyperlink will take you the appropriate revision.


### Associations

This view displays a list of the SpiraPlan artifacts in the current product that are associated with the current revision. This allows you to see which requirements, incidents or tasks were affected by this specific change to the source code:

![](img/Source_Code_404.png)

Clicking on the hyperlink for the artifact will take you to the appropriate artifact page inside the product (assuming your user has permissions to access that information).

In addition to the associations that are created from within the source code management system, you can add associations between source code revisions and SpiraPlan artifacts from within SpiraPlan interface itself. To do this, you simply need to click on the '***Add Association***' button:

![](img/Source_Code_405.png)

To add the association, you just need to select the type of artifact being associated (requirement, test case, incident, etc.) and the numeric ID of the artifact and then click the "***Add Association***" button.

For example to add an association to Requirement RQ00005 you would choose Artifact Type = Requirement and Artifact ID = 5.


## Commit File Details