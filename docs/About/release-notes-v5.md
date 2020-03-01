# Release Notes for Spira v5

## Version 5.4.0.4 (June 2018)

!!! info "Summary"
    - **Security and Performance improvements**: enforced password expiration and restrictions, requirements management module now 400% faster
    - **New artifact icons**: more contemporary, visually striking, with a modular consistent design

??? success "New Features and Fixes"

    - Exploratory testing: associated incidents are not shown during test execution- [IN:4461]
    - Exploratory test containing a link to another test case: upon saving, the link is removed.- [IN:4466]
    - Saving Automation info with error gives concurrency error.- [IN:4563]
    - Sorting of test run sections in reports incorrect- [IN:4638]
    - Edit button appears on some association tabs where it should not.- [IN:4640]
    - Allow Source Code Sidebar to be Expandable- [IN:4649]
    - Parameters Pop-up Window Can;t be Dragged & Dropped- [IN:4650]
    - Test execution page jitters and shakes at specific screen and page height combinations- [IN:4651]
    - Ability to require users to change password at certain intervals [RQ:35]
    - Improvements to TaraVault [RQ:2170]

## Version 5.4 (February 2018)

!!! info "Summary"
    **TaraVault unlimited for all SpiraTeam and SpiraPlan cloud users**: To celebrate the start of a new decade, our cloud source code management solution, TaraVault, is now included at no extra charge, for all the users and repositories and branches you want.
    
    **Improvements to filters**: Update your filters and shared filters easily. Create filters that also include information about which columns you have visible, their sort, order, and width. This is a great way for saving specific “views” you and your teams need.
    
    **Improved navigation between folders and hierarchies**: Each folder now has its own unique url, so you can share links to specific folders with your team. For requirements, releases, and all artifacts with folders new clickable breadcrumbs making it easy to go straight to an artifact’s parent.

??? success "New features"

    - Document Management
        - Remove document popup- [RQ:1867]
        - live reloading: document details page- [RQ:2099]
    
    - Program Management
        - Add a project-group level incident list page for programs- [RQ:1896]
        - Program-view of Planning > Releases- [RQ:2165]
    
    - Project Management
        - Add incident-only planning board- [RQ:1911]
        - Add Task-only planning board- [RQ:1913]
        - Ability to Split a User Story (requirement)- [RQ:2160]
        - Live reloading on the release > build page- [RQ:2161]
        - Implement Bulk Edit permission- [RQ:2169]
    
    - Reporting
        - Custom SQL widget for graphs- [RQ:2173]
        - Add graphs to list pages and changing release list- [RQ:2175]

??? bug "Bug fixes and enhancements"

    - Need to prevent a test being executed if it has test cases in an invalid status for execution- [IN:4387]
    - Duplicate Source Code Revision Session IDs in v5.3.04+- [IN:4458]
    - Preview tab on Document Details breaks for XML documents!- [IN:4182]
    - Instant Messenger Post as Comments function doesn't work- [IN:4288]
    - Test set total estimated duration does not refresh if individual test case est dur is changed- [IN:4316]
    - Extend the length of data sync password column in DB. It gets truncated too easily- [IN:4331]
    - Foreign Key Exception error when cloning a test step from the test step details screen- [IN:4335]
    - Error displayed when you try and import test steps from root folder- [IN:4343]
    - Release execution status not updated when test runs are deleted or edited.- [IN:4349]
    - Document detail page: with Modify Owned permission, save button is never enabled- [IN:4351]
    - Exploratory Test Execution throws fault exception error in SpiraTest / team if user does not have view access to tasks- [IN:4356]
    - Test Set Status Widget includes deleted Test Sets- [IN:4363]
    - Exception removing a parameter from a test case if it is used in any test configuration- [IN:4384]
    - Moving iteration should update test coverage but it does not.- [IN:4463]
    - Rich text fields created using API can contain script tags which are not filtered out on fields without CKEditor- [IN:4468]
    - No cross-association displayed in TESTCASE dedicated sub-tab- [IN:4475]
    - On first load of attachments tab, the wrong documents are loaded briefly- [IN:4478]
    - Exploratory testing: When run from "My Assigned Test Cases" test case doesn't go into exploratory mode- [IN:4506]
    - Split requirement dialog has a place to specify owner but it does not get used- [IN:4510]
    - Subscribe to a Document- [IN:2488]
    - Change Test case copy to place copy below, rather than above, the copied test case- [IN:2570]
    - Excel 2003 reports show blank effort as zeros and incorrectly show effort as percentages- [IN:2797]
    - Version Control - Date sorting appears to put dates "in the future" at the bottom of the list (when sorting descending)- [IN:3003]
    - Source Code Revisions page: problems with filtering and sorting- [IN:3194]
    - Check to see if Attachment Description still has XSS vulnerability in Spira 5.0- [IN:3357]
    - Error appears on release details page and the list of builds is not shown, under certain circumstances.- [IN:3692]
    - Project Group Planning Board: should omit requirements from inactive projects- [IN:3798]
    - Planning board issues (intermittent; related to changing display options)- [IN:3869]
    - Planning Board filtering by deleted release breaks page- [IN:4032]
    - Planning Board: "By Person" views have some issues with the effort numbers- [IN:4061]
    - With Modify Owned permission for incidents, remove attachment is disabled.- [IN:4080]
    - Document detail page: followers list is missing- [IN:4272]
    - With incident modify owned, user can add attachment to incident they don't own- [IN:4297]
    - Test execution, table view: New incident pop-up needs styling update- [IN:4306]
    - Do not prefix the name with "Copy of" when copy/paste to a different folder- [IN:4309]
    - When running test set, test case/run actual duration is incorrect under certain circumstances- [IN:4327]
    - Project Home dashboard: two widgets don't refresh when change from a specific release to all releases- [IN:4333]
    - Project Group planning board: new option has appeared but does not work- [IN:4455]
    - Email notifications do not use a set reply-to address- [IN:4459]
    - Exploratory testing: add ability to paste test step actual result and description into task description - [IN:4465]
    - Exploratory testing, creating tasks: task description not always saved- [IN:4490]
    - For default developer role, Testing -> Configurations menu item leads to error- [IN:4495]
    - Right after saving a new incident, remove attachment doesn't work.- [IN:4098]
    - Test Run Details - test step Full Screen - add scroll bars- [IN:4319]
    - Disable all status result buttons (pass, fail) once clicked, until success is returned- [IN:4454]
