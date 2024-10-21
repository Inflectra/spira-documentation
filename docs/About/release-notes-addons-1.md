# Release Notes for Spira Addons
This page shows summary information about releases in Spira's addons, data syncs, integrations, and optional features. 

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

    - Support mapping 'JiraIssueKey' (if any) to custom property type ‘text’ for Requirements in Spira. This way, customers can have that value on the requirement’s list page
    - Feature of syncing Tags and Labels between Spira and Jira
    - Support of 'duedate' Jira field mapping, Jira -> Spira
    - Improved handling of User custom properties from Jira > Spira Cloud
    - Fixed issues with potential duplicates on next sync cycle
    - Fixed reporter field updating issue, due to improper mapping
    - Feature to turn off synchronization of attachments (after creation), Incidents or Requirements
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



