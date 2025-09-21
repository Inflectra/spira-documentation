# ZAPTEST
!!! abstract "Compatible with SpiraTest, SpiraTeam, SpiraPlan"

ZAPTEST is a cross-platform and cross-browser software testing solution. Using OCR and Image Based recognition, it's able to automate the testing process without any API, Framework or environment dependencies and work only with a Graphic User Interface

This section describes how you can use Spira together with RemoteLaunch to schedule and remotely launch instances of ZAPTEST on different computers and have the testing results be transmitted back to Spira. This allows you to extend your Spira's test management capabilities to include automated ZAPTEST tests.

*Note: This integration requires at least version 5.0 of Spira and version 11.0 of ZAPTEST.*

## Installing the ZAPTEST Engine

This section assumes that you already have a working installation of Spira and have installed RemoteLaunch on the various test automation hosts following the instructions in [RemoteLaunch Guide](RemoteLaunch-Guide.md). Once those prerequisites are in place, please follow these steps:

-   Download and extract the ZapTestEngine.zip file from the Inflectra website and locate the appropriate     ZapTestEngine.dll for the version of ZAPTEST that you are using.
-   Copy the file "ZapTestEngine.dll" into the "extensions" sub-folder of the RemoteLaunch installation.
-   Log in to Spira as a system administrator and go into Spira main Administration page and click on the "Test Automation" link under **Integration**.
-   Click the "Add" button to enter the new test automation engine details page. The fields required are as follows:

![](img/ZAPTEST_148.png)

    -   **Name**: This is the short display name of the automation engine. It can be anything that is meaningful to your users.
    -   **Description**: This is the long description of the automation engine. It can be anything that is meaningful to your users. (Optional)
    -   **Active**: If checked, the engine is active and able to be used for any project.
    -   **Token**: This needs to be the assigned unique token for the automation engine and is used to tell RemoteLaunch which engine to actually use for a given test case. For ZAPTEST this should always be **ZapTest**.

Once you have finished, click the "Insert & Close" button and you will be taken back to the Test Automation list page, with ZAPTEST listed as an available automation engine:

![](img/ZAPTEST_149.png)

### Advanced Settings
You can modify the ZAPTEST configuration for each of the specific automation hosts, by right-clicking on the RemoteLaunch icon in the system tray and choosing "Configuration". That will bring up the RemoteLaunch configuration page.

The ZAPTEST engine adds its own tab to this page which allows you to configure how ZAPTEST operates:

![](img/ZAPTEST_150.png)

The following fields can be specified on this screen:

- **ZAPTEST Location**: You need to browse to the location of the Standalone ZAPTEST.EXE program (e.g. C:\\Program Files (x86)\\ZAP-fiX\\Standalone)
- **Trace Logging**: When selected, this will log additional trace and debugging information to the Windows Event Log. This should not be selected in a production environment.
- **Report Generation Time**: This is how long (in seconds) RemoteLaunch should wait after ZAPTEST has finished before reading the test report (for sending to Spira). It ensures that ZAPTEST has enough time to finish writing the report.

## Setting up the Automated Test Cases
This section describes the process for setting up a test case in Spira for automation and linking it to an automated ZAPTEST test script.

First you need to display the list of test cases in Spira (by clicking Testing \> Test Cases) and then add a new test case. Once you have added the new test case, click on it and select the "Automation" section of the main "Overview" tab:

![](img/ZAPTEST_151.png)

You need to enter the following fields:

- **Automation Engine** - Choose the **ZapTest** Automation Engine that you created in the previous section from the drop-down list.
- **Script Type**: This should be set to Linked as the integration with ZAPTEST only supports referencing ZAPTEST script files and not physically uploading the tests into Spira.
- **Filename**: This needs to contain the full path to a location on the computer running ZAPTEST where the test script can be found.
- **Document Type**: This allows you to choose which document type the automated test script will be categorized under.
- **Document Folder** --This allows you to choose which document folder the automated test script will be stored in.
- **Version**: The version of the test script (1.0 is used if no value specified)
- **Test Script**: *This is not used with the ZapTest Engine since it only supports linked test scripts.*

Once you are happy with the values, click \[Save\] to update the test case. Now you are ready to schedule the automated test case for execution.

## Executing the ZAPTEST Test Sets from Spira
There are two ways to execute automated test cases in Spira:

1.  Schedule the test cases to be executed on a specific computer (local or remote) at a date/time in the future
2.  Execute the test cases right now on the local computer.

We shall outline both of these two scenarios in this section. However first we need to setup the appropriate automation hosts and test sets in Spira:

### Configuring the Automation Hosts and Test Sets
Go to Testing \> Automation Hosts in Spira to display the list of automation hosts:

![](img/ZAPTEST_152.png)

Make sure that you have created an Automation Host for each computer that is going to run an automated test case. The name and description can be set to anything meaningful, but the Token field **must be set to the same token that is specified in the RemoteLaunch application** on that specific machine.

Once you have at least one Automation Host configured, go to Testing \> Test Sets to create the test sets that will contain the automated test case:

![](img/ZAPTEST_142.png)

Note: Unlike manual test cases, automated test cases *must be executed within a test set* -- they cannot be executed directly from the test case.

Create a new Test Set to hold the ZAPTEST automated test cases and click on its hyperlink to display the test set details page:

![](img/ZAPTEST_153.png)

Lower down, the list of test cases in the test set are displayed:

![](img/ZAPTEST_154.png)

You need to add at least one automated test case to the test set and then configure the following fields:

-   **Automation Host**: This needs to be set to the name of the automation host that will be running the automated test set.
-   **Planned Date**: The date and time that you want the scenario to begin. (Note that multiple test sets scheduled at the exact same time will be scheduled by Test Set ID order.)
-   **Status**: This needs to be set to "Not Started" for RemoteLaunch to pick up the scheduled test set. When you change the Planned Date, the status automatically switches back to "Not Started"
-   **Type**: This needs to be set to "Automated" for automated testing

### Executing the Test Sets
Once you have set the various test set fields (as described above), the Remote Launch instances will periodically poll Spira for new test sets. Once they retrieve the new test set, they will add it to their list of test sets to execute. Once execution begins they will change the status of the test set to "In Progress", and once test execution is done, the status of the test set will change to either "Completed" --
the automation engine could be launched and the test has completed -- or "Blocked" -- RemoteLaunch was not able to start the automation engine.

If you want to immediately execute the test case on your local computer, instead of setting the "Automation Host", "Status" and "Planned Date" fields, you can instead click the \[Execute\] icon on the test set itself. This will cause RemoteLaunch on the local computer to immediately start executing the current test set.

In either case, once all the test cases in the test set have been completed, the status of the test set will switch to "Completed" and the individual test cases in the set will display a status based on the results of the ZAPTEST:

- **Passed**: The ZAPTEST automated test ran completed execution and all the test steps in the test script passed and no failures or warnings were logged.
- **Failed**: The ZAPTEST automated test ran completed execution, but at least one test step failed.
- **Warning**: The ZAPTEST automated test ran completed execution, but at least one test step reported a warning, but no steps completely failed.
- **Blocked**: The ZAPTEST automated test failed to execute because of some configuration error.

If you receive the "Blocked" status for either the test set or the test cases you should open up the Windows Application Event Log on the computer running RemoteLaunch and look in the event log for error messages.

*Note: While the tests are executing you will see browser windows launch as ZAPTEST* *executes the appropriate tests.*

Once the tests have completed, you can log back into Spira and see the execution status of your test cases. If you click on a Test Run that was generated by ZAPTEST, you will see the following information:

![](img/ZAPTEST_155.png)

This screen indicates the status of the test run that was reported back from ZAPTEST together with any messages or other information. The Test Name indicates the name of the test script that was executed and there will be detailed steps displayed that match the ZAPTEST execution steps:

![](img/ZAPTEST_156.png)

Each of the Spira execution status values corresponds the matching status inside ZAPTEST as illustrated below:

| **ZAPTEST Status** | **Spira Status** |
| ------------------ | ---------------- |
| Passed             | Passed           |
| Failed             | Failed           |
| Warning            | Caution          |
| Information        | N/A              |

In addition, the detailed test report from ZAPTEST is available in the large text-box below. It will contain messages such as:

![](img/ZAPTEST_157.png)

Congratulations... You are now able to run ZAPTEST automated functional tests and have the results be recorded within Spira.