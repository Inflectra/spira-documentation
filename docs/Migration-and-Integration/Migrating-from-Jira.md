#  Migrating from Atlassian Jira

This guide explains how to use Inflectra's "Jira Migration Tool" for importing projects, versions, requirements, issues, tasks and associated attachments from Atlassian Jira to SpiraTeam. This tool works with **Jira Cloud**, **Jira Server** and **Jira Data Center** editions.

This migration tool also includes options from migrating data from Jira
plugins such as **XRAY for test management**.

!!! info "Advanced Migration"
    If the functions of this migration tool are not sufficient for your needs, please consider using our "[Advanced Jira to Spira Migration Tool](https://github.com/Inflectra/spira-jira-migration-advanced)". This is an open source tool specifically for migration from Jira Server/DataCenter. It is developed by Inflectra's partner Tietoevry.

## Installing the Jira Migration Tool

This guide outlines how to install the migration tool for Jira onto a workstation so that you can then migrate whole projects from Jira to either SpiraTeam or SpiraPlan (hereafter referred to as SpiraTeam). It assumes that you already have a working installation of SpiraTeam v6.0 or later and a working version of Jira Cloud, Server or Data Center. 

!!! warning "Minimum Version of Spira"
    **You must be on at least SpiraTeam 8.0 to use this tool**. If you have an earlier version of SpiraTeam you will need to upgrade to at least v8.0 before trying to migrate projects.

The Windows installation package can be downloaded from the 'Add-Ons & Downloads" section of the Inflectra website. Once you have obtained the Windows Installer package, simply double-click on the package to begin the installation wizard which should display the following welcome page:

 ![](img/jira-importer-1.png)

Click the <Next\> button, accept the software license, then click <Next\> again to choose the folder to install the migration tool to:

 ![](img/jira-importer-2.png)
 
Choose the folder to install to, and then decide whether the application should be accessible by all users on the workstation or just the current user. Then click the <Install\> button to start the installation process. It will confirm if you want to proceed, click <Next\> then wait for it to finish.

## Using the Jira Migration Tool

Now that you have installed the migration tool, you can launch it at any time by going to Start \> Programs \> Inflectra \> SpiraTeam \> Tools \> Jira Importer. This will launch the migration tool application itself:

### Connecting to Jira

![](img/jira-importer-3.png)

The first thing you need to do is to enter the URL for the instance of Jira that you want to import the information from (typically of the form http://servername/jira for on-premise and https://myinstance.atlassian.net for cloud) together with a valid username and password (or API Key if using Jira Cloud).

Once you have entered this information, click the **Login** button and the list of possible Jira projects will be populated.

![](img/jira-importer-4.png)

Select the Jira project that you want to ***import from***, choose which artifacts you want to import.
The importer currently supports the following:

- **Jira issue types**
    - Requirements
    - Tasks
    - Incidents
- **Other Jira artifacts**
    - Attachments
    - Components
    - Versions
    - Users
- **XRAY test objects**
    - Test Cases
    - Test Runs

### Importing from XRAY Cloud

If you are importing test cases and test runs from XRAY Cloud (not Server or DataCenter), you will also need to enter in the XRAY API Client ID and Client Secret as well.

Once you have confirmed the artifacts, click the **Next** button to move to the next page in the import wizard.

### Connecting to SpiraTeam

![](img/jira-importer-5.png)
 
This page allows you to enter the URL, user name and password (or Api Key if using SSO) that you want to use to access the instance of SpiraTeam that you want to ***import to*** and click **Login**. (Typically the URL is of the form http://servername/SpiraTeam for on-premise and https://myinstance.spiraservice.net for cloud). The version of the importer being used must be compatible with the version of SpiraTeam you're importing into; if not you will receive an error message.

Assuming that the login was successful, next choose the product template that you want the imported project to use. You can also select the option to '--- Create New Template ---' instead, which will instruct the importer to create a brand new product template for the import.
*We recommend this option for test imports to avoid affecting any production templates*

![](img/jira-importer-6.png)

Once you have chosen the template, click the **Next** button to move to the next page in the wizard:

### Mapping Jira Issues Types to SpiraTeam Artifacts

![](img/jira-importer-7.png)

On this page you will map the different SpiraTeam artifacts to the different issue types in Jira. Currently, the following artifact types in SpiraTeam can be mapped to Jira issues:
- **Requirements** (used for user stories, features, epics, etc.)
- **Tasks** (used for tasks and sub-tasks)
- **Incidents** (used for all other issue types such as bugs, defects, issues)
- **Test Case** (used for XRAY test cases and pre-conditions)
- **Test Set** (used for XRAY test plans)
- **Test Run** (used for XRAY test executions)

Once you have mapped the artfiacts, click the **Start Import** button to actually begin the process of importing the various artifacts from Jira into SpiraTeam.

### Importer Progress

![](img/jira-importer-8.png)

Note that the importer will automatically create a new project in SpiraTeam to hold all the artifacts with the same name as that used in Jira.

![](img/jira-importer-9.png)
 
During the import process, as each of the types of artifact are imported, the progress display will change (as illustrated above). Once the import has finished, you will receive a message to that effect and the **Done** button will be enabled. Clicking this button will close the importer. You should now log into SpiraTeam using the same user name and password that was used for the import to view the imported project.

## What is Imported?

The migration tool will import the following Jira artifacts:

- Product Definition together with components, priorities, types and statuses
- Custom Properties and Custom Lists
- Users (but not their roles and permissions)
- Releases
- Requirements
- Tasks
- Incidents, together with their associated lists of priorities and statuses
- Any attachments associated with the requirements, tasks and incidents

The migration tool will import the following XRAY artifacts:

- Test case repositories
- Test steps
- Test sets and test plans
- Test executions

### Requirements

Any of the Jira issue types that are mapped to requirements in SpiraTeam:

![](img/jira-requirements-1.png)

Will be imported into SpiraTeam as types of requirement:

![](img/jira-requirements-2.png)

### Tasks

Any of the Jira issue types that are mapped to tasks in SpiraTeam:

![](img/jira-tasks-1.png)

Will be imported into SpiraTeam as types of task:

![](img/jira-tasks-2.png)

### Incidents

Any of the Jira issue types that are mapped to incidents in SpiraTeam:

![](img/jira-incidents-1.png)

Will be imported into SpiraTeam as types of incident:

![](img/jira-incidents-2.png)

### Test Repositories

The test case folders, hierarchy and names are imported, along with the IDs of the various XRAY test cases:

![](img/jira-xray-importer-1.png)

### Test Steps

The migration tool will migrate XRAY test cases that contain standard steps with an Action, Description, Description and Sample Data:

![](img/jira-xray-importer-2.png)

Note that it will convert XRAY parameters from the formal used in XRAY to those in SpiraTest. It also migrates over the test parameter values from the corresponding XRAY data set.

It will also correctly migrate over any test cases that contain links to other test cases as their steps (or a combination of both):

![](img/jira-xray-importer-3.png)

### Test Sets and Test Plans

The migration tool will migrate the XRAY test sets and test plans into SpiraTest as test sets:

![](img/jira-xray-importer-4.png)

The test sets will be imported into a flat list in SpiraTest (that you can organize by folder, post-migration), together with the mapping to the various test cases included in the XRAY test set or test plan.

### Test Executions

The XRAY test executions and sub-test executions will be imported into SpiraTest together with their mapped test cases and test runs. These will be migrated into SpiraTest as a test run. The various fields and statuses are faithfully migrated.

![](img/jira-xray-importer-5.png)

The test run migration includes the test run step level of detail, with the appropriate XRAY test run step results imported, including the expected result, actual result and any test parameter values:

![](img/jira-xray-importer-6.png)