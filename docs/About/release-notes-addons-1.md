# Release Notes for Spira Addons
This page shows summary information about releases in Spira's addons, data syncs, integrations, and optional features. 

## May 2023
- **[SalesForce DataSync](../../External-Bug-Tracking-Integration/Using-Spira-with-Salesforce.com)** v1.1.4.0: general performance enhancements, fixes a potential bug that could cause error "429 Too Many Requests" on SalesForce
- **[HP ALM Importer](../../Migration-and-Integration/Migrating-from-HP-ALM)** v6.0.23.0: fixes restoring a corrupted session

## March 2023
- **[Google Sheets](../../Migration-and-Integration/Importing-from-Google-Sheets)** v3.0.0.0: this major release adds support for: adding/editing custom lists and components; adding users and folders; test step custom properties; pagination to handle large amounts of data; and includes general bug fixes.
- **[SalesForce DataSync](../../External-Bug-Tracking-Integration/Using-Spira-with-Salesforce.com)** v1.1.3.0: this release fixes a bug that could cause repeated error messages in the system log

## January 2023
- **[Excel365 import export tool](../../Migration-and-Integration/Importing-from-Microsoft-Excel-(Office365))** v3.0.0.0: this major release adds support for: adding/editing custom lists and components; adding users and folders; test step custom properties; pagination to handle large amounts of data; and includes general bug fixes.

## December 2022
- **[ClickUp Data Sync](../../External-Bug-Tracking-Integration/Using-Spira-with-ClickUp)** (December 2022) first release to allow user to sync their ClickUp workspace and tasks to products and artifacts within SpiraPlan. 
- **[HP ALM Migration Tool](../../Migration-and-Integration/Migrating-from-HP-ALM)** v6.0.22.0: this update adds a resume feature to handle unexpected interruptions. It also redesigns the import process, allowing users to track real-time progress and estimated remaining time
- **[NUnit 3](../../Unit-Testing-Integration/Integrating-with-NUnit/#installing-the-nunit-3-add-in)**: this release adds support for PropertyAttribute in C# code to describe the link to the test cases in Spira as an alternative to listing each test in the SpiraConfig.json file.
- **[ZenDesk](../../Help-Desk-Integration/Zendesk)**: this release improves custom property support, fixes the component field, and includes better error handling and usability improvements. 


## November 2022
- **[Jira Cloud DataSync](../../External-Bug-Tracking-Integration/Using-SpiraTeam-with-Jira-Cloud)** v5.4.2.0: this update includes a number of enhancements and bug fixes:

    - [IN:6678]: When converting due date/start date, account for Jira time being in local not UTC
    - [IN:7446]: Bidirectional synchronization with Jira flaky with different timezones
    - [IN:7030]: Handle rich text in descriptions
    - [IN:6343]: Linking within JIRA for created incidents
    - [IN:6347]: Sync over story points for new requirements
    - [IN:6661]: Support to the incident - requirement associations
    - [IN:7241]: Support to the requirement - requirement associations

- **[qTest](../../Migration-and-Integration/Migrating-from-qTest)**: this update includes bug fixes and enhancements including:

    - Verbose log support
    - Fixes a bug for a timeout that could happen for large amounts of data
    - Fixes a bug for some fields not being imported
    - Fixed duplicate key messages and WCF size limit issues.
    - Fix changed path for signtool
    - Add folder name to logging
    - Fix recursion typo bug
    - Upgraded importer to v6.0 soap API

- **[ServiceNow DataSync](../../External-Bug-Tracking-Integration/Using-Spira-with-ServiceNow)** v5.0.1.0: this update fixes bugs related to the new API standard introduced by the ServiceNow Tokyo 2022, expanding the compatibility of this dataSync plugin with the most recent SNOW version.
- **[SpiraCapture](../../SpiraCapture/User-Guide)**: this update improves incident creation to support all fields and enforces relevant Spira workflows, and update the Chrome manifest to v3. 


## September 2022
- **[Monday.com datasync](../../External-Bug-Tracking-Integration/Using-Spira-with-Monday)** v1.0: synchronizes incidents and tasks between Spira and Monday.com


