# Using SpiraTeam with JIRA 3 / 4

This section outlines how to use SpiraTest, SpiraPlan or SpiraTeam
(hereafter referred to as SpiraTeam) in conjunction with the JIRA
issue/bug tracking system versions 3.0 -- 4.0. The built-in integration
service allows the quality assurance team to manage their requirements
and test cases in SpiraTeam, execute test runs in SpiraTest, and then
have the new incidents generated during the run be automatically loaded
into JIRA. Once the incidents are loaded into JIRA as issues, the
development team can then manage the lifecycle of these issues in JIRA,
and have the status changes in JIRA be reflected back in SpiraTeam.

In addition, if you are using JIRA 4.x or higher, any issues logged
directly into JIRA will get imported into SpiraTeam so that they can be
linked to test cases and requirements.

► STOP! Please make sure you have first read the Instructions in Section
1 before proceeding!

## Configuring the Plug-In

The next step is to configure the plug-in within SpiraTeam so that the
system knows how to access the JIRA server. To start the configuration,
please open up SpiraTeam in a web browser, log in using a valid account
that has System-Administration level privileges and click on the System
\> Data Synchronization administration option from the left-hand
navigation:

![](img/Using_SpiraTeam_with_JIRA_3__4_9.png)




This screen lists all the plug-ins already configured in the system.
Depending on whether you chose the option to include sample data in your
installation or not, you will see either an empty screen or a list of
sample data-synchronization plug-ins.

If you already see an entry for **JiraDataSync** you should click on its
"Edit" link. If you don't see such an entry in the list, please click on
the \[Add\] button instead. In either case you will be taken to the
following screen where you can enter or modify the JIRA
Data-Synchronization plug-in:

![](img/Using_SpiraTeam_with_JIRA_3__4_52.png)




You need to fill out the following fields for the JIRA Plug-in to
operate correctly:

-   **Name** -- this needs to be set to **JiraDataSync**. This needs to
match the name of the plug-in DLL assembly that was copied into the
C:\\Program Files\\SpiraTeam\\Bin folder (minus the .dll file
extension). If you renamed the JiraDataSync.dll file for any reason,
then you need to change the name here to match.

-   **Description** -- this should be set to a description of the
plug-in. This is an optional field that is used for documentation
purposes and is not actually used by the system.

-   **Connection Info** -- this should the full URL to the JIRA
installation's web-service API. This is typically [http://\<jira
server name\>/rpc/soap/jirasoapservice-v2]{.underline}.

-   **Login** -- this should be set to a valid login to the JIRA
installation. The login needs to have permissions to create and view
issues and versions within JIRA.

-   **Password** -- this should be set to the password of the login
specified above.

-   **Time Offset** -- normally this should be set to zero, but if you
find that issues being changed in JIRA are not being updated in
SpiraTeam, try increasing the value as this will tell the
data-synchronization plug-in to add on the time offset (in hours)
when comparing date-time stamps. Also if your JIRA installation is
running on a server set to a different time-zone, then you should
add in the number of hours difference between the servers'
time-zones here.

The remaining fields work differently depending on which version of the
plugin you are using (JIRA 3.x or JIRA 4.x):

[a) JIRA 3.x Plugin]{.underline}

Please fill out the fields as follows:

-   **Auto-Map Users** -- this is not currently used and can be ignored.

-   **Custom 01** -- This is used to specify a JIRA custom property that
should be mapped to the built-in SpiraTeam Incident Severity field
(which does not exist in JIRA). This can be left empty for now and
will be discussed below in section 3.2.

-   **Custom 02 -- 05** -- these are not currently used by the plug-in
and should be left blank.

[b) JIRA 4.x Plugin]{.underline}

Please fill out the fields as follows:

-   **Auto-Map Users** -- This changes the way that the plugin maps
users in SpiraTeam to those in JIRA:

-   **Auto-Map = True\
**With this setting, all users in SpiraTeam need to have the
same username as those in JIRA. If this is the case then you do
not need to perform the user-mapping task outlined in section
3.2.2. This is a big time-saver if you can guarantee that all
usernames are the same in both systems.

-   **Auto-Map = False\
**With this setting, users in SpiraTeam and JIRA are free to
have different usernames because you specify the corresponding
JIRA name for each user as outlined in section 3.2.2.**\
**

-   **Custom 01** -- This is used to specify a JIRA custom property that
should be mapped to the built-in SpiraTeam Incident Severity field
(which does not exist in JIRA). This can be left empty for now and
will be discussed below in section 3.2.

-   **Custom 02** -- This should be set to the word "True" if you want
to have the new issues submitted to JIRA be submitted using a
specified SecurityLevel. If you're not using the security level
feature of JIRA, leave the field blank.

-   **Custom 03** -- This should be set to the word "True" if you want
to have the plugin restrict synchronization to only loading new
incidents from SpiraTeam \> JIRA and updating existing items. This
is useful if you want to prevent existing issues in JIRA from being
loaded into SpiraTeam. Leave blank if you want the plugin to
synchronize normally.

-   **Custom 04** -- This should be set to the word "True" if you want
to have the plugin copy file attachments from SpiraTeam \> JIRA.
This can use additional system resources and may fail if the files
are too large for JIRA's API to handle. Leave the field blank if you
want the default behavior -- which is to not synchronize
attachments.

-   **Custom 05** - When you click "Force Resync" inside SpiraTeam it
will attempt to resynchronize all incidents/issues from 1/1/1900.
Sometimes that causes the JIRA API to timeout or exceed the maximum
allowed number of results if there are a large number of existing
issues in JIRA.\
\
You can set this field to a specific year (e.g. 1995) or year and
month (e.g. 2010-11) to restrict how far back the system will look
for existing issues. If you leave this field blank it will use the
default value of "1900-01".

> **Note: For most users, we recommend leaving Custom 01 -- Custom 05
> blank.**

## Configuring the Data Mapping

Next, you need to configure the data mapping between SpiraTeam and JIRA.
This allows the various projects, users, releases, incident types,
statuses, priorities and custom property values used in the two
applications to be related to each other. This is important, as without
a correct mapping, there is no way for the integration service to know
that an "Enhancement" in SpiraTeam is the same as a "New Feature" in
JIRA (for example).

The following mapping information needs to be setup in SpiraTeam:

The mapping of the project identifiers for the projects that need to be
synchronized

The mapping of users in the system

The mapping of releases (equivalent to JIRA versions) in the system

The mapping of the various standard fields in the system

The mapping of the various custom properties in the system

Each of these is explained in turn below:

### Configuring the Project Mapping

From the data synchronization administration page, you need to click on
the "View Project Mappings" hyperlink next to the JIRA plug-in name.
This will take you to the data-mapping home page for the currently
selected project:

![](img/Using_SpiraTeam_with_JIRA_3__4_53.png)




If the project name does not match the name of the project you want to
configure the data-mapping for, click on the "(Change Project)"
hyperlink to change the current project.

To enable this project for data-synchronization with JIRA, you need to
enter:

**External Key** -- This should be set to the name of the project token
in JIRA. Typically this is a three-letter acronym for the project.

**Active Flag** -- Set this to 'Yes' so that SpiraTeam knows that you
want to synchronize data for this project. Once the project has been
completed, setting the value to "No" will stop data synchronization,
reducing network utilization.

Click \[Update\] to confirm these settings. Once you have enabled the
project for data-synchronization, you can now enter the other data
mapping values outlined below.

***Note: Once you have successfully configured the project, when
creating a new project, you should choose the option to "Create Project
from Existing Project" rather than "Use Default Template" so that all
the project mappings get copied across to the new project.***

### Configuring the User Mapping

To configure the mapping of users in the two systems, you need to go to
Administration \> Users \> View Edit Users, which will bring up the list
of users in the system. Then click on the "Edit" button for a particular
user that will be editing issues in JIRA:

![](img/Using_SpiraTeam_with_JIRA_3__4_54.png)




You will notice that below the Active flag for the user is a list of all
the configured data-synchronization plug-ins. In the text box next to
the JIRA Data-Sync plug-in you need to enter the login for this username
in JIRA. This will allow the data-synchronization plug-in to know which
user in SpiraTeam match which equivalent user in JIRA. Click \[Update\]
once you've entered the appropriate login name. You should now repeat
for the other users who will be active in both systems.

### Configuring the Release Mapping

When the data-synchronization service runs, when it comes across a
release/iteration in SpiraTeam that it has not seen before, it will
create a corresponding "Version" in JIRA. Similarly if it comes across a
new Version in JIRA that it has not seen before, it will create a new
Release in SpiraTeam. Therefore when using both systems together, it is
recommended that you only enter new Releases/Versions in one system and
let the data-synchronization service add them to the other system.

However you may start out with the situation where you already have
pre-existing Releases/Version in both systems that you need to associate
in the data-mapping. If you don't do this, you may find that duplicates
get created when you first enable the data-synchronization service.
Therefore for any Releases/Iterations that already exist in BOTH systems
please navigate to Planning \> Releases and click on the
Release/Iteration in question. Make sure you have the 'Overview' tab
visible and expand the "Details" section of the release/iteration:

![](img/Using_SpiraTeam_with_JIRA_3__4_55.png)




In addition to the standard fields custom properties configured for
Releases, you will see an additional text property called
"**JiraDataSync ID**" that is used to store the mapped external
identifier for the equivalent Version in JIRA. You need to locate the ID
of the equivalent version in JIRA, enter it into this text-box and click
\[Save\]. You should now repeat for all the other pre-existing releases.

*Note: The JIRA ID can be found by looking at the URL inside JIRA when
choosing to View/Edit the version name/description. The URL will include
the section: **id=X** where X is the numeric ID of the version inside
JIRA.*

### Configuring the Standard Field Mapping

Now that the projects, user and releases have been mapped correctly, we
need to configure the standard incident fields. To do this, go to
Administration \> System \> Data Synchronization and click on the "View
Project Mappings" for the JiraDataSync plug-in entry:

![](img/Using_SpiraTeam_with_JIRA_3__4_53.png)




From this screen, you need to click on Priority, Severity, Status and
Type in turn to configure their values:

[a) Incident Type]{.underline}

Click on the "Type" hyperlink under Incident Standard Fields to bring up
the Incident type mapping configuration screen:

![](img/Using_SpiraTeam_with_JIRA_3__4_56.png)




The table lists each of the incident types available in SpiraTeam and
provides you with the ability to enter the matching JIRA issue type ID
for each one. You can map multiple SpiraTeam fields to the same JIRA
fields (e.g. Bug and Incident in SpiraTeam are both equivalent to Bug in
JIRA), in which case only one of the two values can be listed as Primary
= Yes as that's the value that's used on the reverse synchronization
(from JIRA \> SpiraTeam).

*Note: The JIRA ID can be found by looking at the URL inside JIRA when
choosing to View/Edit the Issue Type. The URL will include the section:
**id=X** where X is the numeric ID of the Issue Type inside JIRA.*

[b) Incident Status]{.underline}

Click on the "Status" hyperlink under Incident Standard Fields to bring
up the Incident status mapping configuration screen:

![](img/Using_SpiraTeam_with_JIRA_3__4_57.png)




The table lists each of the incident statuses available in SpiraTeam and
provides you with the ability to enter the matching JIRA issue status ID
for each one. You can map multiple SpiraTeam fields to the same JIRA
fields (e.g. New and Open in SpiraTeam are both equivalent to Open in
JIRA), in which case only one of the two values can be listed as Primary
= Yes as that's the value that's used on the reverse synchronization
(from JIRA \> SpiraTeam).

We recommend that you always point the New and Open statuses inside
SpiraTeam to point to the ID for "Open" inside JIRA and make Open in
SpiraTeam the Primary status of the two. This is recommended so that as
new incidents in SpiraTeam get synched over to JIRA, they will get
switched to the Open status in JIRA which will then be synched back to
"Open" in SpiraTeam. That way you'll be able to see at a glance which
incidents have been synched with JIRA and those that haven't.

*Note: The JIRA ID can be found by looking at the URL inside JIRA when
choosing to View/Edit the Issue Status. The URL will include the
section: **id=X** where X is the numeric ID of the Issue Status inside
JIRA.*

[c) Incident Priority]{.underline}

Click on the "Priority" hyperlink under Incident Standard Fields to
bring up the Incident Priority mapping configuration screen:

![](img/Using_SpiraTeam_with_JIRA_3__4_58.png)




The table lists each of the incident priorities available in SpiraTeam
and provides you with the ability to enter the matching JIRA priority ID
for each one. You can map multiple SpiraTeam fields to the same JIRA
fields, in which case only one of the two values can be listed as
Primary = Yes as that's the value that's used on the reverse
synchronization (from JIRA \> SpiraTeam).

*Note: The JIRA ID can be found by looking at the URL inside JIRA when
choosing to View/Edit the Priority. The URL will include the section:
**id=X** where X is the numeric ID of the Priority inside JIRA.*

[d) Incident Severity (Optional)]{.underline}

Click on the "Severity" hyperlink under Incident Standard Fields to
bring up the Incident severity mapping configuration screen:

![](img/Using_SpiraTeam_with_JIRA_3__4_59.png)




Unlike the other incident standard fields, JIRA doesn't actually have a
built-in field for storing the severity of an issue, so if you want to
be able to see the SpiraTeam incident severity in JIRA, you'll need to
create a JIRA custom list field to store the different severity values.
If you don't want to synchronize severity values with JIRA, you can skip
the rest of this section.

Once you have created a custom field in JIRA to contain the list of
severity values, you need to now populate the above table with the name
(Not the ID) of the severity custom property values inside JIRA and
click Update. Secondly you need to go to the Plug-in configuration
screen:

![](img/Using_SpiraTeam_with_JIRA_3__4_52.png)




On this screen you need to enter the ID of the custom field that you're
using to store severities in JIRA and populate the Custom 01 property
with this value (see above). *Note: The ID can be found by looking at
the URL inside JIRA when choosing to View/Edit the Custom Field. The URL
will include the section: **id=X** where X is the numeric ID of the
Custom Field inside JIRA.*

### Configuring the Custom Property Mapping

Now that the various SpiraTeam standard fields have been mapped
correctly, we need to configure the custom property mappings. This is
used for both custom properties in SpiraTeam that map to custom fields
in JIRA and also for custom properties in SpiraTeam that are used to map
to standard fields in JIRA (Component, Environment, Resolution and
SecurityLevel) that don't exist in SpiraTeam.

From the View/Edit Project Data Mapping screen, you need to click on the
name of the Incident Custom Property that you want to add data-mapping
information for. We will consider the four different types of mapping
that you might want to enter:

![](img/Using_SpiraTeam_with_JIRA_3__4_60.png)




[a) Text Custom Properties]{.underline}

Click on the hyperlink of the text custom property under Incident Custom
Properties to bring up the custom property mapping configuration screen.
For text custom properties there will be no values listed in the lower
half of the screen.

![](img/Using_SpiraTeam_with_JIRA_3__4_61.png)




You need to lookup the ID of the custom field in JIRA that matches this
custom property in SpiraTeam. Once you have entered the id of the custom
field, click \[Update\].

*Note: The ID can be found by looking at the URL inside JIRA when
choosing to View/Edit the Custom Field. The URL will include the
section: **id=X** where X is the numeric ID of the Custom Field inside
JIRA.*

[b) List Custom Properties]{.underline}

Click on the hyperlink of the list custom property under Incident Custom
Properties to bring up the custom property mapping configuration screen.
For list custom properties there will be a textbox for both the custom
field itself and a mapping table for each of the custom property values
that need to be mapped:

![](img/Using_SpiraTeam_with_JIRA_3__4_62.png)




First you need to lookup the ID of the custom field in JIRA that matches
this custom property in SpiraTeam. This should be entered in the
'External Key' field below the name of the custom property. *Note: The
ID can be found by looking at the URL inside JIRA when choosing to
View/Edit the Custom Field. The URL will include the section: **id=X**
where X is the numeric ID of the Custom Field inside JIRA.*

Next for each of the Property Values in the table (in the lower half of
the page) you need to enter the full name (not the id this time) of the
custom field value as specified in JIRA.

[c) JIRA's Component Field]{.underline}

If your instance of JIRA requires that all new issues are submitted with
a 'Component' then you will need to fill out this section. You first
need to create an incident custom property in SpiraTeam of type 'LIST'
that contains the various component names that exist inside JIRA.

Then click on the hyperlink of this new list custom property under
Incident Custom Properties to bring up the custom property mapping
configuration screen:

![](img/Using_SpiraTeam_with_JIRA_3__4_63.png)




First you need to enter the word "**Component**" as the External Key of
the custom property. This tells the data-sync plug-in that the custom
property in SpiraTeam should be mapped to built-in Component field in
JIRA.

Next for each of the Property Values in the table (in the lower half of
the page) you need to enter the JIRA ID of the various Components that
are configured in JIRA. The external ID can be found by looking at the
URL inside JIRA which choosing to View/Edit the component
name/description.

[d) JIRA's Resolution Field]{.underline}

If you would like the values of the JIRA '**Resolution'** field to be
synchronized back to SpiraTeam, then you will need to fill out this
section. You first need to create an incident custom property in
SpiraTeam of type 'LIST' that contains the various resolution names that
exist inside JIRA.

Then click on the hyperlink of this new list custom property under
Incident Custom Properties to bring up the custom property mapping
configuration screen:

![](img/Using_SpiraTeam_with_JIRA_3__4_64.png)




First you need to enter the word "Resolution" as the External Key of the
custom property. This tells the data-sync plug-in that the custom
property in SpiraTeam should be mapped to built-in Resolution field in
JIRA.

Next for each of the Property Values in the table (in the lower half of
the page) you need to enter the JIRA ID of the various Resolutions that
are configured in JIRA. The external ID can be found by looking at the
URL inside JIRA which choosing to View/Edit the resolution
name/description.

[e) JIRA's Environment Field]{.underline}

If your instance of JIRA requires that all new issues are submitted with
an 'Environment' description specified, then you will need to fill out
this section. You first need to create an incident custom property in
SpiraTeam of type 'TEXT' that will be used to store the environment
description within SpiraTeam.

Then click on the hyperlink of this new list custom property under
Incident Custom Properties to bring up the custom property mapping
configuration screen:

![](img/Using_SpiraTeam_with_JIRA_3__4_65.png)




All you need to do on this screen is enter the word "**Environment**" in
the External Key textbox and the data-sync plug-in will know that this
custom property is mapped to the built-in Environment field in JIRA.

[f) JIRA's Security Level Field (JIRA 4.x Plug-In Only)]{.underline}

If your instance of JIRA requires that all new issues are submitted with
a 'Security Level' then you will need to fill out this section. You
first need to create an incident custom property in SpiraTeam of type
'LIST' that contains the various security levels that exist inside JIRA.

Then click on the hyperlink of this new list custom property under
Incident Custom Properties to bring up the custom property mapping
configuration screen.

First you need to enter the word "**SecurityLevel**" as the External Key
of the custom property. This tells the data-sync plug-in that the custom
property in SpiraTeam should be mapped to built-in Security Level field
in JIRA.

Next for each of the Property Values in the table (in the lower half of
the page) you need to enter the JIRA ID of the various Security Levels
that are configured in JIRA. The external ID can be found by looking at
the URL inside JIRA which choosing to View/Edit the security level
name/description.

[g) JIRA's Issue Key Field (JIRA 4.x Plug-In Only)]{.underline}

It can be convenient to create a SpiraTeam custom property to store the
JIRA Issue Key (the ID used to identify an issue in JIRA). This allows
you to display a list of incients in SpiraTest and see the corresponding
JIRA ID in the same list. You first need to create an incident custom
property in SpiraTeam of type 'TEXT' that will be used to store the JIRA
issue key within SpiraTeam.

Then click on the hyperlink of this new list custom property under
Incident Custom Properties to bring up the custom property mapping
configuration screen:

![](img/Using_SpiraTeam_with_JIRA_3__4_66.png)




All you need to do on this screen is enter the word "**JiraIssueKey**"
in the External Key textbox and the data-sync plug-in will know that
this custom property is mapped to the built-in Issue Key field in JIRA.

Once you have updated the various mapping sections, you are now ready to
start using the system.

## Using SpiraTeam with JIRA

Now that the integration service has been configured and the service
started, initially any incidents created in SpiraTeam for the specified
projects will be imported into JIRA and if using JIRA 4.x, any existing
issues in JIRA will get loaded into SpiraTeam

At this point we recommend opening the Windows Event Viewer and choosing
the Application Log. In this log any error messages raised by the
SpiraTeam Data Sync Service will be displayed. If you see any error
messages at this point, we recommend immediately stopping the SpiraTeam
service and checking the various mapping entries. If you cannot see any
issues with the mapping information, we recommend sending a copy of the
event log message(s) to Inflectra customer services
(<support@inflectra.com>) who will help you troubleshoot the problem.

To use SpiraTeam with JIRA on an ongoing basis, we recommend the
following general processes be followed:

When running tests in SpiraTest or SpiraTeam, defects found should be
logged through the Test Execution Wizard as normal.

Developers using JIRA 4.x can log new defects into either SpiraTeam or
JIRA. In either case they will get loaded into the other system.

Once created in one of the systems and successfully replicated to the
other system, the incident should not be modified again inside SpiraTeam

At this point, the incident should not be acted upon inside SpiraTeam
and all data changes to the issue should be made inside JIRA. To enforce
this, you should modify the workflows set up in SpiraTeam so that the
various fields are marked as inactive for all the incident statuses
other than the "New" status. This will allow someone to submit an
incident in SpiraTeam, but will prevent them making changes in conflict
with JIRA after that point.

As the issue progresses through the customized JIRA workflow, changes to
the type of issue, changes to its status, priority, description and
resolution will be updated automatically in SpiraTeam. In essence,
SpiraTeam acts as a read-only viewer of these incidents.

You are now able to perform test coverage and incident reporting inside
SpiraTest/SpiraTeam using the test cases managed by SpiraTest/SpiraTeam
and the incidents managed on behalf of SpiraTest/SpiraTeam inside JIRA.

