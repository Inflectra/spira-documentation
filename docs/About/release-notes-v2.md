# Release Notes for Spira v2

## Version 2.3.1 (March 2010)

!!! success "New features"

    - Ability to browse Source Code repositories and link code revisions to SpiraPlan artifacts
    - Plug-In for the Subversion version control system now available
    - Ability to synchronize incidents with the Mantis bug-tracking system
    - Support for MS-Word and MS-Excel 2007 specific reports

??? bug "Bug fixes and enhancements"

    - Incident graphs not including data before the start of the date-range fixed
    - Issue changing font and text-size in rich-text editor in MSIE fixed
    - Usability of hierarchical dropdown controls improved; auto-suggest added
    - Attachment tab of artifact screens changed to use popup dialog box and sortable grid
    - MS-Office reports now able to display formatted text entered in rich-text editor
    - Issue on list screens where pagination dropdown disabled after clicking Edit, now fixed
    - Dashboard edit settings functionality fixed to work on non-English versions of .NET
    - Issue when filtering by (None) or multiple values causes subsequent insert to fail now fixed
    - Performance improved on requirements and release details pages
    - Associations comments can now be edited after original creation

## Version 2.3 (November 2009)

!!! success "New features"

    - Ability to customize and save report configurations
    - Additional reports and project home page widgets including a requirements traceability matrix
    - Ability to move, reconfigure and customize user/project dashboards
    - Ability to create project groups and view an integrated project group dashboard
    - Support for Windows Authentication when connecting to database
    - Auto-suggest functionality added to dropdowns throughout application
    - Multi-select and date-range filtering added to the various list screens
    - Ability to specify the database catalog and user names when installing
    - Sorting and filtering added to Project Membership and LDAP Import administration screens
    - Expanded API for external system integration

??? bug "Bug fixes and enhancements"

    - Enhanced usability of various controls and selection boxes including a tree-control for selecting test case coverage
    - Enhanced performance of application when lots of releases are defined
    - Adding a test folder to a release or requirement adds all the constituent test cases
    - Ability to sort incident and test run reports
    - Ability to run Test Run reports for all releases not just a single release
    - Filtering incidents by release includes child iterations as part of filter
    - Project title and report overview added to the various reports in the system
    - Summary graphs fixed so that the x-axis values are sorted
    - Performance of project delete function greatly improved
    - Issue where hierarchical pages sometimes display multiple pages of the same filtered data fixed


## Version 2.2 (May 2009)

!!! success "New features"

    - Ability to upload documents to a project and organize into types and folders with meta-tagging
    - Support for versioning of uploaded documents
    - Ability to assign project resources and track personnel capacity
    - Incidents integrated with release/iteration effort planning functionality
    - Enhanced data integration architecture for easier integration with external systems. Use of XML mapping files replaced
    - with GUI-driven data mapping configuration.
    - New AJAX controls for use with hierarchical dropdowns
    - Drag-and-drop AJAX editing of project tasks in the Iteration Planning Screens

??? bug "Bug fixes and enhancements"

    - Ability to switch a row in the artifact grids to edit mode just by clicking on its cell. Similarly support for activating a filter,
    - updating an edited row and canceling an edit operation by use of the Enter and Escape keys now supported
    - Ability to select saved filters directly from the artifact list pages as well as the ‘My Page’
    - Ability to assign all tasks in a requirement to an iteration
    - Incident status drop-down replaced with incident transition action menu for improved usability
    - Incident adjacent move buttons replaced with list of current incidents matching filter – improves consistency with the
    - other parts of the application and improves usability
    - Usability enhancements for editing tasks, including automating updating of linked requirements’ status as well as autosetting of % complete based on changes to tasks status
    - LDAP Integration and Email Integration both support use of SSL-encrypted connections
    - Performance Enhancements on the artifact list screens
    - Data Access Framework migrated from OleDb to native SQL Server libraries for enhanced performance


## Version 2.1 (January 2009)

!!! success "New features"

    - Option to save current filter on requirements, releases, incidents and tasks list pages
    - Ability to copy/export incidents and tasks between projects
    - Multiple-item cut, copy and paste editing added to the various list pages in the application
    - Custom properties support cross-artifact project lists enabling reusability of common list values

??? bug "Bug fixes and enhancements"

    - Requirements list widget added to My Page to display requirements assigned to the current user
    - Enhanced usability of various controls and selection boxes
    - Improved performance of Requirements and Releases list screens
    - Bulk editing of incidents and tasks artifacts on the list screens
    - Validation of URL attachments modified to support additional protocols and URL formats
    - Filtering on hierarchical list pages displays parent folders to provide context of filtered items
    - Ability to filter all list columns on ‘None’ to display items where no value has been specified
    - Bug where newly inserted items appear at top of list (instead of bottom) has been fixed


## Version 2.0.1 (October 2008)

!!! success "New features"

    - Ability to view release and iteration schedules and assign tasks, tests and incidents
    - Release / Iteration planning screen that allows you to quickly reallocate task assignments
    - View the aggregate task progress for a requirement and compare against requirement high-level estimates
    - View the aggregate estimated and actual task effort for a release/iteration and compare against planned values
    - Support for project estimation and actual effort tracking/analysis at the release and iteration levels
    - Ability to attach URLs to artifacts as well as file attachments
    - Additional project planning home page widgets and reports – including velocity, burndown and burnup
    - Ability to create a new requirement from an existing enhancement incident – closing the lifecycle feedback loop

??? bug "Bug fixes and enhancements"

    - Release / iteration information added to Requirements Plan report
    - Enhanced usability on all artifact details screens, including ability to print, create and delete directly from that page
    - Improved performance on the hierarchical list screens (requirements, releases and test cases) including support for
    - variable size pagination
    - Ability to assign an owner to a requirement artifact
    - Project URLs (displayed on the project home page) can now include HTTPS protocol formats
    - Deleting requirements no longer deletes their associated tasks, merely removes the association to the requirement
    - Bug where filtering test cases by a release and the ‘not run’ execution status returned no results has been fixed
    - Clicking on an email link for a non-existent artifact displays a friendly message instead of a system exception.
    - Bug preventing easy editing of list screen text-boxes in Firefox
    - ‘Screen bounce’ issues when editing some pages has been addressed
    - When inserting a new incident, the custom property panel is correctly reset
    - Clicking an item in the drop-down lists used in the hierarchical list screens now closes the drop-down