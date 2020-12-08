# Common Elements Across the Application

There are lots of different artifacts in the application (described [here](Functionality-Overview.md)). This means each artifact has its own settings, uses, and logical links to other artifacts, and reporting. Each artifact is different but they also share many similarities. These are explained below. 

## Artifact List Pages

When you first visit an artifact section in the app (by clicking on the relevant link in the global navigation bar), you will be taken to the artifact list page. This may look something like below (this image is of the requirements list page) with a grid of data - each row representing a single artifact, and often a sidebar on the left with charts or links:

![](img/Requirements_Management_83.png)

### Filtering

You can easily filter artifact lists as you can see in the screen-shot below. Here, we are filtering Requirements by the status "Requested":

![](img/Requirements_Management_86.png)

To filter the list:

- make sure the columns you want to filter on are visible (you can hide them later if you want)
- use the dropdowns or free-text search fields immediately beneath the column names
- click the `Filter` icon or press the `ENTER` key to apply the filters

Note that the NAME field is searched using a "like" comparison, so that searching for "database" would match "Database is ready", "There is a database", "The data in the database is correct", and so on. All other freetext fields need to be exact matches (e.g. dates or numbers).

To **clear the current filter** (whether it is saved or not), either click the `Clear Filters` button above the table (as you can see in the screenshot above), or go to `Filter` > `Clear Filter` from the operations toolbar.

#### Managing Filters
You can do a number of things with filters. First let's talk about using the `Filters` button on the operations toolbar (at the top of the page just below the main navigation bar).

To **reuse a filter**, save it by going to `Filter` > `Save Filter` from the operations toolbar. Give your new filter a name and click `Save`.

By default, when you save a filter it will also save your **column selection** information. Uncheck the box next to "Save the column selection with the filter" if you do not want to save this information. 

When you apply a saved filter with column selection information, the system will show the specific columns visible (including their relative ordering and width) to match those in the filter. This means that you can Show/Hide different columns, filter on them, and save the entire combination as a saved view. When you switch between saved views, the system will show/hide and reposition the columns associated with the view automatically.

To **share the filter** with other members of the product, in the Save Filter dialog, check the box next to "Share with other members of the product". 

To **update an existing filter**, go to `Filter` > `Save Filter` and click on `Update Existing`. You will see a dropdown of all your saved filters. Pick one, and then click `Save`. This will update the filter itself, any sort applied, whether it is shared or not, or if it should save the column selection with the filter.

To **see your saved filters** for this artifact, go to `Filter` > `Retrieve Filter`. Apply the filter by selecting it.

![](img/Requirements_Management_87.png)

From your "My Page" you can **see all your save filters** across all artifacts and products. You can also delete any filter from there. This is all through the [My Saved Searches](User-Product-Management.md#my-saved-searches) widget.

#### Quick Filter Side Panel
As a shortcut, the left hand panel on artifact list pages includes a set of **Quick Filters**. Click the name of the filter in this panel to apply it. This panel is NOT visible for list pages that do not have a side panel at all - i.e. Releases, Automation Hosts, Test Configurations, and Resources.

The quick filter panel shows a list of **all saved filters** created by you (with an icon of a person) or shared by others (with an icon of a group of people)  for the current artifact.

For Requirements, Test Cases, Incidents, Risks, and Tasks the quick filter panel also shows a list of **Components** for the current product. Picking a component will filter the list to only show those associated with that component.

For Requirements and Test Runs the quick filter panel additionally shows a dropdown for **Releases**. Picking a release will filter the list to only show items that are set for that particular release.

#### Sorting

Many artifact lists let you sort by a specific column (either ascending or descending). To change the column being sorted, click on the up or down arrow icon next to the title of that column. Click the other icon will reverse the sort order. The currently sorted column is indicated by the darker arrow. When you save a filter it will always save the selected sort.


### Show / Hide Columns

This drop-down list allows you to change the fields that are displayed in the artifact list as columns for the current product. To show a column that is not already displayed, simply select that column from the list of "Show..." column names and to hide an existing column, simply select that column from the list of "Hide..." column names. This is stored on a per-product basis, so you can have different display settings for each product that you are a member of. The fields can be any of the built-in fields or any of the custom properties set up by the product owner.

### Right-Click Context Menu

SpiraPlan® provides a shortcut -- called the *context menu* - for accessing some of the most commonly used functions, so that you don't need to move your mouse up to the toolbar each time. To access the context menu, right-click on any of the rows in the artifacts list and the following menu will be displayed (the one below is specific to requirements - different artifacts have different options in the *context menu*):

![](img/Requirements_Management_90.png)


### Export to Another Product

You can export the following artifacts from the current product to any other product that you have access to:

- incidents
- releases
- requirements
- risks
- tasks
- test cases

The artifacts will be exported from the current product to the destination product. Any file attachments will also be copied to the destination product. If the destination product uses the same product template then standard and custom fields will be copied over in full - but this will not necessarily be possible if the destination product uses a different product (the system will try and match up fields as best it can).

*Note: when exporting a requirement that has children, the requirement itself and all of its children are exported to the destination product.*

To export one or more of a particular artifact:

1. go to the list page for that artifact in the right product. 
2. check the check-boxes of the artifact(s) you want to export
3. click `Tools` > `Export to Product` from the toolbar
4. this will then bring up a list of possible destination products (below is an example for exporting incidents)
5. select the destination product and click `Export`

![](img/Incident_Tracking_241.png)


## Artifact Details Pages

To view details about a specific artifact, you need to go to the artifact's detail page. Clicking on an item on the artifact list page will open the corresponding detail page.

Most of these details pages are made up of *three* areas;

1.  the left pane with artifact list navigation options and information

2.  the right pane's header, which displays: the operations toolbar; the editable name of the selected artifact; and the info bar (with a shaded background), which also contains the workflow status transitions

3.  the right pane's tabbed interface with rich information related to the artifact

Please note that on smaller screen sizes the left navigation pane is not displayed. While the navigation pane has a link to take you back to the artifact list, on mobile devices a 'back' button is shown on the left of the operations toolbar.

The navigation pane can be collapsed by clicking on the "-" button, or expanded by clicking anywhere on the gray title area. On desktops the user can also control the exact width of the navigation pane by dragging and dropping a red handle that appears on hovering at the rightmost edge of the navigation pane.

The navigation pane often shows a list of the peer artifacts to the one selected. This list is useful as a navigation shortcut.

### Breadcrumbs 

For folders and hierarchical / tree view artifacts at the top of the details page right hand side you will see the breadcrumb trail, where relevant. 

If the artifact you are looking at is in a folder, above its name you will see a breadcrumb trail for the full folder path. It will be in the form of `Grandparent Folder / Parent Folder`. You can click on any part of this breadcrumb / path to navigate to that folder. 

Artifacts that have folders are: documents, test cases, test sets, and tasks.

Requirements and releases exist in a hierarchy with other requirements and releases. For these you will also see a breadcrumb, but instead of showing folders it will show the hierarchy to the container requirements or releases. Clicking on the breadcrumb link will take you to the specific requirement or release clicked on.

**Tip**: when navigating to folders (for all artifacts that support them), the URL in your browser's address bar will change. Each folder has a unique, sharable URL that you can give to someone to display the list of artifacts with the appropriate folder selected. You can also open up multiple folders in different browser tabs and easily toggle between them from the same browser.


### Workflows

A number of artifacts can be controlled using workflows (these include requirements, releases, test cases, documents, risks, incidents, and tasks). Depending on the user's role and whether they are listed as the owner or author of the artifact, displayed in the info bar beneath the artifact name is the current workflow status and an `Operations` button. When you click this button you will see a set of allowed workflow operations - called transitions (below we are looking at that for a requirement):

![](img/Requirements_Management_94.png)

These workflow transitions specify, given a starting status, which statuses you can move the artifact to. After changing the status of the artifact by clicking on a transition, the form on the overview tab may change. Different fields may be visible, enabled, or required. 

For example, a requested requirement has its "Release" field hidden, but once the requirement is planned, that release field is visible and required. The types of change allowed and the fields that are enabled/visible/required will depend on how your product administrator has set up the workflow. Administrators should refer to the *Administration Guide* for details on configuring workflows. 

Once you've made the changes to the appropriate artifact fields, you can either click "***Save***", "***Save and Close***", or "***Save and New***" to commit the changes or "***Refresh***" to discard the changes and reload the artifact from the database. In addition you can print the current artifact by clicking "***Print***", which will display a printable version of the page in a separate window.


### Electronic Signatures
Any workflow transition (moving from one status to another) can be set to require an electronic signature. If enabled for a particular workflow operation an electronic signature is required to confirm the status change. Confirmation requires entering the users password, and a message explaining the meaning of this operation.

Workflow operations requiring a digital signature are marked with a padlock icon:

![](img/Requirements_Management_95.png)

On attempting to save changes made after clicking a workflow operation that requires a digital signature you will be presented with a popup like the one below:

![](img/Requirements_Management_96.png)

!!! info  "How to digitally sign if using OAuth"
    If you login to Spira using an OAuth / Single Sign On provider like Google or Okta, instead of entering your password use your RSS Key. This is visible on your [My Profile](../User-Product-Management/#my-profile) page.


### Emailing

Using the "***Email***" button on the toolbar, you can send an email containing details of the artifact to an email address or another user on the system:

![](img/Requirements_Management_97.png)

You can specify the subject line for the email, and either a list of email addresses, separated by semicolons, or an existing product user .The content of the email is specified in the System Administration --
Notification Templates.


The bottom part of the right pane can be switched between six views:
"Overview", "Test Coverage", "Tasks", "Attachments", "History" and "Associations", each of which will be described in more detail below.

### Followers
To be notified of any changes made to the current artifact via email, click the "***Subscribe***" button. If you already subscribed, the button will instead let you "***Unsubscribe***" to stop receiving emails about that particular artifact. Depending on your role, you may also see a dropdown arrow to the right of this button. This will let you subscribe others in the product to this artifact.


![](img/Requirements_Management_99.png)

![](img/Requirements_Management_100.png)

You can also quickly see who is following an artifact under the "People" section in the Overview tab.

![](img/Requirements_Management_101.png)

To view information about the follower, or to unfollow them from the item, hover over their avatar to display a user profile card.

![](img/Requirements_Management_102.png)


### Overview

The Overview tab is divided into a number of different sections. Each of these can be collapsed or expanded by clicking on the title of that section. This tab displays information about all the main fields of the artifact, as well as descriptions, comments, and other information.

Many artifacts have a comments section that allows you to add and view discussions relating to the artifact:

![](img/Requirements_Management_104.png)

Existing comments are displayed in order underneath the textbox in date order (either newest first or oldest first). To add a new comment, enter it into the textbox, and click the "***Add Comment***" button.


### Attachments

The attachment tab displays the list of documents, screenshots or web-links (URLs) that have been "attached" to the artifact. The documents can be in any format, though SpiraPlan® will only display icons for certain known types.

![](img/Requirements_Management_113.png)

The attachment list includes the filename/URL that was originally uploaded together with the file-size (in KB), name of the person who attached it and the date uploaded. In addition, if you position the pointer over the filename and hold it there for a few seconds, a detailed description is displayed as a tooltip.

To actually view the document, click on the filename hyperlink and a new web browser window will open. Depending on the type of file, this window will either display the document / web-page or prompt you for a place to save it on your local computer. To remove an existing attachment from an artifact, click the "***Remove***" button and the attachment will be removed from the list. Using the standard filter/sort options you can also sort and filter the list of attachments to make it more manageable.

If you are using SpiraPlan or SpiraTeam (but not SpiraTest) you can also choose to include file attachments stored in a linked version control system (e.g. Git, Subversion, CVS, Perforce, etc.) by selecting the "Include Source Code Documents" option.

To attach a new document to the artifact, you need to first click the "***Add New***" button to display the new attachment dialog box:

![g4169](img/Requirements_Management_114.png)


There are three different types of item that can be attached to an artifact:

To upload a file, choose "File" as the type and then click the Browse button and select the file from your local computer, optionally enter a detailed description then click the "***Upload***" button. The document will be copied from your computer and attached to the artifact.

To attach a web-link (URL) to the artifact, you need to choose "URL" as the type and then enter the fully qualified URL (e.g.
[http://mywebsite.com?Document=1](http://mywebsite.com/?Document=1)), an optional description and then click the "***Upload***" button to attach the web-link.

To attach a screenshot to the artifact, you need to choose "Screenshot" as the type and then copy the image to your computer's clipboard (e.g. on Windows computers, the PRINT SCREEN button captures the current page and adds to the clipboard). Once the image is in the clipboard, paste it into the editor using CTRL+V (or the equivalent keystroke for your operating system) and the item will appear in the preview window. You can then fill in the other fields and click "***Upload***" to attach the image.

Note: If you are using a non-Windows® computer (e.g. Macintosh®) that doesn't put file extensions on filenames (e.g. .xls for an Excel sheet) automatically, then you will need to manually add the file extension to the filename before uploading if you want it to be displayed with the correct icon in the attachment list.

You can also associate an existing document (that's already stored in SpiraPlan) with the artifact. To do that, click on the "***Add Existing***" button to bring up the add file association dialog box:

![](img/Requirements_Management_115.png)


![](img/Requirements_Management_116.png)

You can then choose to either associate a document stored in the SpiraPlan Documents repository or (in the case of SpiraPlan/SpiraTeam but not SpiraTest) from the linked source code repository. In either case you first select the appropriate folder, and then pick the document(s) from the file list on the right. In the case of a source code file association you can also add a comment.


### History

This tab displays the list of changes that have been performed on the artifact since its creation. An example change history for a requirement is shown below:

![](img/Requirements_Management_117.png)

The change history displays the date that each change was made, together with the fields that were changed, the old and new values and the person
who made the change. This allows a complete audit trail to be maintained of all changes in the system. In addition, if you are logged in as a product administrator you can also click on the "Admin View" hyperlink to revert any unwanted changes.


### Associations

You can associate artifacts to one another. For instance, you can associate (or link) one requirement to another requirement, or a test case to a risk. The following artifacts have association tabs:

- Documents
- Incidents
- Requirements
- Risks
- Source code commits
- Source code files
- Tasks
- Test cases (in SpiraTeam and SpiraPlan only)

From the associations tab you can see and manage the list of artifacts associated with the specific artifact you are looking at. You can even make links between artifacts across different products (if the admin has set this up). The image below shows the association tab for a requirement.

![](img/Requirements_Management_118.png)

The requirements and risks in this list are those a user has decided are relevant to the current artifact. They therefore created a direct link between them.

Each association is displayed with the:

- type of association (related-to, dependency, etc)
- name of the artifact being linked-to
- type of artifact (requirement, incident, etc.)
- name of the person who created the association
- a comment that describes why the association was made. In the case of an indirect association (eg when a link to an incident is added to a requirement during a test run), the comment will contain the name of the specific artifact that created that indirect association.

In addition, when using SpiraPlan or SpiraTeam, the system automatically scans the source code repository for any commits, across all branches, that are linked to this artifact.

You can perform the following actions on the list of associations:

1. **Delete**: removes the selected association to the other artifact. This will only delete the association, not the linked artifact itself. Not all associations can be removed in this way because they are managed by the application (for example, the association between a commit with artifact tokens in it and those artifacts)
2. **Refresh**: updates the list of associations from the server, useful if other people are adding associations to this requirement at the same time.
3. **Filter / Apply Filter**: Applies the entries in the filter boxes to the list of associations
4. **Clear Filters**: Clears the current filter, so that all associations for the current requirement are shown.
5. **Edit**: Clicking the "***Edit***" button to the right of the associations allows you to edit the association type and comment fields inline directly on this screen.

To create a new association, click the "***Add***" button to display the add association panel (below is an example from requirements):

![](img/Requirements_Management_119.png)

If you know the ID of the artifact you want to associate, you can enter its ID prefixed by the appropriate token (eg "RQ" for requirement):

![](img/Requirements_Management_120.png)

Otherwise choose the Artifact Type (and Product if making a cross-product association) from the dropdowns:

![](img/Requirements_Management_121.png)

You can narrow down your search by entering a keyword:

![](img/Requirements_Management_122.png)

Artifacts that have folders let you choose a folder to narrow your search. When attempting to add an association to a requirement, you can choose a package from the list to narrow down the results:

![](img/Requirements_Management_123.png)

Once you have a list of artifacts, select the checkboxes of the items you want to associate with the current artifact and click the 'Save' button.

You can add a comment that explains the rationale for the association and choose the type of association being created:

-   **Related-to:** this is used to specify that the two artifacts are simply related
-   **Depends-on:** this is used to specify that the current artifact has a dependency on the one being linked to.
