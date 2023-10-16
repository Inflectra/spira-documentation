# Release Notes for Spira v7

## Version 7.9.0.1 (October 2023)

!!! bug "Bug fixes"

    - Fix details pages not opening correctly when the application is localized to French [IN:8822]


## Version 7.9 (October 2023)

!!! info "Summary"

    - This release brings a brand new [planning board](../../Spira-User-Manual/Planning-Board). Streamlined and beautiful by default. Powerful customizations when you need them for columns, cards, and swimlanes (rows). This takes the beta board released earlier this year to the next level, thanks to the invaluable feedback from customers. The legacy board remains available to help users with the transition. (not available in SpiraTest)
    - Like the planning board, the [task board](../../Spira-User-Manual/Task-Tracking/#task-board) is all new, setting the beta board as the new default. The legacy task board currently remains available. (not available in SpiraTest)
    - What [requirement statuses](../../Spira-Administration-Guide/Template-Requirements/#statuses) show on the planning board can be tailored per product template. This feature was previously only available as a beta, but is now always available (note that it only applies on the new planning board). (not available in SpiraTest)

??? success "New Features"

    * **[Planning Board](../../Spira-User-Manual/Planning-Board) and [Task Board](../../Spira-User-Manual/Task-Tracking/#task-board) (not available in SpiraTest)**

        - As a board user, I use the new planning and task boards by default, but can still access the equivalent legacy board if I need to [RQ:4649]
        - As a task board user, I can change the board setting by dropdowns in a popup, to organize the board to meet my needs [RQ:4687]
        - As a planning board user, I can change the board setting by dropdowns in a popup, to organize the board to meet my needs [RQ:4681]
        - As a board user, I do not see the "All Items" banner header on the boards when no grouping is selected to simplify how I use the board [RQ:4683]
        - As a board user, I do not see the "All items" row when no rows are selected on the boards to simplify how I use the board [RQ:4684]
        - As a board user, I can easily view the planning boards, by improving the spacing and layout of the headers for columns, rows, and groups so I can see more information in less space [RQ:4685]
        - As a board user, I can see the number of cards in the column, row, and group headers of the planning board, to make it easier to know what has data in it [RQ:4686]
        - As a task board user, I can exclusively group by teams and only when rows is set to By Person, to streamline how I can use the board [RQ:4652]
        - As a planning board user, I can use grouping to sometimes improve specific use cases for how I organize the board to meet my needs [RQ:4651]
        - As a planning board user, I can freely pick from any standard list field for either rows or columns, so I can organize the board to meet my needs [RQ:4650]
        - As a board user, when I group by teams I only see teams with people in them for the current product, so I do not see irrelevant information [RQ:4670]
        - As a board user, I can easily expand and collapse rows and groups in a clear and understandable way, to help me setup the board how I need [RQ:4672]
        - As a board user, I do not see columns, rows, or groups for unassigned items by default, to streamline and simplify how I use the board [RQ:4674]
        
    - As a document user, I can [associate a set of documents to any single artifact](../../Spira-User-Manual/Document-Management/#add-associations-in-bulk) in my product from the document list page, to make it quicker to add lots of documents to an artifact [RQ:4682]

??? bug "Bug fixes and enhancements"

    * **Board improvements**

        - Fix boards not sorting user names alphabetically when a release is provided [IN:8603]
        - Fix showing duplicate cards on the beta planning board when moving from Release or Product backlog with no release set to the sprint backlog [IN:8602]
        - Hide the "All Items" banner header on the boards when no grouping is selected to declutter and improve the user experience [IN:8521]
        - Hide the "All items" row when no rows are selected on the boards to streamline the user experience [IN:8524]
        - Improve the design of new boards when showing groups to make it clearer what group the user is currently focused on [IN:8507]
        - Improve the feel of the new planning boards with clearer column and cell differentiation [IN:8539]
        - Improve the usability of the boards when showing rows by making empty rows shorter [IN:8537]
        - Improve the use of vertical space on the new planning boards, by improving the spacing and layout of the headers for columns, rows, and groups [IN:8531]
        - Make it clearer which row a user is looking at on the board by making the row name stick to the left when scrolling horizontally to the right [IN:8540]
        - Make the boards work better when cells have many cards in them by limiting the maximum height of a cell [IN:8543]
        - Make the planning board cards take up less vertical space while still being readable, particularly for the cards showing minimal extra information [IN:8546]
        - Move the save, add and cancel buttons for the default product artifact boards on the artifact popups to make saving changes easier [IN:8562]
        - Show the number of cards in the column, row, and group headers of the planning board, to make it easier to know what has data in it [IN:8560]
        - Simplify the planning board top toolbar by moving the dropdowns into a board settings popup [IN:8503]
        - Simplify the task board top toolbar by moving the dropdowns into a board settings popup [IN:8504]
        - Switch the current beta boards to be the primary board for those pages, and the old main board the legacy board [IN:8381]
        - When showing rows on the board, put row information as a new mini row header bar, instead of in a dedicated column, to preserve horizontal space and improve the user experience [IN:8522]

    - Fix not being able to retrieve program milestones using the API, if there are no program milestone custom property definitions [IN:8627]
    - Replace "k.A." with "N/A" in German in the N/A all testing setting to better align with test execution localization [IN:8672]
    

## Version 7.8 (September 2023)

!!! info "Summary"

    - SpiraPlan (only) adds brand new [program-level reporting](../../Spira-User-Manual/Program-Reports) functionality. Four new standard reports for program milestones and capabilities are now included, or create your own program-level custom reports.
    - Our upgraded [rich text editor](../../Spira-User-Manual/Application-Wide/#rich-text-editor) lets you use @ to quickly find any product member and mention them in comments or a description. Any mentioned user is, where relevant, automatically added to the artifact as a [follower](../../Spira-User-Manual/Application-Wide/#followers).
    - System admins can now quickly see all the programs a user is a member of, with a dedicated tab on the [View/Edit user detailed](../../Spira-Administration-Guide/System-Users/#edit-an-existing-user) screen in system administration.

??? success "New Features"

    - As a product member, [I can add followers to artifacts](../../Spira-User-Manual/Application-Wide/#mentions) I am working on using an @ mention feature, so I can keep my colleagues informed on relevant artifacts [RQ:4653]
    
    * **As a program manager, I can monitor the progress of work in the program using [offline reporting](../../Spira-User-Manual/Program-Reports), so I can analyze current performance**

        - As a report admin, I can create custom reports of [system level history changes](../../Reporting/Custom-Report-Tables/#global--system-history-change-sets), to provide my org with any reports required in this area [RQ:4432]
        - As a report admin, I can create saved [custom reports](../../Spira-Administration-Guide/System-Reporting) of program milestones and capabilities, that will help users' reporting needs [RQ:4626]
        - As a program report user of SpiraPlan, I can access [program level reports for my program](../../Spira-User-Manual/Program-Reports/#reporting-home-page), so that I can create useful reports [RQ:4503]
        - As a program report user, I can generate a [capability summary report](../../Spira-User-Manual/Program-Reports/#capability-summary-report), to help me track their progress [RQ:4644]
        - As a program report user, I can generate a [capability details report](../../Spira-User-Manual/Program-Reports/#capability-summary-report), to help me track progress [RQ:4645]
        
            - As a program report user, I can view associated requirements in a capability details report, to help me track progress [RQ:4666]
            - As a program report user, I can view the history of a capability in its details report, to help me track progress [RQ:4665]
        
        - As a program report user, I can generate a [program milestone summary report](../../Spira-User-Manual/Program-Reports/#program-milestone-summary-report), to help me track their progress [RQ:4642]
        - As a program report user, I can generate a [program milestone details report(../../Spira-User-Manual/Program-Reports/#program-milestone-detailed-report)], to help me track progress [RQ:4643]
            
            - As a program report user, I can view the associated capabilities for a program milestone in its details report, to help me track progress [RQ:4668]
            - As a program report user, I can view the associated releases for a program milestone in its details report, to help me track progress [RQ:4667]
            - As a program report user, I can view the history of a program milestone in its details report, to help me track progress [RQ:4669]


??? bug "Bug fixes and enhancements"

    - Add API operations to let users create, update, and delete product roles [IN:8480]
    - Add a confirmation dialog when an admin [resets a data sync](../../Spira-Administration-Guide/System-Integration/#data-synchronization) to provide options about how far back the data sync should be reset [IN:8384]
    - Add a new API operation to update only FixedBuildId property of an incident to provide faster integration with CI/CD systems [IN:8529]
    - Add an API operation to let users create a blank template with minimal pre-populated fields like statuses, types, or workflows [IN:8437]
    - Add a new API call to let users delete builds [IN:7881]
    - Allow system admins to see a user's program membership with a new Program Membership tab on the admin [edit user page](../../Spira-Administration-Guide/System-Users/#edit-an-existing-user) [IN:3005]

    - Fix non system admins not being able to save changes to test configuration properties on its [detail page](../../Spira-User-Manual/Test-Configuration-Management/#test-configuration-details) [IN:4566]
    - Fix the API to not accept an test case folder, priority, or type ID from invalid products or templates on creation or updates [IN:7320]
    - Fix [product cloning](../../Spira-Administration-Guide/System-Workspaces/#product-cloning) so that it also clones the product's custom properties [IN:7472]
    - Fix editing test set test case mapping using the API so that it requires both test case and test set relevant permissions [IN:7811]
    - Fix the API to create a requirement without a child to set its type [IN:7845]
    - Fix tooltips on the [system history list page](../../Spira-Administration-Guide/System/#system-history-changes) not showing the description for product, program milestone, and capability entries [IN:7874]
    - Fix emoji with skin tones like "🤚🏽" in description fields causing the [Recent Artifacts](../../Spira-User-Manual/User-Product-Management/#recent-artifacts) and [Subscribed Artifacts](../../Spira-User-Manual/User-Product-Management/#my-subscribed-artifacts) widgets on the My Page to break the page [IN:7916]
    - Fix purging a single item from the [product admin history pages](../../Spira-Administration-Guide/Product-General-Settings/#product-history-changes) showing an error "System.guid does not contain a definition for 'Progress''' [IN:8098]
    - Fix getting an error when filtering documents by a custom property on the [document list page](../../Spira-User-Manual/Document-Management/#document-list) or attachment tab [IN:8231]
    - Fix the system admin system-level [custom property definitions page](../../Spira-Administration-Guide/System-Custom-Properties/#edit-custom-properties) not loading correctly if you try to delete a definition that has system history entries [IN:8319]
    - Fix not being able to filter system history records for deleting a program on the [system history list page](../../Spira-Administration-Guide/System/#system-history-changes) [IN:8356]
    - Fix an error message showing when you try and save a capability or program milestone and the creator dropdown is left blank [IN:8357]
    - Fix the [program milestone list page](../../Spira-User-Manual/Program-Milestones/#milestone-list) so that it does not show the release count or requirement count columns [IN:8362]
    - Fix error logging when creating a new program milestone in specific edge cases [IN:8376]
    - Fix the [program milestone](../../Spira-User-Manual/Program-Milestones/#milestone-details) and [capability detail](../../Spira-User-Manual/Program-Capabilities/#capability-details) pages to have fully responsive designs [IN:8388]
    - Fix some idiosyncrasies in the structure of certain translation files to prepare for improvements in German and French translations [IN:8391]
    - Fix the [program milestone](../../Spira-User-Manual/Program-Milestones/#milestone-details) and [risk detail](../../Spira-User-Manual/Risks-Management/#risk-details) pages' toolbar buttons hiding and showing responsively in the correct way [IN:8416]
    - Fix the installer to provide consistent internal file names (inside the installer itself not the application) when upgrading to v7.7 [IN:8473]
    - Fix upgrading to or through Spira v7.7 not unnecessarily upgrading the full-text indexes [IN:8474]


## Version 7.7 (June 2023)

!!! info "Summary"

    - SpiraPlan (only) gains powerful new program features to help you manage delivery of features and releases across multiple products at once. Brand new program level artifacts let you scale your agile practices beyond products like never before.
    - Capabilities let you define cross-product, program-level features. Customize them with types, statuses, priorities, and fully customizable fields. Link capabilities to product requirements to track their progress at a higher level.
    - Program Milestones help you manage deadlines and delivery of product releases. Think of them as sprints for programs. Customize their types, statuses, and more. Tie releases to a milestone to easily see if things are at risk of delay.
    - By linking Capabilities to Program Milestones you can manage multiple capabilities and easily track if relevant features are ready for delivery. Is your Q3 target for a complex interconnected program on time? Are its features at risk? Scaled agile in SpiraPlan surfaces these insights with ease.
    - All these new features have matching new API calls to allow you to extend how you use program artifacts even further.

??? success "New Features"

    - As a developer I can use **SOAP and REST APIs** to manage system level custom properties and lists [RQ:4618]
      
    * **As a program manager, I can plan out the necessary work of the program with **[capabilities](../../Spira-User-Manual/Program-Capabilities)**, linked to product requirements, and release management at the program level, so I can ensure the program objectives will be delivered**

        - As a system admin, I can create, edit, and manage program **capability [types](../../Spira-Administration-Guide/Program-Capabilities/#types)**, so that managers can use this property inside their programs [RQ:4488]
        - As a system admin, I can create, edit, and manage program **capability [priorities](../../Spira-Administration-Guide/Program-Capabilities/#priorities)**, so that managers can use this property inside their programs [RQ:4489]
        - As a system admin, I can create, edit, and manage up to 30 **[custom properties](../../Spira-Administration-Guide/System-Custom-Properties)** for program capabilities, so that managers can use these properties inside their programs [RQ:4427]
        - As a system admin, I can create, edit, and manage program **capability [statuses](../../Spira-Administration-Guide/Program-Capabilities/#statuses)**, so that managers can use this property inside their programs [RQ:4423]
        - As a program member, I can view, create, and edit program capabilities on a filterable **[list page](../../Spira-User-Manual/Program-Capabilities/#capability-list)**, so I can plan out program level work needs [RQ:4424]
        - As a program member, I can organize the program **[capability hierarchy](../../Spira-User-Manual/Program-Capabilities/#capability-list)** on the list page (with one level of children only), so that the requirement structure simple to use but adds meaning [RQ:4425]
        - As a program member, I can view, create, and edit program capabilities on a **[details page](../../Spira-User-Manual/Program-Capabilities/#capability-details)**, so I can plan out program level work needs [RQ:4504]
        - As a program member, I can add or remove **[associations](../../Spira-User-Manual/Program-Capabilities/#requirement-associations)** between capabilities and this program's product requirements, so I can correctly organize my products' requirements [RQ:4426]
        - As a program member, I can see the capability **[progress](../../Spira-User-Manual/Program-Capabilities/#progress)** based off its linked requirements, so I can track progress [RQ:4508]

    * **As a program manager, I can monitor the progress of work in the program so I can analyze current performance and ensure the program is compliant with any reporting or audit standards**

        - As a system admin, I can see changes made to all capabilities **standard fields on the [system history](../../Spira-Administration-Guide/System/#system-history-changes) pages**, to help with internal auditing [RQ:4430]
        - As a system admin, I can see changes made to all capability **custom fields on the [system history](../../Spira-Administration-Guide/System/#system-history-changes) pages**, to help with internal auditing [RQ:4431]
        - As a developer, I can use **SOAP or REST APIs** to manage all relevant information about program capabilities, so that I can automate and extend how my org uses them [RQ:4501]
        - As a report admin, I can create **[custom reports](../../Reporting/Custom-Report-Tables/#capabilities)** of program capabilities, to provide my org with any reports required in this area [RQ:4435]

    * **As a program manager, I can plan out the program delivery timetable with [program milestones](../../Spira-Administration-Guide/Program-Milestones), so I can ensure we meet our program objectives on time**

        - As a system admin, I can create, edit, and manage **program milestone [statuses](../../Spira-Administration-Guide/Program-Milestones/#statuses)**, so that managers can use them inside their programs - Copy [RQ:4500]
        - As a system admin, I can create, edit, and manage **program milestone [types](../../Spira-Administration-Guide/Program-Milestones/#types)**, so that managers can use them inside their programs [RQ:4442]
        - As a system admin, I can create, edit, and manage up to 30 **[custom properties](../../Spira-Administration-Guide/System-Custom-Properties)** for program milestones, so that managers can use these properties inside their programs [RQ:4443]
        - As a program member, I can view program milestones on a filterable **[list page](../../Spira-User-Manual/Program-Milestones/#milestone-list)**, so I can plan out program level work needs [RQ:4437]
        - As a program member, I can **filter and sort** the program milestones [list page](../../Spira-User-Manual/Program-Milestones/#milestone-list) by any available field, so that I can organize my releases into the view I need at that moment [RQ:4438]
        - As a program member, I can view and edit program milestones on a **[details page](../../Spira-User-Manual/Program-Milestones/#milestone-details)**, so I can plan out program level work needs [RQ:4507]
        - As a program member, I can add or remove **[associations](../../Spira-User-Manual/Program-Milestones/#release-associations)** between program milestones and this program's product releases, so I can plan out the scope of the milestone [RQ:4439]
        - As a program member, I can view program milestones' **release [start and end dates](../../Spira-User-Manual/Program-Milestones/#start-and-end-dates)**, to better manage product level timetables [RQ:4509]
        - As a program member, I can view **capability [associations](../../Spira-User-Manual/Program-Milestones/#capability-associations)** to each program milestone, to give me flexibility in seeing how the program data is organized [RQ:4440]
        - As a program member, I can see the total **[progress](../../Spira-User-Manual/Program-Milestones/#progress) of capabilities** for each milestone, so that I can track and manage the program milestone performance [RQ:4441]

    * **As a program manager, I want to monitor the progress of program milestones so I can analyze trends and ensure the program is compliant with any reporting or audit standards**

        - As a system admin, I can see changes made to all program milestone **standard fields on the [system history](../../Spira-Administration-Guide/System/#system-history-changes) pages**, to help with internal auditing [RQ:4447]
        - As a system admin, I can see changes made to all program milestone **custom fields on the [system history](../../Spira-Administration-Guide/System/#system-history-changes) pages**, to help with internal auditing [RQ:4446]
        - As a developer, I can use **SOAP or REST APIs** to manage all relevant information about program milestones, so that I can automate and extend how my org uses them [RQ:4502]
        - As a report admin, I can create **[custom reports](../../Reporting/Custom-Report-Tables/#program-milestones)** of program milestones, to provide my org with any reports required in this area [RQ:4448]
    
    - As a new user, I can see **relevant and meaningful sample data** for program scaled agile, so I can easily understand how the tools works [RQ:4506]


??? bug "Bug fixes and enhancements"

    - Add [Eggplant](https://www.keysight.com/us/en/cmp/2023/eggplant-test-automation.html) as an active Test Automation Engine option in sample data [IN:7934]
    - Fix the installer so that SQL login and DB user credentials are correctly stored during advanced operations [IN:8123]
    - Fix the installer so the correct credentials are always used during upgrades [IN:8126]
    - Fix the installer so the correct connection information is stored in the settings and the log is cleaned up accordingly [IN:8127]
    - Fix the installer so the correct connection information is used when performing backups [IN:8128]
    - When creating a new user with the v7 API set the report admin flag if passed in [IN:8025]


## Version 7.6.1 (May 2023)

!!! info "Summary"

    This release includes a number of performance improvements and bug fixes to streamline user experience.

??? bug "Bug fixes and enhancements"

    - Fix sortable list pages bulk edit "fill with value" feature not working (introduced in 7.6) [IN:8038]
    - Fix sortable list pages bulk edit not working if the left-most column is not the Name field (introduced in 7.6) [IN:8039]
    - Improve performance when editing Test Case parameters by better managing when parameters are refreshed [IN:7996]
    - Improve checking and error handling of full text indexing during upgrades in the installer [IN:8044]
    

## Version 7.6 (April 2023)

!!! info "Summary"

    This release includes a number of performance improvements and bug fixes to streamline user experience.

??? bug "Bug fixes and enhancements"

    **Performance improvements**
    
    - Improve performance when retrieving documents/attachments by caching them locally in the user's browser [IN:7925]
    - Improve performance of product list and details pages with faster and more streamlined loading of dropdowns for users, releases, and requirements [IN:7823]
    - Improve performance when loading the global navigation workspace dropdown to not block initial page loads [IN:7838]

    **Bug fixes**

    - Auto opt-in new installations to beta features by setting the "[enable beta features](../../Spira-Administration-Guide/System/#general-settings)" flag to Yes by default [IN:7977]
    - Fix a bug for on premise customers upgrading from 5.4 to this release or later [IN:7919]
    - Fix test coverage for releases getting out of sync in certain situations (and can otherwise only be resolved by running data tools) [IN:7077]
    - Fix the user's chosen artifact persisting when switching to or from a program (introduced in 7.5) [IN:7959]
    - Fix translation of the yes/no filter field on certain system admin pages like the workspace and user list pages [IN:7982]
    - Fix translation on the System Admin > Edit User page when confirm removing a user from a product [IN:7981]
    - Improve error handling when generating a MS-Word 2007 with large image files [IN:7938]
    - On the beta task board, when grouping by release and filtering by a release with no children, hide the "unassigned items" group [IN:7943]


## Version 7.5 (March 2023)

!!! info "Summary"

    - SpiraPlan and SpiraTeam users can now try out the [new beta task board](../../Spira-User-Manual/Task-Tracking/#beta-task-board). More flexible and powerful than ever before, you can organize your board into columns, swimlanes, and groups to help you focus on the most important tasks at any time.
    - Template admins can now fully customize exactly what [requirement statuses](../../Spira-Administration-Guide/Template-Requirements/#statuses) show on the beta planning board, and in what order. This helps you tailor the beta planning board even further to your needs.
    - A new SpiraApp for SpiraTeam and SpiraPlan lets you conduct [multiple parallel approvals of a requirement](../../SpiraApps/Requirement-Multi-Approvers), with a one click creation of tasks that can be pre-named, and pre-assigned to relevant reviewers

??? success "New Features"

    * **APIs**
        - Implement a v7 of the SOAP API [RQ:4418]
        - Implement a v7 of the REST API [RQ:4417]
    
    * **Cross-Cutting Functionality**

        - As a requirement analyst, I can request [approval of multiple managers](../../SpiraApps/Requirement-Multi-Approvers) before a requirement can proceed through the workflow, so we can have strong oversight and audit trails [RQ:4513]
        - Move background processes from an in memory dictionary to a database table to reduce errors with multiple CPU cores in IIS (and maybe load balancing) [RQ:4505]
        - As a manager, I can [manage associations between requirements and releases](../../Spira-User-Manual/Application-Wide/#associations), and from releases to other releases (in same product only), so it is easy to see/report all requirements that are active for a release [RQ:4510]
    
    * **Beta Planning Board**

        - As a manager using the planning board, when columns are set to status, I can see only the requirement statuses I need and in the correct order for my product, so I can better track and manage work [RQ:4420]
        - As a product template admin, I can [set what statuses should show on the beta planning board](../../Spira-Administration-Guide/Template-Requirements/#statuses) and in what order, so product teams can use the boards more efficiently [RQ:4419]
    
    * **As a manager, I can use the [new beta task board](../../Spira-User-Manual/Task-Tracking/#beta-task-board), so I can better oversee and track the work of my teams**

        - As a manager, I can filter the task board by any currently active release or sprint, so I can focus on the most relevant work at any time [RQ:4408]
        - As a manager, I can set the group by, rows, and columns, so I can quickly and intuitively arrange the board to help me see and manage relevant tasks [RQ:4409]
        - As a task board user, I can group the board by to release, requirement, status, priority, type, person, or team, so I can focus on the most important data [RQ:4413]
        - As a task board user, I can set the columns on the board to release, requirement, status, priority, type, or person, so I can focus on the most important data [RQ:4414]
        - As a task board user, I can set the rows to release, parent requirement, status, priority, type, or person, so I can focus on the most important data [RQ:4415]
        - As a task board user, cards always show in the correct place and can be quickly moved or reordered, so my team can see and manage our work [RQ:4410]
        - As a task board user, I can change the way a task card looks, so I can see the most meaningful information at that moment [RQ:4411]
        - As a task board user, I can view more information about a task and, if I have permissions, edit the task right from the task board, so I can work more efficiently [RQ:4412]

    * **Administration (SpiraPlan only)**

        - As an administrator, I want to see a [list of changes made in the system](../../Spira-Administration-Guide/System/#system-history-changes), to be able to audit and review products and schedules more easily. [RQ:4477]
        - As an administrator, I want to see details of a change made in the system, to allow for a more granular inspection of product or enterprise-level changes. [RQ:4478]

??? bug "Bug fixes and enhancements"

    - Add an [email option](../../Spira-Administration-Guide/System/#email-configuration) to never include the password in a new user confirmation email (when users are created by a system admin) [IN:7805]

    * **APIs**

        - Add ability to see product custom property values on RemoteProject API Object [IN:7771]
        - Add API call to retrieve a paginated set of users [IN:6780]
        - Add API endpoints to allow users to perform full CRUD operations on workflows [IN:7841]
        - Add CRUD operations for Pull Requests in the API [IN:7833]
        - Data Mapping API Endpoints do not validate permissions beyond project membership [IN:7779]
        - Expand User API Object to include all information from admin user screen [IN:7936]
        - Fix the REST API when retrieving active Releases [IN:6835]
        - Improve the naming of API calls to get workflow transitions from ..._RetrieveWorkflowTransitions to ..._RetrieveWorkflowTransitionsForUser [IN:7827]
        - Users without permissions to view certain artifact types should not be able to view and make comments on those artifacts through the API [IN:7773]

    * **Bug Fixes**

        - Add the ability to set limits in the database for the rate at which large calculation stored procedures run (like test case parameter cache refresh) to improve performance [IN:7864]
        - Do not let users be able to select the same option for more than one dropdown on the beta planning boards [IN:7813]
        - Fix description for 'Edit Custom Lists' and 'Product Definitions' (system-wide custom properties) [IN:7781]
        - Fix the product icon missing from the Schedule dashboard widgets [IN:7534]
        - Fix the default sort order on the beta Planning Board to be by Importance/Priority [IN:7740]
        - Fix the export to svg button not displaying on the document details page when working with diagrams [IN:7885]
        - Fix Worx SpiraApp URLs to add slash between artifact token letters and ID [IN:7832]
        - Installer: On 'failQuietly' SQL Commands, change logging behavior to only give summary message, and not full output. [IN:7807]
        - Installer: Renaming indexes should not cause an error, even if index does not exist [IN:7808]
        - Improve performance by improving how attachments are retrieved [IN:7850]
        - Remove all entries of a SpiraApp that are no longer in us [IN:7894]



## Version 7.4 (January 2023)

??? success "Bug fixes and enhancements"

    * **Enhancements**
    
        - Add an API call to retrieve all test sets that contain a specific test case to mirror the functionality on the test set tab of the test case details page in the application [IN:6894]
        - Add API calls to get all releases / requirements that are children of a specified parent release / requirement [IN:5482]
        - Add custom report table for [Attachment Versions] [IN:7757]
        - Add custom report table for [Cross Product Associations](../../Reporting/Custom-Report-Tables/#project-artifacts-sharing) [IN:4242]
        - Add custom report tables for [Source Code Associations](../../Reporting/Custom-Report-Tables/#source-code-associations) and [Source Code Commits](../../Reporting/Custom-Report-Tables/#source-code-commits) [IN:7632]
        - Add JSON File for displaying names of custom data sync fields in [ClickUp Data Sync](../../External-Bug-Tracking-Integration/Using-Spira-with-ClickUp) [IN:7737]
        - Change [WorX SpiraApp](../../SpiraApps/WorX) summary text and description as per software owner's request [IN:7634]
        - If no release provided for a [test execution](../../Spira-User-Manual/Test-Execution), set the wizard's release dropdown to a "Please Select" value and ensure a valid release is provide for execution to start [IN:1205]
    
    * **Bug Fixes**

        - Fix API calls not properly creating manual test runs that have no end date [IN:7596]
        - Fix API to get test sets or test sets for a folder not correctly filtering by a release [IN:7303]
        - Fix blank password custom properties blocking certain API calls [IN:7058]
        - Fix intermittent XSRF error that can show up when having multiple Spira tabs open at the same time [IN:7694]
        - Hide the vertical arrows showing up on grids when users zoom in / out of the page [IN:7630]


## Version 7.3 (December 2022)

!!! info "Summary"
    Introducing our next generation planning board for SpiraTeam and SpiraPlan. Available as a beta alongside the existing planning board, the new board has a brand new look, big new features (including swimlanes), and simpler to use than ever.

    SpiraPlan admins can create teams and assign members of a product to those teams (in beta). Currently teams are available exclusively on the beta planning board.

??? Success "New Features"

    * **[Beta Planning Board](../../Spira-User-Manual/Planning-Board/#beta-planning-board)**

        - The new beta planning board has powerful functionality with a new layout and overhauled design to let you plan work effortlessly [RQ:4286]
        * **There are useful [main display modes](../../Spira-User-Manual/Planning-Board/#view-controls---planning) that dictate how you use the boards**

            - The Product backlog lets managers prioritize ("groom") unplanned work items that do not have a scheduled release [RQ:4368]
            - The Release backlog lets managers review planned or in progress work items [RQ:4369]
            - The sprint backlog lets managers review work in a release and its sprint, or for a single sprint [RQ:4370]
            - When working on the release or sprint backlog there is a [release dropdown](../../Spira-User-Manual/Planning-Board/#view-controls---releases) [RQ:4381]

        * **The planning board makes it easy to customize how the board is organized to help you focus on the right information **

            - [Users can group the board](../../Spira-User-Manual/Planning-Board/#grouping) by certain fields (based on the view) to show one board per member of the group [RQ:4372]
            - Within a board users can choose what field to [organize data by as columns](../../Spira-User-Manual/Planning-Board/#columns) (the x-axis) [RQ:4373]
            - Within a board users can choose what field to [organize data by as rows](../../Spira-User-Manual/Planning-Board/#rows) (the y-axis) [RQ:4374]
        
        * **[Planning board cards design updated with greater customization](../../Spira-User-Manual/Planning-Board/#customizing-the-cards)**

            - Planning board cards always show a standard set of information that is useful and meaningful [RQ:4382]
            - Planning board cards can optionally show the artifact's description, type, status, and position [RQ:4375]
            - Planning board cards can optionally show the artifact's task progress and task mini indicators [RQ:4376]
            - Planning board cards can optionally show the artifact's test coverage and test case mini indicators [RQ:4377]
        
        * **Incident cards can be shown alongside requirement cards for certain views of the Planning Board**

            - When organizing the planning board by priority, incident priority names are matched to requirement importance names [RQ:4379]
            - Incident cards can be displayed alongside requirement cards in certain views of the planning board [RQ:4380]
            - Teams/Tracks Support in Boards (SpiraPlan only) [RQ:2316]

    * **System Administration**

        - System admins [can enable or disable](../../Spira-Administration-Guide/System/#general-settings) beta functionality across the application for their users [RQ:4317]
        - System admins can create and manage [a list of team names](../../Spira-Administration-Guide/System-Users/#view--edit-teams) (SpiraPlan only) [RQ:3689]
        - Product admins can [associate product users to specific teams](../../Spira-Administration-Guide/Product-Users/#team-membership) [RQ:3690]


??? bug "Bug fixes and enhancements"

    - Retain the user-designated ordering on the planning board in all cases (including the first time a card is moved, and moving a card to the end of a stack) [IN:6467]
    - Ensure all incident progress tooltips are shown in the user's local time zone and not in UTC [IN:6573]
    - Improve performance by caching user avatar images in the browser [IN:7287]
    - Fix the SpiraApp for WorX actions that happen when you click the buttons in the column grids [IN:7391]
    - Do not restrict task start and end dates to its release's dates, so that changes to a task whose dates fall outside those of its release are not blocked [IN:7435]
    - Fix the status filter dropdown on the requirement sorted list page not being localized [IN:7470]
    - Show the correct testing settings for SpiraTest (show "Allow users to mark every step in a test case as N/A at once" and hide "Users can create tasks...") [IN:7488]
    - Fix concurrency dates and concurrency checks to serialize using the Invariant Culture to avoid problems using certain cultural settings (for example, Thai) [IN:7499]
    
    * **Logging in and out**

        - Fix a user being logged out and redirected to a broken URL by removing the product ID portion of this broken URL [IN:7584]
        - Fix the browser from getting stuck in a loop if there is unsaved user input after client-side forced session termination [IN:7587]
        - Fix the error that can occur when starting test execution if you have lost the authorization in the current tab for any reason [IN:7607]
        - Fix some actions on the detail pages causing a logged out user to be redirected to a broken URL if their Form Manager, onRetrieve wasn't calling proper URL redirect on Auth Failure [IN:7669]

    * **On premise installer**
    
        - Fix the installer for on premise customers so that users are informed when they are using an incorrect SQL Version for an upgrade [IN:7588]
        - Fix the wrong installer version number being recorded in the web.config file [IN:7612]
        - Fix edge case null reference exception in the installer [IN:7638]
        - When on premise customers upgrade, include the version they are upgrading from on the summary screen and in the log [IN:7610]
    
    * **Documentation and logging**
        - Change the color of the message box about the best browser to use for the document spreadsheet from red to yellow [IN:7563]
        - Clarify the API documentation about what happens when the user create call is made but the user already exists [IN:7618]
        - Fix the help link used for the Rapise Floating Licenses administration page [IN:7490]
        - Correct the v6 SOAP API documentation example for the Document_AddFile method documentation [IN:7654]
        - Record a success audit log message into the event log when any datasync 'Reset Sync' button is pressed. [IN:7525]
        - Turn off logging for a specific "TaraVault active for a product" check to not confuse users with extra noise in the logs [IN:7608]


## Version 7.2 (October 2022)

!!! info "Summary"
    Manage products in a whole new way (SpiraPlan only). New system level custom properties and custom lists let program users see and manage your products with custom data and through new dedicated pages and custom report options. You can use these new features for improved Project Portfolio Management, to implement product charts, and much more.

    Along with existing support for creating and editing dynamic documents inside Spira (including diagrams and documents), the new spreadsheet editor lets you create simple spreadsheets to better organize your teams and track work. You can have multiple sheets, apply formatting to cells, use a wide number of functions, and even import from and export to Excel spreadsheets.

??? Success "New Features"

    - Allow users to create and [edit simple spreadsheets](../../Spira-User-Manual/Document-Management/#editing-spreadsheets) as an option for inline documents [RQ:4322]
    - Email all system administrators every time that the concurrent user limit is exceeded by a user trying to login but can't due to license issues [RQ:4361]
    
    * **Improved Product Management and Customization**
        
        - System admins can add, edit, and remove up to 30 [custom properties](../../Spira-Administration-Guide/System-Custom-Properties/#edit-custom-properties), shared across all products [RQ:4147]
        - System admins can add and manage [system-wide custom lists](../../Spira-Administration-Guide/System-Custom-Properties/#edit-custom-lists) and their values [RQ:4150]
        - The program level [product list page](../../Spira-User-Manual/Program-Products/#product-list) shows all products in a program and lets users see, sort, and filter by any standard or custom field (but not edit) [RQ:4145]
        - The program level [product detail page](../../Spira-User-Manual/Program-Products/#product-details) lets users see all information about a specific product (including custom fields) [RQ:4146]
        - [Custom report views](../../Reporting/Custom-Report-Tables) support [product level custom properties](../../Reporting/Custom-Report-Tables/#global-system-custom-property-definitions), including on the [products report](../../Reporting/Custom-Report-Tables/#projects-products) [RQ:4192]


??? bug "Bug fixes and enhancements"

    - Add a link on the product home page, [overview widget](../../Spira-User-Manual/Product-Homepage/#product-overview) to the new product details page, shown to program members only [IN:7501]
    - Add a new dedicated "Account Lockout Period" [security setting](../../Spira-Administration-Guide/System/#security-settings), so system admins can specify how long a user is locked out for once they enter too many wrong passwords within the relevant window [IN:5010]
    - Add a new system admin [security setting](../../Spira-Administration-Guide/System/#security-settings) to enforce stricter security only possible on HTTPS sites [IN:7359]
    - Fix a typo in the 7.1 onboarding tour about TaraVault [IN:7443]
    - Fix editing tasks or requirements on the [release details page](../../Spira-User-Manual/Release-Management/#reqs-tasks) not triggering notification events [IN:6954]
    - Fix the documentation link on the user's [Add 2-Step Authentication](../../Spira-User-Manual/User-Product-Management/#2-step-authentication) page [IN:7396]
    - Improve explanatory text in two places in administration for the flag that [disables rollup calculations](../../Spira-Administration-Guide/Product-Planning/#testing-settings), and also the 2 pop-up messages [IN:7338]
    - Improve the error pages throughout the app, with a more consistent design in more places, and showing stack trace information to system admins only [IN:6293]
    - Reduce css file sizes by removing Internet Explorer 11 specific rules and values [IN:7412]
    - Show more of the test case names on the [test case grid](../../Spira-User-Manual/Test-Set-Management/#overview---test-cases) of the test set details page (up to 150 characters) [IN:7299]
    - Show the program artifact dropdown when a user goes to a program page before ever going to a product [IN:7474]
    - Update the minimum SQL Server required version under which SpiraPlan can be installed to 2016 [IN:7424]
    - Set the minimum required version of .NET that the application will work under to 4.8 [RQ:3085]
    - When a product has [rollup calculations disabled](../../Spira-Administration-Guide/Product-Planning/#testing-settings), also disable test case parameter hierarchy refreshes [IN:7422]


## Version 7.1 (August 2022)

!!! info "Summary"
    Cloud customers can now [more easily and flexibly set up source code integration](../../Spira-Administration-Guide/System/#taravault-for-source-code) inside SpiraTeam and SpiraPlan. TaraVault is the default provider for Git or Subversion. Along with other quality of enhancements you can now, for each product, either user TaraVault or any other cloud based source code provider. This lets you pick the best provider for each product.

    Our latest [SpiraApp integrates SpiraPlan and OctoPerf](../../SpiraApps/OctoPerf) seamlessly. Kick off load testing in OctoPerf directly from SpiraPlan and the results of the test get logged against each relevant test case.

??? Success "New Features"

    - Ability to switch (at a product level) cloud Spira between [TaraVault and external Git/Subversion](../../Spira-Administration-Guide/System/#taravault-for-source-code) [RQ:4287]
    - A new [SpiraApp integrates SpiraPlan with Octoperf](../../SpiraApps/OctoPerf) to allow users to launch tests directly from Spira and see relevant results as test runs [RQ:4121]

??? bug "Bug fixes and enhancements"

    - Improve diagram export options when viewing a diagram on the document details page to save a diagram as an SVG [IN:7134]
    - Replace Internet Explorer to Edge in sample data, as Internet Explorer has finally, officially retired [IN:7311]
    - Do not let a product have more than one source code provider in active use at any one time [IN:7321]
    - Let product admins disable / enable TaraVault for a product (in addition to full deactivation (hard deletion) as now) [IN:7324]
    - Fix typos and a screenshot in the 7.0 walkthrough popup [IN:7328]
    - Fix the documentation link on the System and Product Admin > SpiraApps settings pages [IN:7330]
    - Fix Product Template custom lists letting you save a blank value name (even though it shows an error suggesting this not allowed) [IN:7384]

    
## Version 7.0 (July 2022)

!!! info "Summary"
    [SpiraApps](../../SpiraApps) bring a brand new of tailoring SpiraTest, SpiraTeam, and SpiraPlan to your needs. Dedicated SpiraApps will extend what is possible, each addressing a specific use case. This release introduces the first 7 SpiraApps and expect more to follow:

    - The FMEA SpiraApp adds full support for Failure Mode & Effects Analysis (FMEA) in the Risk Management module in SpiraPlan (only - not available in SpiraTeam or SpiraTest)
    - New SpiraApps deepen the integration with Github Actions, GitLab Pipelines, and CircleCI Pipelines. Start a new Pipeline or Action directly from SpiraPlan.
    - Two new SpiraApps let you work faster than ever. Create rich descriptions that are automatically added when you create a new artifact. And quickly create a preset list of new tasks or test cases on a requirement or a release to manage workloads better than ever.

    We have updated our data synchronization platform to improve ease of use and simplify setup for administrators, with tailored guidance and information right inside the app.


??? success "New Features"
    * **Data synchronization**

        - Improve ease of use when configuring the most common datasync plugins with better field names and additional helper text [RQ:4280]

    * **Testing**

        - Add [testing setting to mark a whole test case during execution as N/A](../../Spira-Administration-Guide/Product-Planning/#testing-settings) with one click [RQ:4273]
        - Ability to schedule test cases in a test set by Planned Date on the [test case section of the test set details page](../../Spira-User-Manual/Test-Set-Management/#overview-test-cases), and through the API when mapping a new test set to a test case, or updating an existing mapping [RQ:4277]

    * **[SpiraApps](../../SpiraApps)**

        - [CircleCI SpiraApp](../../SpiraApps/CircleCI) integration lets users launch pipelines from Spira and see their results in Spira as builds [RQ:4141]
        - [GitLab CI SpiraApp](../../SpiraApps/GitLab) integration lets users launch pipelines from Spira and see their results in Spira as builds [RQ:4142]
        - [GitHub CI SpiraApp](../../SpiraApps/GitHub) integration lets users launch actions from Spira and see their results in Spira as builds [RQ:4143]
        - Extend the built-in risk functionality by supporting FMEA with a dedicated [FMEA SpiraApp](../../SpiraApps/FMEA) that calculates the Risk Priority Number [RQ:4140]
        - Improved [WorX Manual Testing Accelerator](../../SpiraApps/WorX) functionality, as a new SpiraApp [RQ:4225]
        - Allow users to quickly create [preset tasks or tests cases](../../SpiraApps/Task-Test-Presets) for a specific requirement or release [RQ:4176]
        - Allow users to create artifacts from their details pages with [pre-populated descriptions](../../SpiraApps/Default-Descriptions) (as defined in the SpiraApp settings) [RQ:4224]

    * **SpiraApps Administration**

        - The [system SpiraApps list page](../../Spira-Administration-Guide/System/#spiraapps) lets admins see all available SpiraApps and enable or disable them [RQ:4200]
        - The [system SpiraApps settings page](../../Spira-Administration-Guide/System/#spiraapp-settings) let sys admins manage any system-level settings for the SpiraApp [RQ:4202]
        - The [product SpiraApps list page](../../Spira-Administration-Guide/Product-General-Settings/#spiraapps) lets users see all system-wide active SpiraApps and enable or disable them for the product [RQ:4201]
        - The [product SpiraApps settings page](../../Spira-Administration-Guide/Product-General-Settings/#spiraapp-settings) let users manage any product-level settings for the SpiraApp [RQ:4203]
       
    * **[SpiraApps](../../SpiraApps) Architecture**

        - SpiraApps can be added by Inflectra, storing their functionality, logic, and descriptions in the system [RQ:4211]
        - SpiraApps can be configured by users with system-wide settings [RQ:4212]
        - SpiraApps can be configured by users with product-specific settings [RQ:4213]
        - SpiraApps can run from the button menu toolbar on specific artifact detail pages [RQ:4207]
        - SpiraApps can run from the button menu toolbar on specific artifact list pages [RQ:4206]
        - SpiraApps can run from a custom column shown on artifact grids [RQ:4208]
        - SpiraApps can display as a dashboard widget on the product and reporting home pages [RQ:4209]
        - SpiraApps can run as behind-the-scenes actions, running user-driven events, on artifact details pages [RQ:4214]


??? bug "Bug fixes and enhancements"

    - Add a new API call to get all requirements covered by a specific test case [IN:5862]
    - Add a new API call to update an existing test set test case mapping (can update its owner, planned date, and isTeardown status)  [RQ:4277]
    - Enforce a minimum of two minutes for [authentication expiry settings](../../Spira-Administration-Guide/System/#security-settings) [IN:7174]
    - Fix GitHub Actions integration so that results are always recorded, even if the JSON body contains longs (previously only ints were supported) [IN:7215]
    - Fix GitHub and CircleCI build creation dates not always being the correct timezone [IN:7270]
    - Fix incorrect special character display on the incident and risk workflow transition detail pages [IN:7197]
    - Fix LIS source code commit dates in sample data so that there are no commits in the future [IN:6881]
    - Fix some accented characters not displaying correctly in certain places [IN:7103]
    - Improve the experience of adding comments to an artifact by only showing the "Add Comment" button when a user cannot otherwise edit the artifact (but can add comments) [IN:7111]
    - Let users define product level 'definitions of done' to apply to a requirement through using the new "Task and Test Case Presets" SpiraApp [IN:6052]