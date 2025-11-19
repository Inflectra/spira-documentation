# Release Notes for Spira Addons
This page shows summary information about releases in Spira's addons, data syncs, integrations, and optional features.

## November 2025
- [Jira Cloud Data Synchronization](../External-Bug-Tracking-Integration/Using-SpiraTeam-with-Jira-Cloud.md) v8.3:

    - Bug Fixes and Enhancements:
        - [IN:11692] Fix a bug that could cause an infinite loop of description field updates during bidirectional sync when Plain text is enabled
        - [IN:11722] Simplified description updates when using Rich Text sync

## October 2025
- [Jira Cloud Data Synchronization](../External-Bug-Tracking-Integration/Using-SpiraTeam-with-Jira-Cloud.md) v8.2.2.0:

    - Bug Fixes:
        - [IN:11792] Fix a bug that could happen when using plain text

## September 2025
- [Versioning SpiraApp](../SpiraApps/Versioning.md) released at v1.0

## August 2025
- [Jira Spira QA Coverage app](../External-Bug-Tracking-Integration/Jira-Spira-QA-Coverage.md) v2.2.0:

    - New features: 
        - Improve the addon to optionally show all test cases directly covering a requirement with details about their execution status and date

- [Jira Cloud Data Synchronization](../External-Bug-Tracking-Integration/Using-SpiraTeam-with-Jira-Cloud.md) v8.2.0.0:

    - Bug Fixes and Enhancements:
        - [IN:11450] Fix a bug that prevents the sync of Releases when the Start Date is missing
        - [IN:11419] Fix a bug that prevents rich text sync when a description is required in Jira
        - [IN:11418] Fix 'Association Already Exists' errors in the Event Log related to the plugin
        - [IN:11411] Adds new Sync Mode createReleasesOnly parameter to prevent Release updates in Jira
        - [IN:11507] Fixes API calls to Jira after Atlassian removed Issue Search endpoint for Jira Cloud


## July 2025
- [Jira Cloud Data Synchronization](../External-Bug-Tracking-Integration/Using-SpiraTeam-with-Jira-Cloud.md) v8.1.0.0:

    - Bug Fixes:

        - [IN:11274] [IN:11273] Improves consistency of release/version creation
        - [IN:11271] Fixes a bug where error messages would flood the Event Log when Jira credentials lack permissions
        - [IN:11269] Fixes a bug where Releases were always marked to update
        - [IN:11251] Fixes a bug where Releases were never updated to 'In Progress'
        - [IN:11250] Fixes a bug where Releases with no StartDate would not sync
        - [IN:11258] Fixes a bug where invalid artifact associations would be tempted to be created
        - [IN:11195] Fixes syncing bold text issues from Spira to Jira

## June 2025
- [Jira Cloud Data Synchronization](../External-Bug-Tracking-Integration/Using-SpiraTeam-with-Jira-Cloud.md) v8.0.0.0:

    - New features:
        - New sync mode "Complete", with support for bidirectional sync of Requirements and Tasks between Jira and Spira
        - Bidirectional sync of Releases with no need for artifact association
        - Option for automatic mapping of standard and custom properties based on name matching
        - Option to sync Epic/Story hierarchy into Spira Requirements and vice-versa
        - Support for syncing custom fields of type Release
        - Support for mapping multiple Jira statuses to one Spira status for Tasks and Requirements
        - Option to not sync comments
        - Option to not sync some Jira Types
        - Attachment sync on updates
        - Rich text enhancements, including support for embedded images and files
        - Option to force plain text conversion for descriptions, to keep bidirectional sync of that field
        - Option to sync standard time tracking fields
    
    - Bug Fixes:
        - [IN:9764] [IN:10543] Release type and tags standard fields never resetting
        - [IN:9432] Updates from Spira to Jira may fail if field is required in destination status
        - [IN:8830] DataSync service may fail if API Key is used in some contexts
        - [IN:10846] [IN:10748] [IN:10835] [IN:10837] General code performance and logging updates
        - [IN:10761] Component sync may fail in some bidirectional contexts

- [Desktop Data-Synchronization Utility](../External-Bug-Tracking-Integration/Setting-up-Data-Synchronization.md) v4.1.0.0:
    - Support for extended DataSync plugin properties
- [Standalone Data-Synchronization Windows Service](../External-Bug-Tracking-Integration/Setting-up-Data-Synchronization.md) v8.1.0.0:
    - Support for extended DataSync plugin properties

## December 2024
- [Jira Importer](../Migration-and-Integration/Migrating-from-Jira.md):

    - Handles the import of the following test artifacts from XRAY Cloud as well as XRAY Datacenter and Server:
        - test cases
        - test steps
        - test sets
        - test plans
        - test runs
        - test run steps

- [RemoteLaunch](../RemoteLaunch-User-Guide/RemoteLaunch-Guide.md) v6.0.4.0:

    - RemoteLaunch to support cross-project Test Case executions [IN:10109]
    - Allow all users to login with their RSS token, however they authenticate when logging in to Spira [IN:7579]

## October 2024
- [TestRail Importer](../Migration-and-Integration/Migrating-from-TestRail.md):

    - Handles TestRail API rate limiting when importing from TestRail cloud instances
    - Imports custom fields for test cases and test runs
    - Imports and maps test case priority, type, and status
    - Handles TestRail test cases that don't have any defined steps
    - Imports TestRail test templates as test case types
    - Imports TestRail 'ref' field as Spira custom property
    - Maps TestRail test run cases in a test plan to Spira test set test cases
    - Handles embedded images that were not attached to the case in TestRail 

## September 2024
- [Jira Data Synchronization](../External-Bug-Tracking-Integration/Using-SpiraTeam-with-Jira-Cloud.md):

    - Support mapping 'JiraIssueKey' (if any) to custom property type 'text' for Requirements in Spira. This way, customers can have that value on the requirement's list page
    - Feature of syncing Tags and Labels between Spira and Jira
    - Support of 'duedate' Jira field mapping, Jira -> Spira
    - Improved handling of User custom properties from Jira > Spira Cloud
    - Fixed issues with potential duplicates on next sync cycle
    - Fixed reporter field updating issue, due to improper mapping
    - Feature to turn off synchronization of attachments (after creation), Incidents or Requirements
    - Fixed issue with new Releases creation in Spira

## July 2024
- **[Excel365 import export tool](../Migration-and-Integration/Importing-from-Microsoft-Excel-(Office365).md)** v3.1.0.0: This version limits the maximum page size for Test Cases to 200 records to avoid crashes and memory errors [IN:9509]
- **[Google Sheets](../Migration-and-Integration/Importing-from-Google-Sheets.md)** v3.1.0.0: This version limits the maximum page size for Test Cases to 200 records to avoid crashes and memory errors [IN:9509]

## April 2024
- [Jira Data Synchronization](../External-Bug-Tracking-Integration/Using-SpiraTeam-with-Jira-Cloud.md): Enhanced bidirectional incident synchronization for both **Jira Cloud** and **Jira Server** plugins:
    - Apply more precise timestamp checking to prevent recent Jira updates from blocking a Spira change being processed
    - Update Jira issue before and after executing a status transition to ensure all required fields are submitted

- [Spira Migration Tool](../Migration-and-Integration/Spira-Migration-Tool.md): New desktop tool (Mac OS and Windows) to backup and migration Spira product templates with ease. 

## January 2024
- [Robot Framework Integration](../Unit-Testing-Integration/Integrating-with-Robot-Framework.md): New integration with Robot Framework released [RQ:4753].
- [xUnit Test Integration](../Unit-Testing-Integration/Integrating-with-xUnit-Python.md): New Python parser for xUnit compatible testing frameworks released.

## December 2023
- **[Jira Cloud DataSync](../External-Bug-Tracking-Integration/Using-SpiraTeam-with-Jira-Cloud.md) v6.0** and - **[Jira Server DataSync](../External-Bug-Tracking-Integration/Using-SpiraTeam-with-JIRA-5+.md) v6**: these updates includes a number of enhancements and bug fixes:

    - Add support for JIRA estimate fields [IN:6345]
    - Add the ability to sync requirements and not import new incidents with a new dedicated "NoIncidents" sync mode [IN:6341]
    - Allow the Jira Due Date field to be mapped to a Spira requirement custom property [IN:6672]
    - Fix the first Comment from Jira Cloud sometimes being duplicated in Spira [IN:7689]
    - Fix artifact associations not always syncing for incidents and requirements, and never syncing for tasks [IN:8864]
    - Improve Jira field mapping for "release" fields [IN:8831]
    - Improve logging by capturing the ProjectID from Jira to help debugging [IN:8684]
    - Improve logging by reducing warning entries for similar issues [IN:8815]
    - Improve the names of the different data sync modes to be more meaningful for end users (True becomes noRequirements and Both becomes Bidirectional) [IN:8936]

- [Jira Configuration Helper](../External-Bug-Tracking-Integration/Using-SpiraTeam-with-Jira-Cloud.md/#jira-configuration-helper): adds the ability to filter statuses by project [IN:8686]
- [Jira Migration Tool](../Migration-and-Integration/Migrating-from-Jira.md) : fixes not being able to import users from Jira due to breaking changes in Atlassian's APIs [IN:8840]
- [PyTest Integration](../Unit-Testing-Integration/Integrating-with-PyTest.md): fixes a bug reporting back test results with the correct timezone [IN:9119].


## May 2023
- **[SalesForce DataSync](../External-Bug-Tracking-Integration/Using-Spira-with-Salesforce.com.md)** v1.1.4.0: general performance enhancements, fixes a potential bug that could cause error "429 Too Many Requests" on SalesForce
- **[HP ALM Importer](../Migration-and-Integration/Migrating-from-HP-ALM.md)** v6.0.23.0: fixes restoring a corrupted session

## March 2023
- **[Google Sheets](../Migration-and-Integration/Importing-from-Google-Sheets.md)** v3.0.0.0: this major release adds support for: adding/editing custom lists and components; adding users and folders; test step custom properties; pagination to handle large amounts of data; and includes general bug fixes.
- **[SalesForce DataSync](../External-Bug-Tracking-Integration/Using-Spira-with-Salesforce.com.md)** v1.1.3.0: this release fixes a bug that could cause repeated error messages in the system log

## January 2023
- **[Excel365 import export tool](../Migration-and-Integration/Importing-from-Microsoft-Excel-(Office365).md)** v3.0.0.0: this major release adds support for: adding/editing custom lists and components; adding users and folders; test step custom properties; pagination to handle large amounts of data; and includes general bug fixes.

## December 2022
- **[ClickUp Data Sync](../External-Bug-Tracking-Integration/Using-Spira-with-ClickUp.md)** (December 2022) first release to allow user to sync their ClickUp workspace and tasks to products and artifacts within SpiraPlan. 
- **[HP ALM Migration Tool](../Migration-and-Integration/Migrating-from-HP-ALM.md)** v6.0.22.0: this update adds a resume feature to handle unexpected interruptions. It also redesigns the import process, allowing users to track real-time progress and estimated remaining time
- **[NUnit 3](../Unit-Testing-Integration/Integrating-with-NUnit.md/#installing-the-nunit-3-add-in)**: this release adds support for PropertyAttribute in C# code to describe the link to the test cases in Spira as an alternative to listing each test in the SpiraConfig.json file.
- **[ZenDesk](../Help-Desk-Integration/Zendesk.md)**: this release improves custom property support, fixes the component field, and includes better error handling and usability improvements. 


## November 2022
- **[Jira Cloud DataSync](../External-Bug-Tracking-Integration/Using-SpiraTeam-with-Jira-Cloud.md)** v5.4.2.0: this update includes a number of enhancements and bug fixes:

    - [IN:6678]: When converting due date/start date, account for Jira time being in local not UTC
    - [IN:7446]: Bidirectional synchronization with Jira flaky with different timezones
    - [IN:7030]: Handle rich text in descriptions
    - [IN:6343]: Linking within JIRA for created incidents
    - [IN:6347]: Sync over story points for new requirements
    - [IN:6661]: Support to the incident - requirement associations
    - [IN:7241]: Support to the requirement - requirement associations

- **[qTest](../Migration-and-Integration/Migrating-from-qTest.md)**: this update includes bug fixes and enhancements including:

    - Verbose log support
    - Fixes a bug for a timeout that could happen for large amounts of data
    - Fixes a bug for some fields not being imported
    - Fixed duplicate key messages and WCF size limit issues.
    - Fix changed path for signtool
    - Add folder name to logging
    - Fix recursion typo bug
    - Upgraded importer to v6.0 soap API

- **[ServiceNow DataSync](../External-Bug-Tracking-Integration/Using-Spira-with-ServiceNow.md)** v5.0.1.0: this update fixes bugs related to the new API standard introduced by the ServiceNow Tokyo 2022, expanding the compatibility of this dataSync plugin with the most recent SNOW version.
- **[SpiraCapture](../SpiraCapture/User-Guide.md)**: this update improves incident creation to support all fields and enforces relevant Spira workflows, and update the Chrome manifest to v3. 


## September 2022
- **[Monday.com datasync](../External-Bug-Tracking-Integration/Using-Spira-with-Monday.md)** v1.0: synchronizes incidents and tasks between Spira and Monday.com