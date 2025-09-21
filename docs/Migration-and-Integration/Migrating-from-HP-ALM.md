#  Migrating from HP ALM
!!! abstract "Compatible with SpiraTest, SpiraTeam, SpiraPlan"

This page outlines how to use the HP ALM Migration Tool to import projects from HP ALM (formerly known as HP Quality Center) into Spira.

!!! info "What can be imported from HP ALM?"
    The migration tool will import the following artifacts:

    - Custom Properties and Custom Lists
    - Users (but not their roles and permissions)
    - Releases
    - Requirements
    - Automation Hosts
    - Test Cases and their associated manual design steps (but not any automated test scripts)
    - Test Runs and their associated manual test steps
    - Test Sets and the association with the test cases
    - Defects, together with their associated lists of priorities and statuses
    - The coverage relationship between requirements and test cases
    - The linkages between any defects and test runs
    - Any attachments associated with the requirements, test cases, test sets or design steps.

## Installing the HP ALM Migration Tool
To get started, you will need to install the migration tool onto a workstation that can access both your HP ALM server, and your Spira application.

You must already have a working installation of Spira v4.0 or later and a working version of HP ALM 11.5 or later. If you are using HP QualityCenter 10.0 or older, please refer to the migration tool and [documentation here](Migrating-from-HP-QualityCenter.md).

The Windows installation package can be downloaded from the "Add-Ons & Downloads" section of the Inflectra website. Once you have obtained the Windows Installer package, simply double-click on the package to begin the installation wizard which should display the following welcome page:

 ![](img/Migrating_from_HP_ALM_69.png)

Click the <Next\> button, accept the software license, then click <Next\> again to choose the folder to install the migration tool to:

 ![](img/Migrating_from_HP_ALM_70.png)
 
Choose the folder to install to, and then decide whether the application should be accessible by all users on the workstation or just the current user. Then click the <Install\> button to start the installation process. It will confirm if you want to proceed, click <Next\> then wait for it to finish.

## Using the HP ALM Migration Tool


### Connecting to HP ALM and choosing artifacts
Now that you have installed the migration tool, you can launch it at any time by going to Start \> Programs \> Inflectra \> SpiraTest \> Tools \> HP ALM Importer. This will launch the migration tool application itself:

![](img/Migrating_from_HP_ALM_71.png)

The first thing you need to do is to enter the URL for the instance of HP ALM that you want to import the information from (typically of the form http://<server name\>/qcbin) together with a valid username and password.

Once you have entered this information, click the <Authenticate\> button and the list of possible domains and projects will be populated. Select the HP ALM domain and project that you want to ***import from*** and click the <Login\> button. If the user has permission to access this project, you will be see a message that the login was successful. 

Assuming this is a new import session, i.e. you are not restoring a previous session, choose the types of artifact you want to import and then click the <Next\> button to move to the next page in the import wizard:

### Connecting to Spira and choosing options
 ![](img/Migrating_from_HP_ALM_72.png)
 
This page allows you to enter the URL, user name and password that you want to use to access the instance of Spira that you want to ***import to*** and click <Login\>. Typically the URL is of the form (http://<server name\>/SpiraTest). The version of the importer being used must be compatible with the version of Spira you're importing into; if not you will receive an error message.

You start the import process from the Spira login screen. There is an "Import Options" box. Here, you can check 'Verbose Logging' to add more log entries to the session log, which will be saved on the computer's Desktop. You can also choose to  'Resume Previous Import Session'. This option is explained [below](#restoring-a-failed-or-canceled-session).

Click the <Start Import\> button to begin the process of importing the various artifacts from HP ALM into Spira. Note that the importer will automatically create a new project in Spira to hold all the artifacts with the same name as that used in HP ALM.

### Import progress
![](img/Migrating_from_HP_ALM_73.png)

During the import process, the importer shows the current session identifier (which is part of the session log name), as well as the progress and estimated remaining time for every artifact. The Event History at the bottom logs important events of the session. As each of the types of artifact are imported, the progress display will change (as shown above). Once the import has finished, you will receive a message to that effect and the <Done\> button will be enabled. Clicking this button closes the importer. You can cancel the importing session at any time by clicking on 'Cancel and Close'. You should now log into Spira using the same username and password that was used for the import to view the imported project.

*Note: Once you have migrated a project into Spira you will have the definitions of incident priorities and statuses from both Spira and HP ALM (this is because HP ALM doesn't use the same codes as Spira, so they will be imported).*

*You should go back in to the Administration screen and make all the standard Spira statuses and priorities inactive, and then create a new incident workflow using the imported HP ALM statuses.*

## Restoring a failed or canceled Session

If you can cancel a session part way through, or the session fails for any reason, you can easily resume importing artifacts from that session. To do this:

- provide your ALM credentials normally on the first screen (you can ignore the artifact selection) and hit 'Next'. 
- on the second screen, provide your Spira credentials and check 'Resume Previous Import Session'. 
- click on the 'Import Session File' button. You should see then a list of previous session folders (if not, point it to `ApplicationData]\Spira_ALM_QC_Importer_Sessions`). 
- select the folder > header.log file that corresponds to the session being restored, based on the date and time

![](img/Migrating_from_HP_ALM_74.png)

You should see then the identification of the session, followed by the artifacts previously selected for it:

![](img/Migrating_from_HP_ALM_75.png)

At this point, you can add or remove artifacts from the session. Please note that artifacts that already started importing can not now be deselected. In our example, only Test Runs, Users, and Attachments are not disabled. Since we didn't select Attachments originally, if you check off that box, it will include attachments for **new** artifacts - changes will not be made to artifact attachments already imported to Spira. Press 'Start Import' and wait a few seconds until the program loads the previous session data and continues from the point it stopped previously:

![](img/Migrating_from_HP_ALM_76.png)

Wait until the import session successfully ends. Congratulations, you have just imported your data from HP ALM to Spira!