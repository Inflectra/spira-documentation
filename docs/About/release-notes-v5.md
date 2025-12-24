# Release Notes for Spira v5

## Version 5.4.0.4 (June 2018)

!!! info "Summary"
    **[Security and Performance improvements](https://www.inflectra.com/Ideas/Entry/spotlight-on-spirateam-v5404-security-performance-639.aspx)**: enforced password expiration and restrictions, requirements management module now 400% faster
    
    **New artifact icons**: more contemporary, visually striking, with a modular consistent design

??? success "New Features and Fixes"

    - Exploratory testing: associated incidents are not shown during test execution [IN:4461]
    - Exploratory test containing a link to another test case: upon saving, the link is removed. [IN:4466]
    - Saving Automation info with error gives concurrency error. [IN:4563]
    - Sorting of test run sections in reports incorrect [IN:4638]
    - Edit button appears on some association tabs where it should not. [IN:4640]
    - Allow Source Code Sidebar to be Expandable [IN:4649]
    - Parameters Pop-up Window Can't be Dragged and Dropped [IN:4650]
    - Test execution page jitters and shakes at specific screen and page height combinations [IN:4651]
    - Ability to require users to change password at certain intervals [RQ:35]
    - Improvements to TaraVault [RQ:2170]

## Version 5.4 (February 2018)

!!! info "Summary"
    [New Agile Task and Incident Boards](https://www.inflectra.com/Ideas/Entry/spotlight-on-spirateam-54--new-agile-task-and-inci-569.aspx)

    [Program View of Releases and Incidents (SpiraPlan)](https://www.inflectra.com/Ideas/Entry/spotlight-on-spiraplan-54--program-view-of-release-571.aspx)

    [Graphing Enhancements and Custom Graphs](https://www.inflectra.com/Ideas/Entry/spotlight-on-spirateam-54--graphing-enhancements-a-568.aspx) 

??? success "New features"

    - Document Management
        - Remove document popup [RQ:1867]
        - live reloading: document details page [RQ:2099]
    
    - Program Management
        - Add a project-group level incident list page for programs [RQ:1896]
        - Program-view of Planning > Releases [RQ:2165]
    
    - Project Management
        - Add incident-only planning board [RQ:1911]
        - Add Task-only planning board [RQ:1913]
        - Ability to Split a User Story (requirement) [RQ:2160]
        - Live reloading on the release > build page [RQ:2161]
        - Implement Bulk Edit permission [RQ:2169]
    
    - Reporting
        - Custom SQL widget for graphs [RQ:2173]
        - Add graphs to list pages and changing release list [RQ:2175]

??? bug "Bug fixes and enhancements"

    - Need to prevent a test being executed if it has test cases in an invalid status for execution [IN:4387]
    - Duplicate Source Code Revision Session IDs in v5.3.04+ [IN:4458]
    - Preview tab on Document Details breaks for XML documents! [IN:4182]
    - Instant Messenger Post as Comments function doesn't work [IN:4288]
    - Test set total estimated duration does not refresh if individual test case est dur is changed [IN:4316]
    - Extend the length of data sync password column in DB. It gets truncated too easily [IN:4331]
    - Foreign Key Exception error when cloning a test step from the test step details screen [IN:4335]
    - Error displayed when you try and import test steps from root folder [IN:4343]
    - Release execution status not updated when test runs are deleted or edited. [IN:4349]
    - Document detail page: with Modify Owned permission, save button is never enabled [IN:4351]
    - Exploratory Test Execution throws fault exception error in SpiraTest / team if user does not have view access to tasks [IN:4356]
    - Test Set Status Widget includes deleted Test Sets [IN:4363]
    - Exception removing a parameter from a test case if it is used in any test configuration [IN:4384]
    - Moving iteration should update test coverage but it does not. [IN:4463]
    - Rich text fields created using API can contain script tags which are not filtered out on fields without CKEditor [IN:4468]
    - No cross-association displayed in TESTCASE dedicated sub-tab [IN:4475]
    - On first load of attachments tab, the wrong documents are loaded briefly [IN:4478]
    - Exploratory testing: When run from "My Assigned Test Cases" test case doesn't go into exploratory mode [IN:4506]
    - Split requirement dialog has a place to specify owner but it does not get used [IN:4510]
    - Subscribe to a Document [IN:2488]
    - Change Test case copy to place copy below, rather than above, the copied test case [IN:2570]
    - Excel 2003 reports show blank effort as zeros and incorrectly show effort as percentages [IN:2797]
    - Version Control - Date sorting appears to put dates "in the future" at the bottom of the list (when sorting descending) [IN:3003]
    - Source Code Revisions page: problems with filtering and sorting [IN:3194]
    - Check to see if Attachment Description still has XSS vulnerability in Spira 5.0 [IN:3357]
    - Error appears on release details page and the list of builds is not shown, under certain circumstances. [IN:3692]
    - Project Group Planning Board: should omit requirements from inactive projects [IN:3798]
    - Planning board issues (intermittent; related to changing display options) [IN:3869]
    - Planning Board filtering by deleted release breaks page [IN:4032]
    - Planning Board: "By Person" views have some issues with the effort numbers [IN:4061]
    - With Modify Owned permission for incidents, remove attachment is disabled. [IN:4080]
    - Document detail page: followers list is missing [IN:4272]
    - With incident modify owned, user can add attachment to incident they don't own [IN:4297]
    - Test execution, table view: New incident pop-up needs styling update [IN:4306]
    - Do not prefix the name with "Copy of" when copy/paste to a different folder [IN:4309]
    - When running test set, test case/run actual duration is incorrect under certain circumstances [IN:4327]
    - Project Home dashboard: two widgets don't refresh when change from a specific release to all releases [IN:4333]
    - Project Group planning board: new option has appeared but does not work [IN:4455]
    - Email notifications do not use a set reply-to address [IN:4459]
    - Exploratory testing: add ability to paste test step actual result and description into task description  [IN:4465]
    - Exploratory testing, creating tasks: task description not always saved [IN:4490]
    - For default developer role, Testing -> Configurations menu item leads to error [IN:4495]
    - Right after saving a new incident, remove attachment doesn't work. [IN:4098]
    - Test Run Details - test step Full Screen - add scroll bars [IN:4319]
    - Disable all status result buttons (pass, fail) once clicked, until success is returned [IN:4454]


## Version 5.3 (October 2017)

!!! info "Summary"
    **[Data-driven testing with test configurations](https://www.inflectra.com/Ideas/Entry/spotlight-on-spiratest-53--data-driven-testing-wit-495.aspx)**

    **Exploratory testing**: new testing mode to edit, move, and create test steps during exploratory testing sessions

    **Improved artifact details page**: new designs, improved information flow, faster performance 

??? success "New features"

    - Session Management
        - Database-backed session management [RQ:1791]
    - Reporting
        - Incident Cumulative Count by Status [RQ:2143]
        - Charts using jqplot are improved by replacing them with c3/d3 [RQ:2100]
        - Reporting page charts have popovers in place to give quick help information [RQ:2158]
        - Project/Program home page charts have popovers in place to give quick help information [RQ:2157]
    - UI Updates
        - All details pages have unified top title area, including workflow operations [RQ:2091]
        - live reloading: task details page [RQ:2096]
        - live reloading: requirement details page [RQ:2097]
        - live reloading: release details page [RQ:2098]
        - All details pages restyled with new "unity" design [RQ:2106]
    - Enhanced Support for FDA Processes [RQ:2149]



??? bug "Bug fixes and enhancements"

    - Have insert test step link dialog remember last test case [IN:1451]
    - Ability to sort reports by custom properties [IN:1624]
    - Documentation: for incident date range graphs, explain that they rely on the "closed on date" not the status [IN:2755]
    - Update the documentation: for test set list, explain the "Display data for" dropdown [IN:2933]
    - Embedded images not appearing in Word 2003 format reports [IN:3325]
    - Project Home Test Set Status widget: overdue test sets should consider status [IN:3379]
    - Documentation: 2 places give incorrect information about what happens when you click View Details [IN:3396]
    - Misleading Error Message when trying to execute a Test Case without step [IN:3612]
    - Documentation: Add a description of the bracketed numbers at the top of the test execution page [IN:3622]
    - Test execution: certain sequences of actions related to actual result and "pass all" result in actual results being lost [IN:3627]
    - Change event not fired if click only one checkbox on a form manager dropdown [IN:3630]
    - Release Detailed report: take out "Active" and add "Status" and "Type" fields, plus a few other minor issues [IN:3645]
    - Update documentation to explain the new "Refresh the Database Indexes" button. [IN:3654]
    - Documentation: explain new Release Types and statuses [IN:3676]
    - Rich text custom fields shown on list pages are not shown formatted, but as HTML [IN:3679]
    - Add New Document popup does not hide fields correctly, forcing scrolling [IN:3689]
    - Automatically set artifact type on the association panel if a shared project only shares one artifact with current project [IN:3765]
    - Allow sorting by custom properties in all reports [IN:3776]
    - Test execution attachment panel should clear the grid on changing test case immediately [IN:3780]
    - Test Case list page produces error when filtering by test steps and adding new test case [IN:3783]
    - Tooltips not working for releases in the Quick Filter panel [IN:3788]
    - Column resizing causes big problems on mobile devices, probably needs to be disabled. [IN:3794]
    - With Limited View, problems displaying test set detail page (and also test case detail page) [IN:3796]
    - Scrollbar in IE covers rightmost content of page [IN:3806]
    - Notification Events page does not go to incident workflow [IN:3817]
    - In test execution screen, disable incident creation if no releases exist [IN:3818]
    - Double-Click for Quick-Edit on list pages does not work in Chrome [IN:3822]
    - Cannot move items to the Root folder on Task List [IN:3830]
    - Deleting associations button should be labeled "remove" not "delete" to avoid confusion [IN:3835]
    - Viewing History Details of Purged item causes error to be logged. [IN:3899]
    - German umlauts not showing correctly in Word 2003 reports [IN:3915]
    - Planning board usability - dragging may move previously selected items [IN:3918]
    - REST API: get/post Test Set Folder Test Sets search does not filter properly by test set folder id [IN:3984]
    - Can expand and collapse hierarchical lists in the newly redesigned association panel [IN:3986]
    - Show tooltips in search results on the new associations panel [IN:4004]
    - In Administration, the "rows per page" setting is not saved - keeps reverting back to 15 [IN:4011]
    - Separate out the release filters in the test set report (display data for vs. column filter) [IN:4029]
    - Multi-select lists: dropdown closes when click checkbox, and change event is not triggered [IN:4034]
    - Test execution with single step test case does not refresh incident tab after passing/failing [IN:4042]
    - Labels inside forms were not correctly showing as disabled when they are disabled [IN:4043]
    - Make screenshots have more unique filenames and be stored in separate folder [IN:4048]
    - Cutting and pasting test cases can remove them from the ui by adding them to folders in other projects [IN:4051]
    - Copying folder into subfolder creates semi-infinite loop. [IN:4052]
    - Custom Properties not displaying in PDF format reports (other formats OK) [IN:4053]
    - Searching by ID on associations tab of incident details page can cause errors [IN:4062]
    - SpiraTest: followers are not displayed on incident detail page [IN:4069]


## Version 5.2 (April 2017)

!!! info "Summary"
    **Improved reporting**: additional graphs and more dashboard layout choices

    **Planning board improvements** 

    **[Testing improvements](https://www.inflectra.com/Ideas/Entry/preview-of-spiratest-v52--testing-enhancements-458.aspx)**


??? success "New features"

    - Users section on various artifact detail pages (author, owner, subscribees) [RQ:1551]
    - Redesign of Incident Details Page [RQ:1869]
    - Adding new/replacement graphs based D3/C3 [RQ:1887]
    - Planning board enhancements [RQ:1908]
    - Cross-project associations on incident details page [RQ:1910]
    - Enhanced functionality for subscribing to / following artifacts [RQ:1961]
    - Additional graphs for Reports/Project Home [RQ:2075]
    - Different Project Home pages for different roles [RQ:2078]



??? bug "Bug fixes and enhancements"

    - Have insert test step link dialog remember last test case [IN:1451]
    - Ability to sort reports by custom properties [IN:1624]
    - Documentation: for incident date range graphs, explain that they rely on the "closed on date" not the status [IN:2755]
    - Update the documentation: for test set list, explain the "Display data for" dropdown [IN:2933]
    - Embedded images not appearing in Word 2003 format reports [IN:3325]
    - Project Home Test Set Status widget: overdue test sets should consider status [IN:3379]
    - Documentation: 2 places give incorrect information about what happens when you click View Details [IN:3396]
    - Misleading Error Message when trying to execute a Test Case without step [IN:3612]
    - Documentation: Add a description of the bracketed numbers at the top of the test execution page [IN:3622]
    - Test execution: certain sequences of actions related to actual result and "pass all" result in actual results being lost [IN:3627]
    - Change event not fired if click only one checkbox on a form manager dropdown [IN:3630]
    - Release Detailed report: take out "Active" and add "Status" and "Type" fields, plus a few other minor issues [IN:3645]
    - Update documentation to explain the new "Refresh the Database Indexes" button. [IN:3654]
    - Documentation: explain new Release Types and statuses [IN:3676]
    - Rich text custom fields shown on list pages are not shown formatted, but as HTML [IN:3679]
    - Add New Document popup does not hide fields correctly, forcing scrolling [IN:3689]
    - Automatically set artifact type on the association panel if a shared project only shares one artifact with current project [IN:3765]
    - Allow sorting by custom properties in all reports [IN:3776]
    - Test execution attachment panel should clear the grid on changing test case immediately [IN:3780]
    - Test Case list page produces error when filtering by test steps and adding new test case [IN:3783]
    - Tooltips not working for releases in the Quick Filter panel [IN:3788]
    - Column resizing causes big problems on mobile devices, probably needs to be disabled. [IN:3794]
    - With Limited View, problems displaying test set detail page (and also test case detail page) [IN:3796]
    - Scrollbar in IE covers rightmost content of page [IN:3806]
    - Notification Events page does not go to incident workflow [IN:3817]
    - In test execution screen, disable incident creation if no releases exist [IN:3818]
    - Double-Click for Quick-Edit on list pages does not work in Chrome [IN:3822]
    - Cannot move items to the Root folder on Task List [IN:3830]
    - Deleting associations button should be labeled "remove" not "delete" to avoid confusion [IN:3835]
    - Viewing History Details of Purged item causes error to be logged. [IN:3899]
    - German umlauts not showing correctly in Word 2003 reports [IN:3915]
    - Planning board usability - dragging may move previously selected items [IN:3918]
    - REST API: get/post Test Set Folder Test Sets search does not filter properly by test set folder id [IN:3984]
    - Can expand and collapse hierarchical lists in the newly redesigned association panel [IN:3986]
    - Show tooltips in search results on the new associations panel [IN:4004]
    - In Administration, the "rows per page" setting is not saved - keeps reverting back to 15 [IN:4011]
    - Separate out the release filters in the test set report (display data for vs. column filter) [IN:4029]
    - Multi-select lists: dropdown closes when click checkbox, and change event is not triggered [IN:4034]
    - Test execution with single step test case does not refresh incident tab after passing/failing [IN:4042]
    - Labels inside forms were not correctly showing as disabled when they are disabled [IN:4043]
    - Make screenshots have more unique filenames and be stored in separate folder [IN:4048]
    - Cutting and pasting test cases can remove them from the ui by adding them to folders in other projects [IN:4051]
    - Copying folder into subfolder creates semi-infinite loop. [IN:4052]
    - Custom Properties not displaying in PDF format reports (other formats OK) [IN:4053]
    - Searching by ID on associations tab of incident details page can cause errors [IN:4062]
    - SpiraTest: followers are not displayed on incident detail page [IN:4069]


## Version 5.1 (December 2016)

!!! info "Summary"
    Powerful new search

    Improved program management tools

    Seamless cross-product associations


??? success "New features"

    - Enhanced project group dashboards and reporting [RQ:1700]
    - Ability to configure which cross-project associations are allowed [RQ:1702]
    - Ability to included shared projects' requirements on requirements list page [RQ:1704]
    - Hosted data integration hub for cloud customers [RQ:1870]
    - Data mapping to allow easier use of multiple instances of the same system [RQ:1888]
    - Enhanced global search that uses SQL free text indexing [RQ:1886]
    - Streamline navbar for project groups and projects [RQ:1889]
    - Ability to resize column widths on list pages [RQ:1893]
    - Project Group Planning Board [RQ:1894]
    - Add cross-project associations capability to requirement details page [RQ:1895]
    - Brand new users get helpful in-app onboarding / orientation [RQ:1901]



??? bug "Bug fixes and enhancements"

    - Yes/No Slider Checkboxes have bad performance when you have lots of them on a page [IN:3723]
    - Exclude packages from requirements burndown/up/velocity graphs [IN:3724]
    - Change Incident fields in My Page Widgets [IN:1388]
    - Requirements are inserted with an deleted parent [IN:2780]
    - Associations: at top of "Add New Association" dialog, hide or disable artifacts that the user does not have permission to view. [IN:2859]
    - Reports: some czech characters are wrong in PDF format [IN:3063]
    - Filtering by text that contains Czech characters does not work [IN:3311]
    - Correcting indents in Data Tools for requirements turns reqs into packages even when they have no children [IN:3461]
    - Requirement gets stuck as a "package" when you copy a package and then delete all the children under the copy [IN:3479]
    - Dragging a parent requirement under itself causes weird hierarchy issues [IN:3495]
    - Need to enforce read-only workflow fields on server-side [IN:3635]
    - Release fields appear blank on some detail pages if the release is in "closed" status  [IN:3694]
    - SpiraTest 5.0 : Reports not return requirements in "Sub-release" [IN:3704]
    - Rich Text Properties Don't Display Correctly in Some Reports [IN:3705]
    - SQL Command Timeouts for Custom Query reports [IN:3728]
    - Resource list page: effort is wrong sometimes due to SQL removing duplicates [IN:3740]
    - Resource details page: the release dropdown does not work [IN:3742]
    - Rich text fields are not always hidden when specified in workflow [IN:3747]
    - Add current folder to parent for 'add folder' dialog [IN:3757]
    - IE11: On requirement detail page, the newly-redesigned Add Associations dialog does not display at all. [IN:3760]
    - Requirement list: select all selects requirements from another project [IN:3762]
    - In new Add Associations dialog, searching doesn't work as expected if user doesn't select an artifact. [IN:3763]
    - Ability to resize columns [IN:447]
    - Ability to resize table columns in list screens [IN:539]
    - Separate the Requirements > Tasks and main Tasks filters [IN:1442]
    - Make text truncation on list screens configurable [IN:1492]
    - Show artifact ID when in edit mode on list pages [IN:2326]
    - Date-Range Graphs a day out for PCs set to timezones west of server time. [IN:2365]
    - Name heading on detail pages omits <> less than/greater than pairs, and anything between them [IN:2392]
    - Editing in SpiraTeam: sometimes it is not possible to select text [IN:2395]
    - With large number of projects, scrollbar appearing in middle of Reporting Screen [IN:2639]
    - User dropdowns display quotes with a forward slash in dropdown list [IN:2886]
    - Simply clicking on Add Comment button causes item to be considered modified [IN:2982]
    - Planning Board: the New Requirement dialog does not display the default estimate [IN:3196]
    - Incident Summary Graph: get error if select Component for x-axis [IN:3304]
    - Edge only: pasting a screenshot into a rich text field does not work [IN:3646]
    - UI: Most number fields need to be widened to show more digits, especially for Edge and Chrome [IN:3666]
    - Incident detail page, schedule section: clock icon is partially covering the time for "Closed On" date. [IN:3667]
    - SpiraTeam Users [IN:3690]
    - The ckeditor native browser spell checker is disabled for test step editing [IN:3695]
    - Keep titles in sidebar panel heading when minimized [IN:3714]
    - The Order of Reports Displayed on Menu [IN:3736]
    - On requirement detail page, association tab: some incident associations give an error when attempting to edit them [IN:3769]
    - Tooltips not appearing for Activity Stream on Project Home [IN:3770]
    - Requirement details, associations tab: filtering by comment fails with an error if any comment is blank [IN:3772]
    - Add variable rows and sorting to some of the admin screens [IN:1419]
    - Calendar controls / drop down lists getting cutoff [IN:2452]
    - Large images pasted into comments makes the page width wider than the browser window [IN:3732]


## Version 5.0 (July 2016)

!!! info "Summary"
    **Testing improvements**: test case folders and test set folders 

    **Electronic signature support**

    **Workflows for releases**

    **The app is 100% response across all sizes of device**


??? success "New features"

    - Manipulate Components through the API [RQ:1855]
    - Support for electronic signatures on specific workflow transitions [RQ:1792]
    - Workflow for releases [RQ:1794]
    - Ability to have Document custom properties [RQ:1798]
    - Ability to track Documents history [RQ:1807]
    - Add CORS support to the REST API [RQ:1821]
    - Releases can be categorized into different types [RQ:1824]
    - Releases can have different statuses [RQ:1825]
    - Screenshot annotation capture tools [RQ:1830]
    - All pages are fully responsive to different devices (desktop, mobile, etc.)  [RQ:1832]
    - Releases can have task progress roll-up multiple levels [RQ:1839]
    - Encrypt password and other secure global settings [RQ:1851]

??? bug "Bug fixes and enhancements"

    - Newly added items appear in 'closed' folders. [IN:768]
    - Allow certain releases to flow-up status like iterations [IN:874]
    - Ability to filter tasks by requirement in task list [IN:929]
    - Add company and department to user profile [IN:1044]
    - Allow dragging of Entire Release name. [IN:1121]
    - Add last login date/time to Active Sessions screen [IN:1358]
    - Administrator controlled logon/user broadcast messaging service [IN:1546]
    - As part of workflow update allow password-based confirmations as optional feature [IN:1670]
    - Expanding requirement that has multiple levels of children causing items to not appear when filter is set [IN:1707]
    - Add history items to SOAP API [IN:1770]
    - Ability to add existing document to artifact through API [IN:1952]
    - View permissions asks user if they want to save changes. [IN:2106]
    - When prompting a user that they must enter a comment, highlight the comment box in some way [IN:2146]
    - Editing in lists: cancel button doesn't work if you used the context menu to go into edit mode [IN:2186]
    - For user with "limited view", hide the main menu options that they can't use. [IN:2203]
    - If we don't fix IN2203 for version 4.0, then I suggest that we make the menu item go to My Page instead of Project Home page [IN:2204]
    - Whole planning menu disappears if requirement view is unchecked for role [IN:2214]
    - Editing on list page: update and cancel buttons disappear when you put the same row into edit mode a second time [IN:2242]
    - Incident detail page: "hours" label still present when effort field is hidden [IN:2254]
    - Include clickable list of tokens on the Notification Event Details page [IN:2275]
    - Add RemoteHistory object to API and allow artifact history retrieval [IN:2297]
    - Required fields a pain in requiring new comment when amending data in a status [IN:2304]
    - Spira API - Connection closed error [IN:2414]
    - Add API method for checking health of installation [IN:2438]
    - Error at changing incident state via eclipse plugin [IN:2490]
    - LDAP bind password stored in database in clear text [IN:2512]
    - Requirements detail page navigation panel: filter by Assigned uses priority sort. Confusing. tree order would be better [IN:2533]
    - Add existing attachments dialog should show all documents, not be limited to the "rows per page" setting in document list [IN:2550]
    - Allow Show/Hide Columns in Attachment Area like in other lists [IN:2568]
    - Add Active API user count to API functions [IN:2590]
    - Quick filter panel release list is using rows per page setting from main release list; needs to always show all releases [IN:2610]
    - User with create permission, but not modify permission, for incidents gets an error when attempting to save a new incident [IN:2637]
    - Rich text custom field: can't effectively make it required. Need to ignore tags such as <br> that aren't real data. [IN:2674]
    - Planning board: item appears to be duplicated after dragging into a closed column and then opening the column [IN:2961]
    - Filtering the document list: a few minor problems [IN:3013]
    - For custom fields, need to specify formats for date and number fields in Excel reports [IN:3033]
    - Documentation: in the integration guide, note which fields are used for exporting ONLY [IN:3165]
    - Updating requirement effort does not trigger a recalculation of the total effort for the release [IN:3173]
    - Omit inactive releases from quick filter [IN:3188]
    - "Allow Empty" custom properties option - allow user to specify whether or not it applies to folders [IN:3192]
    - Filtering incident reports by component does not work (all incidents are included) [IN:3199]
    - Cross-site scripting problem: creating an incident through the API, for example via KronoDesk, fails to strip out potentially dangerous HTML [IN:3204]
    - Release Backlog expansion/contraction status in Planning Board not saved across refreshes [IN:3218]
    - Admin -> Edit File Icons not refreshing from DB [IN:3220]
    - Project Managers need to be able to create folders in their projects [IN:3300]
    - Split task functionality has problem with permissions [IN:3322]
    - If page gets reloaded due to the Find button, all of the custom fields are omitted [IN:3338]
    - Rename 'Copy' to Duplicate on Incidents List Page. [IN:3340]
    - Display last successful/failed login on user's admin profile [IN:3342]
    - Accented characters cause issues with file upload/download [IN:3343]
    - Plugin Delete button active even when grayed out [IN:3350]
    - Add image preview to the 'Preview' tab in Documents. [IN:3352]
    - German umlauts in TXT attachment to Incident not displayed correctly [IN:3369]
    - Notifications: 2 different actions are giving system errors. [IN:3375]
    - Add 'Design Element' as new requirement type [IN:3376]
    - Error when attempting to edit incident associations [IN:3395]
    - unassigned items' section of the planning board should stay expanded after adding new requirements  [IN:3410]
    - In reports, in change history, custom list IDs are shown rather than the actual list values. [IN:3413]
    - Build Pagination Options not populated on Release Details Page [IN:3425]
    - Display problem when browser window is narrow enough so that the main menu drops down on the left side [IN:3462]
    - On Edit User page, if you change a role in the "Membership and Mapping" section, then click on the main "Save" button, the change does not get saved. [IN:3474]
    - REST API should return 404 in cases where artifacts not found (vs. 200) [IN:3477]
    - Document list: filtering and/or sorting does not work on some fields [IN:3485]
    - Incident Detail Progress not updating properly on save [IN:3488]
    - Global Search shows no indication of in-progress searching.. [IN:3505]