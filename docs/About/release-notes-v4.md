# Release Notes for Spira v4

## Version 4.2 (October 2014)

!!! success "New features"

    - Ability to have artifact dependencies and associate tasks to incidents
    - Enhanced source code inspection and traceability capabilities including multiple-branch support
    - Refreshed Planning Board for Scrum, Kanban and other agile methodologies
    - Requirements burndown, burnup and velocity graphs added
    - Build details now includes consolidated list of affected artifacts on one screen


??? bug "Bug fixes and enhancements"

    - Code preview and syntax coloring added to source code file viewing pages
    - Task burndown and burnup graphs updated to better visualize the information
    - Associations grids and reports now include the artifact status as an additional field
    - List custom properties can now be categorized as active / inactive and an undelete option has been added
    - Components are now available for categorizing tasks and incidents as well as requirements
    - Performance enhancements when viewing lots of project documents
    - Copying a project now copies the tasks associated with the requirements
    - Ability to rank backlog items in the updated Scrum/Kanban planning boards
    - Dates in reports standardized to all display in user’s local timezone rather than a mix of local and UTC
    - Use case scenario steps added to requirements reports
    - Additional functions added to both the SOAP and REST web service APIs
    - Incident dashboard widgets can now use either Detected Release or Resolved Release for displaying data
    - Sorting fixed on main project administration screen.
    - Build dropdown list now correctly populates on various report configuration screens
    - Rich-text custom properties now render correctly in the various reports


## Version 4.1 (January 2013)

!!! success "New features"

    - Requirement types and customizable requirement workflows
    - Requirements now estimated in story points with evidence-based effort calculations for resource tracking
    - Task types and customizable task workflows
    - Support for organizing tasks into folders
    - Support for use cases and scenarios
    - Ability to manage project components and map requirements into different components
    - Integrated instant messenger capability for enhanced team collaboration
    - Ability to create shared project filters and add them to project dashboards

??? bug "Bug fixes and enhancements"

    - Application-wide performance enhancements especially on slower network connections
    - Filters now displayed for columns that are not visible to the current user
    - Issue associated with indenting/outdenting requirements with deleted children fixed
    - Notifications now include last comment when comment added to artifact
    - Generation of MS-Word and MS-Excel reports now handles complex markup and formatting
    - Generation of Acrobat PDF reports now handles larger reports without timing-out
    - Screenshot capture no longer relies on Java applet, migrated to HTML clipboard API
    - Quick-Filter panel added to requirements, incident and task list pages to increase productivity
    - Global search can now search by keyword and artifact token; resources added to global search
    - Change history for custom properties fixed to handle cases where multiple items updated at once.
    - Requirement name added to task list pages

## Version 4.0 (December 2012)

!!! success "New features"

    - Support for thirty (30) custom properties per artifact and additional property types (date, user, multi-list, rich text, etc.)
    - Ability to raise incidents and add discussion comments from inbound emails
    - Cross-project resource allocation and leveling capabilities
    - Redesigned user interface with enhanced usability and performance
    - Ad-hoc report generator and cross-project reporting capabilities
    - Enhanced permission system with more customizable and granular user roles / permissions
    - Support for displaying data in different timezones depending on user preferences
    - Support for user avatars within enhanced discussion thread system

??? bug "Bug fixes and enhancements"

    - System remembers the custom ordering of columns in the various list pages throughout the application
    - Ability for users to register for new accounts, with administrators able to approve in bulk
    - Progress indicator now displayed on incident list pages and tabs
    - Adobe Acrobat (PDF) format reports now available for all report types
    - Web-based event log added to make remote administration and diagnostics easier
    - Ability to log incidents and view tasks without seeing other users’ information
    - Ability to remove comments from an artifact
    - Ability to give custom properties a default value and make them required fields
    - Ability to edit the names of incident workflow transitions without having to delete and re-add
    - Easier multi-select on datagrids using SHIFT+CLICK to select ranges
    - System can detect unsaved changes and prompt user before navigating away
    - Ability to move non-modal dialog boxes in the system
    - Ordering of comments in discussion threads can now be changed to oldest or newest first date order