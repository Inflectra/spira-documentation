# Release Notes for Spira v6

## Version 6.3.0.1 (February 2020)

!!! bug "Bug fixes and performance improvements"
    - Input boxes in grids should be full when in edit mode on grids with resizable columns [IN:5376]
    - Artifacts with folders can create new items in wrong folder when loading the list page via the url [IN:5388]
    - Planning boards do not always show all items for a parent release when viewing a sprint [IN:5392]
    - Data Sync encryption does not support FIPS mode [IN:5396]

## Version 6.3 (January 2020)

!!! info "Summary"
    **TaraVault unlimited for all SpiraTeam and SpiraPlan cloud users**: To celebrate the start of a new decade, our cloud source code management solution, TaraVault, is now included at no extra charge, for all the users and repositories and branches you want.
    
    **Improvements to filters**: Update your filters and shared filters easily. Create filters that also include information about which columns you have visible, their sort, order, and width. This is a great way for saving specific “views” you and your teams need.
    
    **Improved navigation between folders and hierarchies**: Each folder now has its own unique url, so you can share links to specific folders with your team. For requirements, releases, and all artifacts with folders new clickable breadcrumbs making it easy to go straight to an artifact’s parent.

??? success "New Features"

    - Replace file upload with newer control on artifact detail pages and document list page [RQ:2359]
    - TaraVault licensing has no restrictions [RQ:2530] 
    - Improvements to Convert Incident to Requirement feature [RQ:2600]
    - Breadcrumbs on artifact details page are clickable so you can navigate up hierarchy for an artifact [RQ:2651]
    - Allow for urls that link to folders on a list page [RQ:2640]
    - Can save a filter & column arrangement combination as a "view" [RQ:2642]
    - The ability to update a saved filter [RQ:2652]
    - Spira 6.3 Installer Tasks [RQ:2671]

??? bug "Bug fixes and enhancements"

    - Add tooltip to shared filter that shows the username of the filter creator [IN:4904]
    - The ability to update a saved filter [IN:5048]
    - Admin: User Edit page could potentially show TaraVault DataGrid on Self-Hosted  [IN:5133]
    - Test set and test run custom fields using lists do not sync up correctly if multiple fields use the same list [IN:5156]
    - TaraVault product config page "Edit Users" button broken [IN:5195]
    - Program Incidents & Releases sometimes displays object reference issue [IN:5264]
    - Null Reference thrown if Security Settings nulled out in Admin Page [IN:5268]
    - Improve performance of requirement test and task coverage calculations [IN:5294]
    - Product admins can delete shared filters from the product homepage Shared Searches widget [IN:5303]
    - Automation host filters cannot be retrieved [IN:5320]
    - On association tabs permission checks are not carried out to hide buttons to create new artifact X from artifact Y [IN:5344]
    - Expanders and collapsers on Reports Config page broken [IN:5355]


## Version 6.2.2 (December 2019)

!!! info "Summary"
    **SpiraTeam and SpiraPlan cloud users can use any source code provider**: In addition to our source code provider, TaraVault, cloud customers can choose to use any Git or Subversion provider they wish.

    **Bug fixes and UI improvements**: The improvements include better access to the sidebars on all main pages, and improved search in dropdowns.

??? bug "Bug fixes and enhancements"

    - Build detail page: need ability to collapse description section, or confine it within a scrollable box [IN:4300]
    - Detect and notify the user when they attempt to run a test set with a blank configuration [IN:4655]
    - Html and body tags from rich text fields are not stripped out when rendered outside of CK editors [IN:4666]
    - Cloning workflows does not copy digital signature settings correctly [IN:4674]
    - Administration > Project > Project Associations: cross project artifact dropdown does not show selected artifacts [IN:4881]
    - Accented characters in some grids do not display correctly [IN:4965]
    - Notifications for risks: many fields are blank in the email; warning about exposure [IN:4967]
    - "Source Code" link under Project Admin Menu bounces back to Project Admin Home [IN:5073]
    - Cannot delete Document with Comment [IN:5082]
    - Folder Name on Test Case List not decoding HTML  [IN:5123]
    - Test Case Details: Can Link a Test Case to itself [IN:5131]
    - For rich text custom properties, long custom property name overlaps the field itself [IN:5148]
    - Product delete fails sometimes with a TaraVault foreign key error [IN:5181]
    - Sortable grids add new item erroneously after just adding a new item and clicking buttons like refresh [IN:5192]
    - My Assigned Requirements widget shows numbers for the 6 new statuses [IN:5213]
    - Fix sidebars on list and details pages to the top of the page so they are always visible [IN:5214]
    - Test Execution Page Leave Button no functionality when on a test case not owned [IN:5218]
    - Custom Props of type list: default values are saved but not shown in the admin UI [IN:5224]
    - Export buttons on Requirements list page are set for release permissions, not requirement permissions [IN:5240]
    - User profile page: clicking username copies rss token not username [IN:5243]
    - Search in dropdowns for anywhere in the values, not just at the start [IN:5244]
    - Task board: error occurs when creating a new task with certain settings [IN:5258]
    - Error not shown in association panel when the server throws an error message [IN:5276]
    - Limit the rows displayed on the product dashboard grids [IN:5277]
    - Improve the UI for the Modal Dialog Boxes when creating Custom Reports  [IN:5293]
    - Security fix for user first or last name containing code [IN:5295]


## Version 6.2.1 (October 2019)

!!! info "Summary"
    **Enhanced product template management**: Users can migrate a product from one template to another. This will help you consolidate your templates and streamline your administration more easily.

??? success "New Features"

    - Project Template Migration Wizard implemented [RQ:2489]
    - Installer tasks for cloud and download [RQ:2598]


??? bug "Bug fixes and enhancements"

    - Admin manual: Add info about Product Admin Home and Template Admin Home pages [IN:5020]
    - Requirement - Tasks grid can display timezone based exception when certain dates are null [IN:5061]
    - RSS Token on user profile and admin user/edit should be blurred like for TaraVault [IN:5072]
    - Standalone database did not upgrade from 5.4 to 6.x [IN:5127]
    - When a custom ESQL custom graph has no data, it will display a bad error message [IN:5129]
    - Test set detail page: test case section reflects execution status on list page  [IN:5132]
    - Need to reduce some of the erroneous events that get logged [IN:5169]
    - Name in global nav shows HTML encoded characters for non latin characters [IN:5173]
    - Data Sync Project Mappings Confusion since 6.0 [IN:5187]
    - The Assigned Tasks/Requirements/Pending Runs widget shows too many items [IN:5196]
    - Markierungen is not correct German translation for tags [IN:5197]
    - Folder edit buttons are misaligned in version 6.2.0.1 (regression due to fix for Chrome 76) [IN:5198]
    - Installer: v620 installer forgot one needed DELETE clause [IN:5201]
    - Add Test Set API to allow parallel distributed execution [IN:5203]
    - Performance issue when you have lots of test cases with links/parameters [IN:5204]
    - Documentation link is bad for admin > User Details Edit [IN:5207]
    - Installer can timeout when running a specific part of an upgrade [IN:5209]

## Version 6.2.0.1 (September 2019)

!!! bug "Bug fixes"
    Temporary fix to manage a bug introduced in the latest Chrome browser version


## Version 6.2 (August 2019)

!!! info "Summary"
    **Additional Requirement List Views (SpiraTeam and SpiraPlan only)**: In addition to the current hierarchical list view of requirements, additional views will make it easier for users to work with requirements in ways that work for them at the time.

    **Improved Risk Associations (SpiraPlan only)**: Now you can add links between risks to and from other risks, as well as incidents, test cases, and requirements.

??? success "New Features"

    - MindMapping requirements functionality  [RQ:1708]
    - Additional Task Board View (tasks by Requirement) [RQ:2357]
    - Documentation links take you to new online documentation system [RQ:2587]
    - Requirements list view: document view [RQ:2537]
    - Requirements list view: sortable grid [RQ:2538]
    - Task Board - add by requirement view [RQ:2550]
    - Release Details - show requirement points [RQ:2551]
    - Rename Package to Epic [RQ:2555]
    - Risks has an association panel and can link to risks, tests, requirements, and incidents [RQ:2556]
    - Upgrade jQuery to 2.2.4 [RQ:2568]
    - Requirements 'mind map' view [RQ:2571]
    - Requirements use case diagram [RQ:2572]


??? bug "Bug fixes and enhancements"

    - Admin Product Membership: error when click save, if All Active is selected and there are inactive members [IN:5109]
    - Project Membership table can have bad entries [IN:5165]
    - License Key does not allow FIPS 140-2 compliance.. [IN:3305]
    - Details pages are missing grey background on type/status area [IN:5088]
    - Certain new v6 API calls are not CORS enabled [IN:5094]
    - Getting system error on Admin -> Edit User page [IN:5160]
    - SpiraTest: some tabs are visible to admins but should not be [IN:5163]
    - Installer: Upgrade from v6.0 to v6.1 leaves no Foreign Keys  [IN:5167]
    - On Product Membership page, system error occurs when deleting a member [IN:5180]
    - Allow tasks to be associated to test cases directly [IN:2990]
    - Online help: section 8.1 about the task list progress column is incomplete [IN:4460]
    - Html and body tags from rich text fields are not stripped out when rendered outside of CK editors [IN:4666]
    - New/Clone product: test type 'is exploratory' flag is not copied over from original template [IN:5080]
    - CKeditors on dark mode on live instances do not switch font color correctly [IN:5093]
    - Viewing source code of a rich text editor in dark mode does not work [IN:5102]
    - Installer - v600 upgrade code forgetting to put NOT NULL on a few columns. [IN:5104]
    - Installer: Backup Block Size could throw error. [IN:5108]
    - Some status colors are incorrect for dark and light themes [IN:5111]
    - Installer: Two Columns upgraded to not match Clean Install [IN:5114]
    - Installer: Race condition in Upgrading certain versions [IN:5115]
    - Add ranking labels to planning board detailed view [IN:5121]
    - Force admin to enter product name before product is deleted [IN:5147]
    - Documentation: formatting problem in two topics: Incident Board and Task Board  [IN:5157]
    - Project Data Tool: Correct Requirements inserts wrong Requirement Type [IN:5159]
    - Unable to expand section 11 of the Online User Guide [IN:4626]
    - Product Home, Req Incident Count widget: problem with requirement icons (either missing or huge, depending on browser) [IN:5063]


## Version 6.1.0.1 (July 2019)

!!! bug "Bug fixes"
    - Navigation bar does not properly restrict access to artifacts by Spira version [IN:5092]
    - Improves dark mode and fixes details pages missing grey background on type/status area in the header [IN:5088]


## Version 6.1 (July 2019)

!!! info "Summary"
    **Dark Mode**: The application follows the color scheme you use in your operating system, or you can set it manually. Dark mode makes every part of the application easier on the eyes and look more gorgeous than ever.

    **Improvements to Administration**: With easier filtering and more intuitive controls for key pages like tables and managing workflow permissions, administration is now more user friendly than ever.

    **Version 6 of our SOAP and REST APIs**: Our existing APIs are as compatible as they can be with version 6 of SpiraPlan. The new API version will allow access to new features, such as those from templates.

??? success "New Features"

    - Enable beta dark color mode for modern browsers [RQ:2557]
    - Add new 6.0 API for existing calls [RQ:2308]
    - All workflow status field permissions are set with radio buttons not checkboxes [RQ:2408]
    - Change the artifacts that create an initial item to use a blank name v.s. "New Artifact" [RQ:2498]
    - Admin type, priority, and status pages can be filtered in the same way as components [RQ:2502]
    - Add new API functions for template management [RQ:2542]
    - Can filter admin users and product membership lists by all or active only [RQ:2548]
    - Planning Boards: Hide Statuses that have no transition to them or from them for RQs and TKs [RQ:2549]


??? bug "Bug fixes and enhancements"

    - Issues with inactive products and templates  [IN:5045]
    - Activating old project changes its assigned template [IN:5046]
    - Project role artifact view permissions are being applied, when current user has sys admin permission [IN:4140]
    - Test Set Status Widget includes deleted Test Sets [IN:4363]
    - Permission error: Attachment of a Test run can be deleted with only create permission [IN:4784]
    - API to POST artifacts causes problems on servers east of GMT [IN:4785]
    - Document_RetrieveFolders call dies [IN:4868]
    - Add friendlier error when deleting a test case parameter that is in use [IN:4915]
    - Add ability to clone a product/project in different ways [IN:4945]
    - Workspace dropdown includes inactive templates [IN:4983]
    - Test execution initial screen: cannot proceed after getting a prompt to fill in a required custom field [IN:4999]
    - Test execution: pause button does nothing [IN:5012]
    - Error on Product Admin Dashboard [IN:5021]
    - Installer: Null Reference check missing in PreReq check [IN:5081]
    - Support change/remove user membership for a project using 6.0 API [IN:4107]
    - Add ability to specify/change project group with API [IN:4108]
    - User defined start page not properly remembered on refresh/login [IN:4966]
    - On revision detail page, the link "Back to Revision List" is incorrect [IN:4974]
    - SpiraPlan: risk default values and sample data contain a misspelling [IN:4976]
    - Test configuration detail page: entries do not appear unless you refresh the page [IN:4978]
    - For TaraVault users, admin menu for product settings has incorrect label [IN:4995]
    - Project Home: All Pending Test Runs, change permissions for reassign and delete buttons [IN:4998]
    - Test execution: in table view, Pass All button does not work at first [IN:5016]
    - Tree view wraps and obscures long names - eg on adding an existing attachment [IN:5036]
    - Screen images not correctly sized on test run details page [IN:5037]
    - Installer: Upgrade overwrites existing 'DataSync' config file. [IN:5040]
    - Blank space is shown where the main nav bar should be, under certain circumstances involving an inactive template [IN:5062]
    - Test configuration detail page: remove button does not work [IN:4979]
    - Test execution: table view, image button has no label [IN:5015]
    - Admin Project History list has Revert and Purge All too close together [IN:5039]
    - Risk Details: 'Empty' name watermark doesn't match other Details Screens [IN:5068]
    - Installer: Not properly entering DataSyncConfig config tokens. [IN:5075]


## Version 6.0.0.3 (May 2019)

!!! bug "Bug fixes"
    - Displaying reports shows error (SpiraTest only) [IN:5000]
    - Null error when saving a test from Rapise into Spira 6.0.0.2 [IN:5004]
    - On premise installer fixes


## Version 6.0 (April 2019)

!!! info "Summary"
    **Enterprise Risk Management [SpiraPlan only]**: Risks have their own types, statuses, workflows, and mitigations. New reports for risks, as well as charts and a risk cube have been added. 

    **Changes to certain names in the system**: Projects are now called Products; Project Groups are now Programs; and Iterations are now Sprints.

    **Better manage your products (projects) with templates**: Templates now control many aspects of a product (such as notifications, workflows, custom fields), and can control many products at once. Each existing product from 5.4 will have its own template. Every new product can have its own template or be managed by an existing template.

    **New customizations at the template level**: Requirement, Test Case, Document, and Task types are customizable. Documents can now be managed using workflows to allow you to control versioning and check-ins. Notifications now apply to products in a template and no longer the same system wide.

    **Improve navigation and new administration user interface**: New login screens and a completely reworked navigation menu in the application make using SpiraPlan easier than ever. Navigation is more mobile friendly and intuitive. Administration menus are now only ever one click away.

??? success "New Features"

    - Risk Administration (Project Template)
        - Edit Risk Statuses [RQ:2417]
        - Edit Risk Types [RQ:2418]
        - Edit Risk Impacts [RQ:2419]
        - Edit Risk Probabilities [RQ:2420]
        - Notifications for risks are customizable and get sent out properly [RQ:2488]
        - Edit Risk Workflows [RQ:2421]

    - Risks
        - Top open risks [RQ:2430]
        - Risk List Page sidebar donut chart [RQ:2492]
        - Risk List Page [RQ:2411]
        - Risk Details page displays standard risk fields inc. exposure [RQ:2422]
        - Display risk custom properties [RQ:2423]
        - Risk Mitigations [RQ:2424]
        - Risk Details page Tasks tab [RQ:2425]
        - Risk Details page Discussions / comments [RQ:2427]
        - My Assigned Risks [RQ:2428]
        - Assigned Risks RSS feed [RQ:2429]
        - Project Home Risk Widget / risk cube [RQ:2431]
        - Risk summary report [RQ:2434]
        - Risk detailed report [RQ:2435]

    - Project Templates [RQ:1703]
    - Workflows for documents, plus check-in/out/review [RQ:1930]
    - Switch licensing to annual vs. perpetual [RQ:2306]
    - Database Refactoring/Changes for future functionality [RQ:2174]
    - UI: redesign login pages [RQ:2307]
    - Cross app navigation is intuitive, quick, and clear [RQ:2351]
    - UI: replace gif/png icons with svgs [RQ:2352]
    - Customizable fields for non-incidents [RQ:2309]
    - Refactoring URL structure for existing Admin pages [RQ:2360]
    - New System Administration Home Page [RQ:2362]
    - New Project Admin Home Page [RQ:2365]
    - Add Active flag to Data Sync Plugins [RQ:2366]
    - Updates to program naming [RQ:2368]
    - Make additional fields customizable [RQ:2369]
    - Add database design for BDD support [RQ:2381]
    - Administrators and owners navigation is streamlined and consistent throughout the app [RQ:2390]
    - Users can see My Assigned Documents on the My Page [RQ:2398]
    - Can add and view comments on the document details page, consistent with the workflow [RQ:2399]
    - New installer for 6.0 [RQ:2400]
    - Onboarding framework gives quick info to new and to upgrading users [RQ:2401]
    - Project Template Migration Wizard - disable ability to change template on a product [RQ:2402]
    - Remove Change Projects Button in Admin [RQ:2403]
    - Additional standard statuses for requirements, tasks and test cases [RQ:2409]
    - Change "project" to "product" in the UI to better align with users' real business need [RQ:2455]
    - Switch history tracker to use new MEANING field [RQ:2484]
    - API backwards compatibility to make v3/4/5 work with templates [RQ:2490]
    - Template Admin Home Page  [RQ:2491]
    - Database support for multiple approvers [RQ:2503]


??? bug "Bug fixes and enhancements"

    - System Administration - Add/Edit Users: German translation for "Locked Out" misleading [IN:2230]
    - security issue when having 2 projects open in browser tabs [IN:2651]
    - Limited view role can access source code pages when should not be able to [IN:4754]
    - When a test case is created from a requirement, it lacks the default test step. [IN:3499]
    - Default task notification template does not include the task name [IN:3584]
    - System Error when trying to display the detail page for some Project History Changes [IN:4691]
    - The 'Loading / Activity' notification is nice, but off-screen. [IN:4876]
    - A general system admin should be added as an owner when they create a new template/program/product [IN:4911]
    - Administration > Projects > Project Associations: limit the list of artifact types for selection [IN:4553]
    - Can click on artifact id field on details page to copy to clipboard [IN:4793]
    - Can't easily blank out a previously populated Actual Result in normal test execution [IN:4802]