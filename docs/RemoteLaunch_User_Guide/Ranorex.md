# Ranorex

Ranorex is an automated functional test automation system that lets you
record application operations and generate .NET language (C\#, VB.NET)
test automation scripts that can be used to playback the test script
against the test application.

This section describes how you can use SpiraTest / SpiraTeam (hereafter
SpiraTeam) together with RemoteLaunch to schedule and remotely launch
instances of Ranorex on different computers and have the testing results
be transmitted back to SpiraTeam. This allows you to extend your
SpiraTeam's test management capabilities to include automated Ranorex
tests.

This plugin was developed by one of our partners (step2IT GmbH) but has
been formally tested by Inflectra and is fully supported by Inflectra.

*Note: This integration requires at least version 3.0 of SpiraTest/Team
and version 3.0 of Ranorex.*

## Installing the Ranorex Engine

This section assumes that you already have a working installation of
SpiraTest or SpiraTeam and have installed RemoteLaunch on the various
test automation hosts following the instructions in Section 1 (above).
Once those prerequisites are in place, please follow these steps:

-   Download and extract the RanorexAutomationEngine.zip
file from the Inflectra website and locate the appropriate
RanorexAutomationEngine.dll for the version of Ranorex that you are
using.

-   If you don't see the version listed, just use the nearest
version that is *lower* than your current version.

-   Copy the file "RanorexAutomationEngine.dll" into the "extensions"
sub-folder of the RemoteLaunch installation.

-   Log in to SpiraTeam as a system administrator and go into SpiraTeam
main Administration page and click on the "Test Automation" link
under **Integration**.

-   Click the "Add" button to enter the new test automation engine
details page. The fields required are as follows:\
![](img/Ranorex_111.png)




-   **Name**: This is the short display name of the automation
engine. It can be anything that is meaningful to your users.

-   **Description**: This is the long description of the automation
engine. It can be anything that is meaningful to your users.
(Optional)

-   **Active**: If checked, the engine is active and able to be used
for any project.

-   **Token**: This needs to be the assigned unique token for the
automation engine and is used to tell RemoteLaunch which engine
to actually use for a given test case. For Ranorex this should
always be **RanorexEngine**.

-   Once you have finished, click the "Insert & Close" button and you
will be taken back to the Test Automation list page, with Ranorex
listed as an available automation engine:\
\
![](img/Ranorex_112.png)




### Advanced Settings

You can modify the Ranorex configuration for each of the specific
automation hosts, by right-clicking on the RemoteLaunch icon in the
system tray and choosing "Configuration". That will bring up the
RemoteLaunch configuration page.

The Ranorex engine adds its own tab to this page which allows you to
configure how Ranorex operates:

![](img/Ranorex_113.png)




The following fields can be specified on this screen:

**Result Path** -- This is the folder where the results of Ranorex tests
will be stored. The currently logged-in user needs to have Read/Write
permissions over this folder.

**Trace Logging** -- When selected, this will log additional trace and
debugging information to the Windows Event Log. This should not be
selected in a production environment.

## Setting up the Automated Test Cases

This section describes the process for setting up a test case in
SpiraTeam for automation and linking it to an automated Ranorex test
script.

First you need to display the list of test cases in SpiraTeam (by
clicking Testing \> Test Cases) and then add a new test case. Once you
have added the new test case, click on it and select the "Automation"
tab:

![](img/Ranorex_114.png)




You need to enter the following fields:

**Automation Engine** - Choose the Ranorex Automation Engine that you
created in the previous section from the drop-down list.

**Script Type** -- This should be set to Linked as the integration with
Ranorex only supports referencing Ranorex test script files and not
physically uploading the test scripts into SpiraTeam.

**Filename** -- This needs to be the full path to the Ranorex test
suite.

To make this easier across different machines, you can use several
constants for standard Windows locations (see example in screenshot):

\[MyDocuments\] -- The user's "My Documents" folder. The user indicated
is the user that ran RemoteLaunch.

\[CommonDocuments\] -- The Public Document's folder.

\[DesktopDirectory\] -- The user's Desktop folder. The user indicated is
the user that ran RemoteLaunch.

\[ProgramFiles\] -- Translated to the Program Files directory. For
64-bit machines, it's the 64-bit directory.

\[ProgramFilesX86\] -- Translated to the 32-bit Program Files directory.

If you'd like to pass parameters to Ranorex you can specify them by
separating them from the filename with a pipe ("\|") character. For
example to run a specific Ranorex test case you can use the following
"filename":

c:\\test\\mytestsuit.exe\|/testcase:addDataTest

**Document Type** -- This allows you to choose which document type the
automated test script will be categorized under.

**Document Folder** --This allows you to choose which document folder
the automated test script will be stored in.

**Version** -- The version of the test script (1.0 is used if no value
specified)

**Test Script** -- *This is not used with the Ranorex Engine since it
only supports linked test scripts.*

Once you are happy with the values, click \[Save\] to update the test
case. Now you are ready to schedule the automated test case for
execution.

### Using Parameterized Test Cases

There is an advanced feature of SpiraTest/Team and RemoteLaunch that
lets you pass parameters from SpiraTeam to your Ranorex automated test
suite. This is very useful if you have a data-driven Ranorex test suite
that defines input variables from an external data source.

To setup the automated test case for parameters, click on the "Test
Steps" tab and click on "Edit Parameters":

![](img/Ranorex_115.png)




The name of the parameter ${login} needs to match the name of the
variable defined within the Ranorex script in its variables
configuration.

## Executing the Ranorex Test Sets from SpiraTeam

There are two ways to execute automated test cases in SpiraTeam:

1.  Schedule the test cases to be executed on a specific computer (local
or remote) at a date/time in the future

2.  Execute the test cases right now on the local computer.

We shall outline both of these two scenarios in this section. However
first we need to setup the appropriate automation hosts and test sets in
SpiraTeam:

### Configuring the Automation Hosts and Test Sets

Go to Testing \> Automation Hosts in SpiraTeam to display the list of
automation hosts:

![](img/Ranorex_15.png)




Make sure that you have created an Automation Host for each computer
that is going to run an automated test case. The name and description
can be set to anything meaningful, but the Token field **must be set to
the same token that is specified in the RemoteLaunch application** on
that specific machine.

Once you have at least one Automation Host configured, go to Testing \>
Test Sets to create the test sets that will contain the automated test
case:

![](img/Ranorex_116.png)




Note: Unlike manual test cases, automated test cases *must be executed
within a test set* -- they cannot be executed directly from the test
case.

Create a new Test Set to hold the Ranorex automated test cases and click
on its hyperlink to display the test set details page:

![](img/Ranorex_117.png)




Lower down, the list of test cases in the test set are displayed:

![](img/Ranorex_118.png)




You need to add at least one automated test case to the test set and
then configure the following fields:

-   **Automation Host** -- This needs to be set to the name of the
automation host that will be running the automated test set.

-   **Planned Date** -- The date and time that you want the scenario to
begin. (Note that multiple test sets scheduled at the exact same
time will be scheduled by Test Set ID order.)

-   **Status** -- This needs to be set to "Not Started" for RemoteLaunch
to pick up the scheduled test set. When you change the Planned Date,
the status automatically switches back to "Not Started"

-   **Type** -- This needs to be set to "Automated" for automated
testing

If you have parameterized test cases inside the automated test set you
can set their values in three different ways:

-   **Test Set Parameter Values** -- this lets you set the same value of
a parameter for all the test cases in the test set:\
![](img/Ranorex_17.png)




-   **Test Case Parameter Values** -- this lets you set a specific value
for a parameter for a particular test case in the test set:\
![](img/Ranorex_18.png)


\
You set these values, by right-clicking on a row and choosing "Edit
Parameters":\
![](img/Ranorex_27.png)




-   **Test Configurations** -- this lets you create a data grid of
possible test parameters and execute the test set multiple times,
once for each unique combination:\
![](img/Ranorex_19.png)




### Executing the Test Sets

Once you have set the various test set fields (as described above), the
Remote Launch instances will periodically poll SpiraTeam for new test
sets. Once they retrieve the new test set, they will add it to their
list of test sets to be execute. Once execution begins they will change
the status of the test set to "In Progress", and once test execution is
done, the status of the test set will change to either "Completed" --
the automation engine could be launched and the test has completed -- or
"Blocked" -- RemoteLaunch was not able to start the automation engine.

If you want to immediately execute the test case on your local computer,
instead of setting the "Automation Host", "Status" and "Planned Date"
fields, you can instead click the \[Execute\] icon on the test set
itself. This will cause RemoteLaunch on the local computer to
immediately start executing the current test set.

In either case, once all the test cases in the test set have been
completed, the status of the test set will switch to "Completed" and the
individual test cases in the set will display a status based on the
results of the Ranorex test:

**Passed** -- The Ranorex automated test ran successfully and all the
test steps in the test script passed and no assertions were thrown.

**Failed** -- The Ranorex automated test ran successfully, but at least
one test step failed or at least one assertion failed.

**Caution** -- The Ranorex automated test run successfully, but at least
one warning was logged in one of the test steps.

**Blocked** -- The Ranorex automated test did not run successfully or at
least one timeout error was recorded.

If you receive the "Blocked" status for either the test set or the test
cases you should open up the Windows Application Event Log on the
computer running RemoteLaunch and look in the event log for error
messages.

*Note: While the tests are executing you will see browser windows launch
as Ranorex executes the appropriate tests.*

Once the tests have completed, you can log back into SpiraTeam and see
the execution status of your test cases. If you click on a Test Run that
was generated by Ranorex, you will see the following information:

![](img/Ranorex_119.png)




This screen indicates the status of the test run that was reported back
from Ranorex together with any messages or other information. The Test
Name indicates the name of the test inside Ranorex and the execution
status corresponds the matching status inside Ranorex as illustrated
below:

**Ranorex Status**   **SpiraTeam Status**
Success              Passed
Failed               Failed

In addition, the detailed test report from Ranorex is available in the
large text-box below. It will contain messages such as:

+-----------------------------------------------------------------------+
| \[2011/10/14 14:08:32.795\]\[Debug \]\[Logger\]: Console logger       |
| starting.                                                             |
|                                                                       |
| \[2011/10/14 14:08:32.874\]\[Info \]\[Test\]: Test Suite 'WinForms   |
| Test' started.                                                       |
|                                                                       |
| \[2011/10/14 14:08:32.889\]\[Info \]\[Test\]: Test Case               |
| 'VS2005\_Application\_Test' started.                                |
|                                                                       |
| \[2011/10/14 14:08:33.467\]\[Success\]\[Test\]: Test Module           |
| 'StartWinformsSample' completed with status 'Success'.            |
|                                                                       |
| \[2011/10/14 14:08:33.467\]\[Info \]\[Test\]: Test Module             |
| 'CheckIfApplicationAlive' started.                                  |
|                                                                       |
| \[2011/10/14 14:08:33.608\]\[Info \]\[Validation\]: Validating Exists |
| on item 'WinFormsApp.ButtonTest\_PushButton'.                       |
|                                                                       |
| \[2011/10/14 14:09:55.718\]\[Failure\]\[Test\]: Test Case             |
| 'VS2005\_Application\_Test' completed with status 'Failed'.       |
|                                                                       |
| \[2011/10/14 14:09:55.718\]\[Failure\]\[Test\]: Test Suite 'WinForms |
| Test' completed with status 'Failed'.                              |
+-----------------------------------------------------------------------+

Congratulations... You are now able to run Ranorex automated functional
tests and have the results be recorded within SpiraTest / SpiraTeam.

