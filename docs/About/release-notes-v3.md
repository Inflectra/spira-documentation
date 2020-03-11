# Release Notes for Spira v3

## Version 3.2 (December 2011)

!!! success "New features"

    - Language pack for Finnish customers
    - Global search capability across artifacts and projects
    - Build management and integration capabilities
    - Ability to attach a source code file to a SpiraTeam artifact
    - Additional My Page widgets for reading RSS feeds, logging incidents and displaying subscriptions
    - RSS Feeds added to the My Saved Searches and My Subscribed Artifacts widgets

??? bug "Bug fixes and enhancements"

    - Ability to specify multiple IDs for artifact filters in printable reports (+)
    - Print button added to Task Details page (+)
    - Links added to artifact History tabs to make it easier to perform revert and purge operations (+)
    - Application restarts when database previously offline without needing IIS reset (!)
    - Ability to filter reports by selecting a folder / summary requirement to report on just one branch (+)
    - Report option added to list screen toolbars to allow easier reporting on lists of items (+)
    - Ability to more easily attach an existing document from the Documents tab to an artifact (+)
    - Web Service API extended to allow artifact moves (+)
    - Incident closed date automatically cleared when incident moves to open status (-)
    - Allows document version to be set on initial upload and adds screenshot capture to document upload screen (+)
    - Updated navigation bar added to task, automation hosts, documentation and resources pages (+)
    - History entry added to artifacts when they’re exported to a new project to provide auditability (+)
    - Additional token available in Email notification template to allow the last comment/resolution to be included (+)

## Version 3.1 (June 2011)

!!! success "New features"
    - Support for multiple languages
        - Language packs for French, German, Spanish and Czech languages
    - Ability to for project members to view schedules and perform time tracking
    - Version control of all artifacts including undo of updates and deletes
    - Additional dashboard widgets, reports and charts/graphs
        - Document Tag Cloud
        - Burndown, Velocity and Burnup graphs now available in Project Home dashboard
    - Really Simple Syndication (RSS) Feeds of data from My Page dashboard widgets
    - Agile / Scrum Planning Board that allows easier BackLog and Sprint planning
    - New graphing system based on HTML Canvas that allows data and graphs to be exported
    - Enhanced bulk editing tools and ability to perform multiple-item drag and drop ordering

??? bug "Bug fixes and enhancements"

    - Allow custom properties to be reported on in summary (x, y) charts
    - Ability to move/copy documents between folders
    - Add comments fields to all detailed reports
    - New navigation sidebar on requirements, releases and incidents screens
    - Shortcuts for inserting child artifacts and creating artifacts from other types on list pages
    - Easier task editing on Release details page
    - Requirements and Tasks tabs now show both requirements and tasks linked to the Release
    - Predefined date ranges added to date-range filters
    - Long-running tasks (e.g. project delete, copy) run as background tasks to avoid timeout issues

## Version 3.0 (September 2010)

!!! success "New features"

    - Plan requirements (user stories) directly against iterations for enhanced Scrum/Agile support
    - Project members can view team members’ assigned artifacts on a single screen
    - Enhanced Email Notification Functionality including customizable events and email templates
    - Discussion threads available for requirements, releases and tasks
    - Ability to work on different projects at the same time in the same browser session
    - PDF format reports available for the requirements module

??? bug "Bug fixes and enhancements"

    - Performance of application enhanced, with incident details screen completed re-optimized
    - Right-click shortcut menus added to data-grids in the system to reduce scrolling and enhance usability
    - Screenshot utility added to allow easier uploading of screen captures to artifacts in the system
    - Ability to send artifacts directly to individuals through an email sending dialog box
    - Subscription functionality added to allow users to subscribe to specific artifacts in the system
    - Exporting of requirements and releases between projects no longer loses hierarchy when multiple items chosen
    - Sorting artifacts by custom text fields now supported
    - Enhanced API that provides greater access to the system functions with integrated help system
    - Obsolete requirements status added