# Using Spira with *monday.com*

This section outlines how to use SpiraTest, SpiraTeam, or SpiraPlan
(hereafter referred to as Spira) in conjunction with *monday.com* products. This data sync engine allows bringing new *monday* items as Tasks and Incidents in Spira (and vice versa), as well as updating artifacts and items in both systems.

!!! danger "Set up data synchronization"
    **STOP! Please make sure you have first read the instructions to [set up  the data sync](../Setting-up-Data-Synchronization/) before proceeding!**

The *monday.com* products are cloud-based platforms that allows users to create their own applications and work management software with more than 50 integrations with other applications.

## Configuring the Integration Service 

This section outlines how to set up the integration service between
*monday* and Spira. It assumes that you already have a working
installation of Spira and a valid *monday* account, workspace and board to integrate with.
To setup the service, you must be logged into Spira as a user with
System-Administrator level account.

Inside Spira, go to the Administration page and navigate to the
Integration \> Data Synchronization webpage. Check that you don't
already have a Plug-In called "MondayDataSync".

If you already have a plug-in called *MondayDataSync*, please click on
its `edit` button, otherwise please click the `Add` button to create a
new plug-in.

Now fill out this configuration page as follows:

![](img/Using_Spira_with_monday_1.png)


You need to fill out the following fields for the *monday* Data Sync
plugin to work properly:

-   **Name** -- This needs to be set to **MondayDataSync**

-   **Caption** -- This is the display name of the plug-in, generally
something generic like "*monday*" would work.

-   **Description** -- The description of what you're using the plug-in
for. This field is entirely optional and is not used by the system
in any way.

-   **Connection Info** -- This field is not used by this data sync engine. Please leave it blank.

-   **Login** -- This field is not used by this data sync engine. Please leave it blank.

-   **Password** -- Your *monday.com* API token. You can learn how to generate and copy your personal API token [here](https://developer.monday.com/api-reference/docs/authentication#accessing-api-tokens).

-   **Time Offset** -- This should be set to 0, but if you find that
changes are not being synced, try increasing the value to tell the
plugin to offset timestamps.

-   **Sync Mode** -- This option allows choosing between unidirectional or bidirectional syncing of items and/or artifacts between the systems. The valid values are: *monday_to_spira*, *spira_to_monday*, or *bidirectional*. Please choose one and type it into this field. If this field is left blank, the bidirectional sync will be assumed.
-   **Artifact Sync Mode** -- Use this field to set how the artifact and/or item interaction will proceed between the two systems. The valid values are: *tasks_only*, *incidents_only*, or *both*. By choosing the first option, for example, you can limit the sync to just Tasks. Please choose one and type it into this field. If this field is blank, the data sync will look for changes in both artifacts.
-   **Sync subitems?** -- If you want the *monday* subitems to be synced to Spira, please enter *yes* to this field. If you want the datasync to just skip *monday* subitems, enter *no*. You can learn more about this by going to the 'Subitems' section of this documentation. If you are using the *spira_to_monday* sync mode, you can ignore this option.

Once all those fields have
been filled out, click the `Add` or `Save` button to save your changes.

## Configuring Project Mappings

For this step, please ensure that you are in the Spira project you
would like to sync with *monday*. For this example, the project is called
"Monday.com DS Team Management".

Click on the "View Project Mappings" button for *monday* Data Sync. You
need to fill out the following fields to sync correctly:

![](img/Using_Spira_with_monday_2.png)

-   **External Key** -- This field needs to follow the template: `Workspace||Task Board,,Incident Board`. Please enter your *monday* Workspace name followed by two pipe characters `(||)`, then the *monday* board name you want to sync with Tasks in Spira followed by two commas `(,,)`, and finally the *monday* board name you want to sync with Incidents in Spira. Please note that all the pipes and commas are always required. If you don't want to sync Incidents for example, your external key should be something such as *`myWorkspace||,,MyIncidentBoard`*. Make sure to enter the exact name of the workspace and board(s) on the product external key, otherwise the data may be synced to the wrong workspace and board(s).

-   **Active** -- Set this to yes so that the Data Sync plug-in knows to
synchronize with this project.

Use this as a reference to find the necessary names in *monday*:

![](img/Using_Spira_with_monday_3.png)

The *monday* plugin can synchronize Incidents and Tasks, so you will need to set up the status mappings for these artifacts, accordingly to the Artifact Sync Mode you chose. We shall discuss each in turn.

### Configuring the Incident Status Mapping

Now click the "Status" button within the "Incident" section to map the
incident statuses together. The purpose of this is so that the *monday*
Data Sync plug-in knows what the equivalent status is in *monday* for an
incident status in Spira. Please make sure this is called `Status` in *monday*.

![](img/Using_Spira_with_monday_4.png)

You must map every status in the system. Descriptions of the field are
below:

-   **External Key** -- Status is a dropdown in *monday*, so please match the Status names with the Spira statuses. Please make sure to type the exact name you see in *monday*. Also, make sure to use a single option dropdown menu for this option in *monday*, as Spira does not support having multiple Incident Status.

-   **Primary** -- You must have exactly one primary key for each *monday* status. This is what status the plug-in should set the incident in SpiraPlan to when the status in *monday* changes. This is only used if there are more options in SpiraPlan than *monday*.

### Configuring the Incident Priority Mapping

Select the "Priority" button within the "Incident" section to map the
incident priorities together. The purpose of this is so that the *monday*
Data Sync plug-in knows what the equivalent priority is in *monday* for an
incident priority in Spira. Please make sure this is called `Priority` in *monday*.

![](img/Using_Spira_with_monday_5.png)

You must map every priority in the system. Descriptions of the field are
below:

-   **External Key** -- Priority is a dropdown in *monday*, so please match the Priority names with the Spira priorities. Please make sure to type the exact name you see in *monday*. Also, make sure to use a single option dropdown menu for this option in *monday*, as Spira does not support having multiple Incident Priority.

-   **Primary** -- You must have exactly one primary key for each *monday* priority. This is what status the plug-in should set the incident in SpiraPlan to when the priority in *monday* changes. This is only used if there are more options in SpiraPlan than *monday*.

### Configuring the Incident Type Mapping

Select the "Type" button within the "Incident" section to map the
incident types together. The purpose of this is so that the *monday*
Data Sync plug-in knows what the equivalent type is in *monday* for an
incident type in Spira. Please make sure this is called `Type` in *monday*.

![](img/Using_Spira_with_monday_6.png)

You must map every Type in the system. Descriptions of the field are
below:

-   **External Key** -- Type is a dropdown in *monday*, so please match the Type names with the Spira types. Please make sure to enter the exact name you see in *monday*. Also, make sure to use a single option dropdown menu for this option in *monday*, as Spira does not support having multiple Incident types.

-   **Primary** -- You must have exactly one primary key for each *monday* Type. This is what status the plug-in should set the incident in SpiraPlan to when the Type in *monday* changes. This is only used if there are more options in SpiraPlan than *monday*.

### Configuring the Incident Severity Mapping

Now click the "Severity" button within the "Incident" section to map the
incident severities together. Use the same logic as described in the `Incident Priority Mapping` section.

### Configuring the Task Status Mapping

Click the "Status" button within the "Task" section to map the
task statuses together. Use the same logic as described in the `Incident Status Mapping` section.

### Configuring the Task Priority Mapping

Click the "Priority" button within the "Task" section to map the
task priorities together. Use the same logic as described in the `Incident Priority Mapping` section.

### Configuring the Task Type Mapping

Click the "Type" button within the "Task" section to map the
task types together. Use the same logic as described in the `Incident Type Mapping` section.

### Configuring the User Mapping
To configure the mapping of users in the two systems, you need to go to
Administration \> Users \> View Edit Users, which will bring up the list
of users in the system. Then click on the "Edit" button for a particular
user that will be editing items in *monday*:

![](img/Using_Spira_with_monday_7.png)

Click on the 'Data Mapping' tab to list all the configured
data-synchronization plug-ins for this user. In the text box next to the
Monday.com Data-Sync plug-in you need to enter the display name for this
user in *monday*. This will allow the data-synchronization plug-in to know
which user in Spira match which equivalent user in *monday*. Click
`Save` once you've entered the appropriate login name. You should now
repeat for the other users who will be active in both systems.

*If you have set the "Auto-Map Users" option in the *monday* plugin, you
can skip this section completely.*

### Configuring *monday* fields

The sheer configurability of *monday* meant some assumptions were made in the designing of this data sync. Specific column names are mapped to their counterparts in SpiraPlan based on the list below. If a field is not present in *monday*, it will not be synced.

| Spira Field | *monday* Field Name | *monday* Field Type
| ----------- | ----------- |
| Incident Description| Description|Text
| Incident Priority| Priority|Single Dropdown (Status)
| Incident Severity| Severity |Single Dropdown (Status)
| Incident Type| Type |Single Dropdown (Status)
| Incident Status| Status |Single Dropdown (Status)
| Incident Start Date| Start Date |Date
| Incident End Date| End Date |Date
| Incident Detected By| Creator |People
| Incident Owner| Owner |People
| Task Description| Description|Text
| Task Priority| Priority|Single Dropdown (Status)
| Task Type| Type |Single Dropdown (Status)
| Task Status| Status |Single Dropdown (Status)
| Task Start Date| Start Date |Date
| Task End Date| End Date |Date
| Task Creator| Creator |People
| Task Owner| Owner |People

It's also possible to sync the *monday* item Group to a Spira custom property for Incidents and/or Tasks. To do that, in Spira:
- Create a Custom List - choose any name you want
- Add the *monday* group names to this custom list. Make sure they match exactly the group names in *monday*. E.g.: This Week, Next Week, etc.
- Add a new Custom Property type List to the artifact you are syncing in Spira (Incidents and/or Tasks) and link it with the just created list. You can choose any name you want for this custom property.
- Go to the Product Data Mapping options for this Data Sync in Spira and select the Custom Property you just created within the target artifact. As the External Key value, enter exactly **MondayGroup**. To save and finish, click on 'Update'.


Additionally, please make sure that the board(s)/workspace names provided as External Key of a Spira Product are unique through the workspace/system, otherwise, the data may be synced to the wrong board/workspace.
Due to the nature of text fields in *monday* (only plain text is supported), descriptions will only be synced from Monday to Spira on creation and from Spira to Monday all the time.

### Monday sub-items

Monday allows users to create sub-items for any item in the boards. By default, the data sync will sync these subitems in Spira. They will have their parent linked under the 'Associations' tab in Spira. To turn off the subitems sync feature, change the **Sync subitems?** property of the data sync to `no`. It's not possible to create subitems in *monday* from Spira.

![](img/Using_Spira_with_monday_8.png)

## Using the Data Synchronization

Assuming everything was done correctly, the plug-in should start
working. If you are using Spira on-premise, start your Data Sync service and you can now start synchronizing incidents and/or tasks

### Synchronizing Spira Incidents

If you selected `both` or `incidents_only` as your Artifact Sync Mode, and `spira_to_monday` or `bidirectional` as the Sync Mode, when you log a new incident in Spira, it will appear in *monday* as a new item of your Incidents Board:

![](img/Using_Spira_with_monday_9.png)

If you selected `monday_to_spira` or `bidirectional` as the Sync Mode, when you add a new item in your *monday* Incidents Board, it will appear in Spira as a new Incident.


### Synchronizing Spira Tasks

If you selected `both` or `tasks_only` as your Artifact Sync Mode, and `spira_to_monday` or `bidirectional` as the Sync Mode, when you create a new task in Spira, it will appear in *monday* as a new item of your Tasks Board:

![](img/Using_Spira_with_monday_10.png)

If you selected `monday_to_spira` or `bidirectional` as the Sync Mode, when you add a new item in your *monday* Tasks Board, it will appear in Spira as a new Task.


## Summary

Congratulations, you have just integrated your Spira instance with
the *monday.com* project managing system.