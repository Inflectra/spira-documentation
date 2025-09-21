# Worksoft Certify
!!! abstract "Compatible with SpiraTest, SpiraTeam, SpiraPlan"

Worksoft Certify is a test automation solution for enterprise applications including SAP, Workday, Salesforce.com, Oracle, and Web Apps. Built to test complex business processes that span multiple applications, Certify ensures that your software and business work exactly as planned.

This section describes how you can use Spira together with RemoteLaunch to schedule and remotely launch instances of Worksoft Certify on different computers and have the testing results be transmitted back to Spira. This allows you to extend your Spira's test management capabilities to include automated Worksoft Certify tests.

*Note: This integration requires at least version 5.0 of Spira and version 10.0 of Worksoft Certify.*

## Installing the Worksoft Certify Engine

This section assumes that you already have a working installation of Spira and have installed RemoteLaunch on the various test automation hosts following the instructions in [RemoteLaunch Guide](RemoteLaunch-Guide.md). Once those prerequisites are in place, please follow these steps:

-   Download and extract the WorksoftCertifyEngine.zip file from the Inflectra website and locate the appropriate WorksoftCertifyEngine.dll for the version of Worksoft Certify that you are using.
-   Copy the file "WorksoftCertifyEngine.dll" into the "extensions" sub-folder of the RemoteLaunch installation.
-   Log in to Spira as a system administrator and go into Spira main Administration page and click on the "Test Automation" link under **Integration**.
-   Click the "Add" button to enter the new test automation engine details page. The fields required are as follows:

![](img/Worksoft_Certify_137.png)

    -   **Name**: This is the short display name of the automation engine. It can be anything that is meaningful to your users.
    -   **Description**: This is the long description of the automation engine. It can be anything that is meaningful to your users. (Optional)
    -   **Active**: If checked, the engine is active and able to be used for any project.
    -   **Token**: This needs to be the assigned unique token for the automation engine and is used to tell RemoteLaunch which engine to actually use for a given test case. For Worksoft Certify this should always be **WorksoftCertify**.

Once you have finished, click the "Insert & Close" button and you will be taken back to the Test Automation list page, with Worksoft Certify listed as an available automation engine:

![](img/Worksoft_Certify_138.png)

### Advanced Settings
You can modify the Worksoft Certify configuration for each of the specific automation hosts, by right-clicking on the RemoteLaunch icon in the system tray and choosing "Configuration". That will bring up the RemoteLaunch configuration page.

The Worksoft Certify engine adds its own tab to this page which allows you to configure how Worksoft Certify operates:

![](img/Worksoft_Certify_139.png)

The following fields can be specified on this screen:

- **Trace Logging** -- When selected, this will log additional trace and debugging information to the Windows Event Log. This should not be selected in a production environment.
- **Certify User** -- This should be populated with a valid username that can login to the Worksoft Certify database that you are using
- **Certify Password** -- This should be populated with a valid password for the user specified in the previous field that can login to the Worksoft Certify database that you are using
- **Test Timeout** -- This tells RemoteLaunch how long to let the Worksoft Certify tests run (in seconds) in the event one of the tests were to not finish property. Once the test report is generated, RemoteLaunch will stop execution, regardless of this setting.
- **Report Generation Time** -- This is how long (in seconds) RemoteLaunch should wait after Worksoft Certify has finished before reading the test report (for sending to Spira). It ensures that Worksoft Certify has enough time to finish writing the report.

## Setting up the Automated Test Cases
This section describes the process for setting up a test case in Spira for automation and linking it to an automated Worksoft Certify test script.

First you need to display the list of test cases in Spira (by clicking Testing \> Test Cases) and then add a new test case. Once you have added the new test case, click on it and select the "Automation" section of the main "Overview" tab:

![](img/Worksoft_Certify_140.png)

You need to enter the following fields:

- **Automation Engine** - Choose the **Worksoft Certify** Automation Engine that you created in the previous section from the drop-down list.
- **Script Type** -- This should be set to Linked as the integration with Worksoft Certify only supports referencing Worksoft Certify projects and not physically uploading the tests into Spira.
- **Filename** -- This needs to contain the following elements at the very least:

    - **/Process="xxxxx"** needs to specify the name of the Worksoft Certify process
    - **/Project="xxxxx"** needs to specify the name of the Worksoft Certify project
    - You can also add other [Worksoft Certify command line options](http://community.worksoft.com/Knowledge-Base/Worksoft-Products/Worksoft-Certify/certify-command-line-options.html)

- **Document Type** -- This allows you to choose which document type the automated test script will be categorized under.
- **Document Folder** --This allows you to choose which document folder the automated test script will be stored in.
- **Version** -- The version of the test script (1.0 is used if no value specified)
- **Test Script** -- *This is not used with the Worksoft Certify Engine since it only supports linked test scripts.*

Once you are happy with the values, click \[Save\] to update the test case. Now you are ready to schedule the automated test case for execution.

## Executing the Worksoft Certify Test Sets from Spira
There are two ways to execute automated test cases in Spira:

1.  Schedule the test cases to be executed on a specific computer (local or remote) at a date/time in the future
2.  Execute the test cases right now on the local computer.

We shall outline both of these two scenarios in this section. However first we need to setup the appropriate automation hosts and test sets in Spira:

### Configuring the Automation Hosts and Test Sets
Go to Testing \> Automation Hosts in Spira to display the list of automation hosts:

![](img/Worksoft_Certify_141.png)

Make sure that you have created an Automation Host for each computer that is going to run an automated test case. The name and description can be set to anything meaningful, but the Token field **must be set to the same token that is specified in the RemoteLaunch application** on that specific machine.

Once you have at least one Automation Host configured, go to Testing \> Test Sets to create the test sets that will contain the automated test case:

![](img/Worksoft_Certify_142.png)

Note: Unlike manual test cases, automated test cases *must be executed within a test set* -- they cannot be executed directly from the test case.

Create a new Test Set to hold the Worksoft Certify automated test cases and click on its hyperlink to display the test set details page:

![](img/Worksoft_Certify_143.png)

Lower down, the list of test cases in the test set are displayed:

![](img/Worksoft_Certify_144.png)

You need to add at least one automated test case to the test set and then configure the following fields:

-   **Automation Host** -- This needs to be set to the name of the automation host that will be running the automated test set.
-   **Planned Date** -- The date and time that you want the scenario to begin. (Note that multiple test sets scheduled at the exact same time will be scheduled by Test Set ID order.)
-   **Status** -- This needs to be set to "Not Started" for RemoteLaunch to pick up the scheduled test set. When you change the Planned Date, the status automatically switches back to "Not Started"
-   **Type** -- This needs to be set to "Automated" for automated testing

### Executing the Test Sets
Once you have set the various test set fields (as described above), the Remote Launch instances will periodically poll Spira for new test sets. Once they retrieve the new test set, they will add it to their list of test sets to execute. Once execution begins they will change the status of the test set to "In Progress", and once test execution is done, the status of the test set will change to either "Completed" --
the automation engine could be launched and the test has completed -- or "Blocked" -- RemoteLaunch was not able to start the automation engine.

If you want to immediately execute the test case on your local computer, instead of setting the "Automation Host", "Status" and "Planned Date" fields, you can instead click the \[Execute\] icon on the test set itself. This will cause RemoteLaunch on the local computer to immediately start executing the current test set.

In either case, once all the test cases in the test set have been completed, the status of the test set will switch to "Completed" and the individual test cases in the set will display a status based on the results of the Worksoft Certify test:

- **Passed** -- The Worksoft Certify automated test ran successfully and all the test steps in the test script passed and no assertions were thrown.
- **Failed** -- The Worksoft Certify automated test ran successfully, but at least one test step failed or at least one assertion failed.
- **Blocked** -- The Worksoft Certify automated test did not run successfully and reported back the **aborted** test status to RemoteLaunch.

If you receive the "Blocked" status for either the test set or the test cases you should open up the Windows Application Event Log on the computer running RemoteLaunch and look in the event log for error messages.

*Note: While the tests are executing you will see browser windows launch as Worksoft Certify* *executes the appropriate tests.*

Once the tests have completed, you can log back into Spira and see the execution status of your test cases. If you click on a Test Run that was generated by Worksoft Certify, you will see the following information:

![](img/Worksoft_Certify_145.png)

This screen indicates the status of the test run that was reported back from Worksoft Certify together with any messages or other information. The Test Name indicates the name of the test inside Worksoft Certify and there will be detailed steps displayed that match the Worksoft Certify execution steps:

![](img/Worksoft_Certify_146.png)

Each of the Spira execution status values corresponds the matching status inside Worksoft Certify as illustrated below:

| **Worksoft Certify Status** | **Spira Status** |
| --------------------------- | ---------------- |
| Passed                      | Passed           |
| Failed                      | Failed           |
| Aborted                     | Blocked          |
| Skipped                     | N/A              |

In addition, the detailed test report from Worksoft Certify is available in the large text-box below. It will contain messages such as:

![](img/Worksoft_Certify_147.png)

Congratulations... You are now able to run Worksoft Certify automated functional tests and have the results be recorded within Spira.

