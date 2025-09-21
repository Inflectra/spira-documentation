# TestComplete
!!! abstract "Compatible with SpiraTest, SpiraTeam, SpiraPlan"

SmarteBear™ TestComplete™ (hereafter TestComplete) is an automated functional test automation system that lets you record application operations and generate test automation scripts in a variety of languages (JavaScript, C\#, VBScript). These test scripts can then be used to playback the test script against the test application and verify that it works correctly.

This section describes how you can use Spira together with RemoteLaunch to schedule and remotely launch instances of TestComplete on different computers and have the testing results be transmitted back to Spira. This allows you to extend your Spira's test management capabilities to include automated TestComplete tests.

*Note: This integration requires at least version 3.0 of Spira and version 8.0 of TestComplete.*

## Installing the TestComplete Engine
This section assumes that you already have a working installation of Spira and have installed RemoteLaunch on the various test automation hosts following the instructions in [RemoteLaunch Guide](RemoteLaunch-Guide.md). Once those prerequisites are in place, please follow these steps:

Download and extract the TestCompleteAutomationEngine.zip file from the Inflectra website and locate the appropriate TestCompleteX.dll or TestExecuteX.dll for the version of TestComplete or TestExecute that you are using.

If you don't see the version listed, just use the nearest version that is *lower* than your current version.

-   Copy the file "TestCompleteX.dll" or "TestExecuteX.dll" (where X is the appropriate version) into the "extensions" sub-folder of the RemoteLaunch installation.
-   Log in to Spira as a system administrator and go into Spira main Administration page and click on the "Test Automation" link under **Integration**.
-   Click the "Add" button to enter the new test automation engine details page. The fields required are as follows:

![](img/TestComplete_34.png)

    -   **Name**: This is the short display name of the automation engine. It can be anything that is meaningful to your users.
    -   **Description**: This is the long description of the automation engine. It can be anything that is meaningful to your users. (Optional)
    -   **Active**: If checked, the engine is active and able to be used for any project.
    -   **Token**: This needs to be the assigned unique token for the automation engine and is used to tell RemoteLaunch which engine to actually use for a given test case. For TestComplete this should be **TestCompleteX** where 'X' is the version number of the DLL file that you are using. For TestExecute this should be **TestExecuteX** where 'X' is the version number of the DLL file that you are using.

*Note: We only use the major version numbers for the token name. So the DLLs TestComplete9.0.dll and TestComplete9.1.dll would both use Token = "TestComplete9".*

Once you have finished, click the "Insert & Close" button and you will be taken back to the Test Automation list page, with TestComplete listed as an available automation engine.

### Advanced Settings
You can modify the TestComplete configuration for each of the specific automation hosts, by right-clicking on the RemoteLaunch icon in the system tray and choosing "Configuration". That will bring up the RemoteLaunch configuration page.

The TestComplete engine adds its own tab to this page which allows you to configure how TestComplete operates:

![](img/TestComplete_35.png)

The following fields can be specified on this screen:

- **Wait Time**: This should be set to the amount of time TestComplete needs on this workstation to close the currently open test. The default value is 10000ms (10 seconds). If you get error messages that TestComplete is still open, you need to increase this value.
- **Application Visible**: This allows you to configure whether the TestComplete application is displayed during test execution or is kept hidden. The default is for it to be hidden.
- **Close TC After Each Test**: When this is selected, the plugin will close the TestComplete application after each test executes. We generally recommend leaving this disabled as the startup and closedown of TestComplete can sometimes interfere with the tests being executed.

## Setting up the Automated Test Cases
This section describes the process for setting up a test case in Spira for automation and linking it to an automated TestComplete test script.

First you need to display the list of test cases in Spira (by clicking Testing \> Test Cases) and then add a new test case. Once you have added the new test case, click on it and select the "Automation" tab:

![](img/TestComplete_36.png)

You need to enter the following fields:

- **Automation Engine** - Choose the TestComplete Automation Engine that you created in the previous section from the drop-down list.
- **Script Type**: This should be set to Linked as the integration with TestComplete only supports referencing TestComplete test project/suite file paths and not physically uploading the test scripts into Spira.
- **Filename**: This is actually a compound of several different components that need to be entered, separated by the pipe (\|) symbol. The syntax depends on whether we want to associate the Spira test case with a specific *project item* or with a specific *test routine*. If you want to use parameterized test cases, you need to link it with a specific routine (see below for more details on parameters).

    - If you want to execute a specific **project item**, the filename should consist of `Suite Filename\|Project Name\|Project Item Name` (e.g. `[CommonDocuments]\TestComplete 7 > Samples\Open Apps\OrdersDemo\C#\TCProject\Orders.pjs|Orders_C#_C#Script|ProjectTestItem1`)
    - If you want to execute a specific **test routine**, the filename should consist of `Suite Filename\|Project Name\|Unit Name\|Routine Name` (e.g. `[CommonDocuments]\TestComplete 7 > Samples\Scripts\Hello\Hello.pjs|Hello_C#Script|hello_cs|Hello`)

    - In the case of executing a specific test routine, the last component (the *routine name*) is actually the name of the function in the test script itself.
    - As illustrated in the examples, for the Test Suite filename, you can use several constants for standard Windows locations to make things easier:

        - \[MyDocuments\] -- The user's "My Documents" folder. The user indicated is the user that ran RemoteLaunch.
        - \[CommonDocuments\] -- The Public Document's folder.
        - \[DesktopDirectory\] -- The user's Desktop folder. The user indicated is the user that ran RemoteLaunch.
        - \[ProgramFiles\] -- Translated to the Program Files directory. For 64-bit machines, it's the 64-bit directory.
        - \[ProgramFilesX86\] -- Translated to the 32-bit Program Files directory.

- **Document Type**: Spira choose which document type the automated test script will be categorized under.
- **Document Folder**: Spira choose which document folder the automated test script will be stored in.
- **Version**: The version of the test script (1.0 is used if no value specified)
- **Test Script**: *This is not used with the TestComplete Engine since it only supports linked test scripts.*

Once you are happy with the values, click \[Save\] to update the test case. Now you are ready to schedule the automated test case for execution.

### Using Parameterized Test Cases
There is an advanced feature of Spira and RemoteLaunch that lets you pass parameters from Spira to your TestComplete automated test script. This is very useful if you have a data-driven TestComplete test script that accepts input parameters. To use this feature you need to use the option described above to link the Spira test case to an explicit test routine inside TestComplete. If you choose the option to link to a Project Item, any parameters passed will be ignored.

To setup the automated test case for parameters, click on the "Test Steps" tab and click on "Edit Parameters":

![](img/TestComplete_37.png)

Since the parameters in Spira map to the function arguments inside a TestComplete test script the parameter names need to match the order of the arguments inside TestComplete (i.e. they are matched by position/order not by name).

*Therefore we recommend using numbers for the parameter names so that it's easy to see which parameter value will be passed to which argument in the test script function.*

## Executing the TestComplete Test Sets from Spira
There are two ways to execute automated test cases in Spira:

1.  Schedule the test cases to be executed on a specific computer (local or remote) at a date/time in the future
2.  Execute the test cases right now on the local computer.

We shall outline both of these two scenarios in this section. However first we need to setup the appropriate automation hosts and test sets in Spira:

### Configuring the Automation Hosts and Test Sets
Go to Testing \> Automation Hosts in Spira to display the list of automation hosts:

![](img/TestComplete_15.png)

Make sure that you have created an Automation Host for each computer that is going to run an automated test case. The name and description can be set to anything meaningful, but the Token field **must be set to the same token that is specified in the RemoteLaunch application** on that specific machine.

Once you have at least one Automation Host configured, go to Testing \> Test Sets to create the test sets that will contain the automated test case:

![](img/TestComplete_38.png)

Note: Unlike manual test cases, automated test cases *must be executed within a test set* -- they cannot be executed directly from the test case.

Create a new Test Set to hold the TestComplete automated test cases and click on its hyperlink to display the test set details page:

![](img/TestComplete_39.png)

You need to add at least one automated test case to the test set and then configure the following fields:

-   **Automation Host**: This needs to be set to the name of the automation host that will be running the automated test set.
-   **Planned Date**: The date and time that you want the scenario to begin. (Note that multiple test sets scheduled at the exact same time will be scheduled by Test Set ID order.)
-   **Status**: This needs to be set to "Not Started" for RemoteLaunch to pick up the scheduled test set. When you change the Planned Date, the status automatically switches back to "Not Started"
-   **Type**: This needs to be set to "Automated" for automated testing

If you have parameterized test cases inside the automated test set you can set their values in three different ways:

-   **Test Set Parameter Values**: this lets you set the same value of a parameter for all the test cases in the test set:

![](img/TestComplete_17.png)

-   **Test Case Parameter Values**: this lets you set a specific value for a parameter for a particular test case in the test set:

![](img/TestComplete_18.png)

You set these values, by right-clicking on a row and choosing "Edit Parameters":

![](img/TestComplete_27.png)

-   **Test Configurations**: this lets you create a data grid of possible test parameters and execute the test set multiple times, once for each unique combination:

![](img/TestComplete_19.png)

### Executing the Test Sets
Once you have set the various test set fields (as described above), the Remote Launch instances will periodically poll Spira for new test sets. Once they retrieve the new test set, they will add it to their list of test sets to execute. Once execution begins they will change the status of the test set to "In Progress", and once test execution is done, the status of the test set will change to either "Completed" --
the automation engine could be launched and the test has completed -- or "Blocked" -- RemoteLaunch was not able to start the automation engine.

If you want to immediately execute the test case on your local computer, instead of setting the "Automation Host", "Status" and "Planned Date" fields, you can instead click the \[Execute\] icon on the test set itself. This will cause RemoteLaunch on the local computer to immediately start executing the current test set.

In either case, once all the test cases in the test set have been completed, the status of the test set will switch to "Completed" and the individual test cases in the set will display a status based on the results of the TestComplete test:

- **Passed**: The TestComplete automated test ran successfully and all the test conditions in the test script passed
- **Failed**: The TestComplete automated test ran successfully, but at least one test condition in the test script failed.
- **Blocked**: The TestComplete automated test did not run successfully

If you receive the "Blocked" status for either the test set or the test cases you should open up the Windows Application Event Log on the computer running RemoteLaunch and look in the event log for error messages.

*Note: While the tests are executing you may see browser or application windows launch as TestComplete executes the appropriate tests.*

Once the tests have completed, you can log back into Spira and see the execution status of your test cases. If you click on a Test Run that was generated by TestComplete, you will see the following information:

![](img/TestComplete_40.png)

This screen indicates the status of the test run that was reported back from TestComplete together with any messages or other information. The Test Name indicates the name of the test inside TestComplete, and the execution status corresponds to the matching status inside TestComplete as illustrated below:

| TestComplete Status | Spira Status |
| ------------------- | ------------ |
| Passed              | Passed       |
| Failed              | Failed       |
| Warning             | Caution      |

In addition, the detailed test report from TestComplete is available in the "Console Output" text-box below. It will contain messages such as:

![](img/TestComplete_41.png)

For the most detail, the "Test Steps" section will contain a step-by-step breakdown of each action taken in the automated test:

![](img/TestComplete_42.png)

### Screenshot Capture
During the execution of the test, TestComplete will capture screenshots of the application being tested. These screenshots are uploaded to Spira so that you have a complete record of the testing activities:

![](img/TestComplete_43.png)

Congratulations... You are now able to run TestComplete automated functional tests and have the results be recorded within Spira.